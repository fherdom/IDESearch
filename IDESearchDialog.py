﻿# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name : IDECANARIAS Search
Description          : Perform querys in toponimia
Date                 : 19/Aug/11 
copyright            : (C) 2011 by Felix J. Hdez
email                : fhernandeze@grafcan.es 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

http://qgis.org/pyqgis-cookbook/plugins.html

"""
import os, sys, base64, re
import psycopg2
import pprint
import tempfile
import math

from datetime import datetime

from PyQt4 import QtCore, QtGui, QtXml
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
from PyQt4.QtNetwork import QHttp

from qgis.core import *
import qgis.utils

from form002 import Ui_Dialog as Ui_IDESearch

from Utils import *

class IDESearchDialog(QtGui.QDialog):
    """
    """
    
    def __init__(self, iface):
        """
        """
        self.iface = iface
        self.canvas = iface.mapCanvas()
        QtGui.QDialog.__init__(self) 
        
        # Set up the user interface from Designer. 
        self.ui = Ui_IDESearch()
        self.ui.setupUi(self)
        self.http = QHttp()
        self.httpogr = QHttp()
        self.url = QUrl()
        self._radio = 0
        self._point = None
        self._pointutm = None
        self.i = None

        self.layer = None
        self.layerid = ''
        
        self.chkRemote = False
        
        self.tblResultHeader = [QString.fromUtf8('Nombre'), QString.fromUtf8('Clasificación'), QString.fromUtf8('Localización')]
        self.ui.tblResult.setHorizontalHeaderLabels(self.tblResultHeader)
        
        #self.connect(self.ui.btnSearch, SIGNAL("clicked()"),                    self.onClick_btnSearch)
        self.connect(self.ui.txtSearch, SIGNAL("returnPressed(void)"),          self.onClick_btnSearch)
        self.connect(self.ui.tblResult, SIGNAL("cellDoubleClicked(int,int)"),   self.onDblClick_tblResult)
        #self.connect(self.ui.chkRemote, SIGNAL("clicked()"),                    self.onClick_chkRemote)
        self.connect(self.http, QtCore.SIGNAL("done(bool)"),                    self.onDone_http)
        self.connect(self.httpogr, QtCore.SIGNAL("done(bool)"),                 self.onDone_httpogr)
        self.connect(self.ui.radiodms, SIGNAL("toggled(bool)"),                 self.__setRadiodms)
        self.connect(self.ui.radiodm, SIGNAL("toggled(bool)"),                  self.__setRadiodm)
        self.connect(self.ui.radiod, SIGNAL("toggled(bool)"),                   self.__setRadiod)
        self.connect(self.ui.radioutm, SIGNAL("toggled(bool)"),                 self.__setRadioutm)
        self.connect(self.ui.btnGet, SIGNAL("clicked()"),                       self.onClick_btnGet)
        self.connect(self.ui.btnGo, SIGNAL("clicked()"),                        self.onClick_btnGo)
        self.connect(self.ui.txtCoordinates, SIGNAL("returnPressed(void)"),     self.onClick_btnGo)
        self.connect(self.ui.btnClipboard, SIGNAL("clicked()"),                 self.onClick_btnClipboard)
        
        baseDirectory = os.path.dirname(__file__)
        fillPath = lambda x: os.path.join(baseDirectory, x)
        staticPath, templatePath, databasePath, filenamelog = map(fillPath, ['static', 'templates', '.database', 'idecanarias.log'])
        databaseName, databaseUser, databasePassword, databaseHost = open(databasePath).read().splitlines()
        self.conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (databaseHost, databaseName, databaseUser, databasePassword)

        # Log file
        self.DEBUG = True
        self.filenamelog = filenamelog
        self.Log("init app")
        
    def Log(self, msg):
        """
        """
        if self.DEBUG:
            f = open(self.filenamelog, "a")
            f.write("%s: %s\n" % (datetime.now(), msg))
            f.close()
        
    def alert(self, msg):
        """
        """
        QtGui.QMessageBox.warning(self, QString.fromUtf8("Búsquedas IDECANARIAS"), msg)
        
    def __setRadiodms(self, checked):
        """
        """
        if checked:
            self._radio = 0
        self.reverse_action(None)        

    def __setRadiodm(self, checked):
        """
        """
        if checked:
            self._radio = 1      
        self.reverse_action(None)              

    def __setRadiod(self, checked):
        """
        """
        if checked:
            self._radio = 2
        self.reverse_action(None)                    

    def __setRadioutm(self, checked):
        """
        """
        if checked:
            self._radio = 3
        self.reverse_action(None)            

    def onClick_chkRemote(self):
        """
        """
        self.ui.tblResult.clear()
        self.ui.tblResult.setRowCount(0)
        self.ui.tblResult.setHorizontalHeaderLabels(self.tblResultHeader)

    def onClick_btnClipboard(self):
        """
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.txtCoordinates.text()) 

    def onClick_btnGet(self):
        """
        """
        ct = ClickTool(self.iface, self.reverse_action);
        self.iface.mapCanvas().setMapTool(ct)

    def onClick_btnGo(self):
        """
        develop er to parse this: 
        28º 07' 9.7249'' S, 15º 25' 30.9814'' O
        28º 07.16208' S, 15º 25.51637' O
        28.11936800, -15.42527283
        458232.06, 3110498.55
        
        Algorithm
        lat = 45 + (25 / 60) + (2.98 / 3600)
        lng = 10 + (11 / 60) + (30.29 / 3600)
        """
        
        lat = None
        lng = None
        x = None
        y = None
        
        texto = self.ui.txtCoordinates.text().toUtf8()
        if not texto:
            texto = "28º 07' 9.7249'' N, 15º 25' 30.9814'' O"
        
        patterndms = r"^([\d]{1,3})\º ([\d]{1,3})\' ([\d]{1,3}(\.\d+)?)\'\' ([NS]),\s*([\d]{1,3})\º ([\d]{1,3})\' ([\d]{1,3}(\.\d+)?)\'\' ([EO])$"
        m = re.match(patterndms, texto)    
        if m:
            lat = int(m.group(1)) + (float(m.group(2)) / 60) + (float(m.group(3)) / 3600)
            lng = int(m.group(6)) + (float(m.group(7)) / 60) + (float(m.group(8)) / 3600)
            if m.group(5) == "S":
                lat = -lat
            if m.group(10) == "O":
                lng = -lng
            self.ui.radiodms.setChecked(True)

        patterndm = r"^([\d]{1,3})\º ([\d]{1,3}(\.\d+)?)\' ([NS]),\s*([\d]{1,3})\º ([\d]{1,3}(\.\d+)?)\' ([EO])$"
        m = re.match(patterndm, texto)
        if m:
            lat = int(m.group(1)) + (float(m.group(2)) / 60) 
            lng = int(m.group(5)) + (float(m.group(6)) / 60)
            if m.group(4) == "S":
                lat = -lat
            if m.group(8) == "O":
                lng = -lng
            self.ui.radiodm.setChecked(True) 
            
        m = re.match(r"^(\-?[\d]{1,3}(\.\d+)?),\s*(\-?[\d]{1,3}(\.\d+)?)$", texto)
        if m:
            lat = float(m.group(1))
            lng = float(m.group(3))
            self.ui.radiod.setChecked(True)
            
        # convert to UTM
        self.Log("%s, %s (%s)" % (lat, lng, texto))
        
        if lat and lng:
            point = QgsPoint(lng, lat)
            self._point = point
            self._pointutm = pointFromWGS84(point)
            x = self._pointutm[0]
            y = self._pointutm[1]

        m = re.match(r"^(\d+(\.\d+)?),\s*(\d+(\.\d+)?)$", texto)
        if m:
            x = float(m.group(1))
            y = float(m.group(3))
            self._pointutm = QgsPoint(x, y)
            self._point = pointToWGS84(self._pointutm)
            self.ui.radioutm.setChecked(True)

        # reverse lat/lon
        # Use pdb for debugging
        #import pdb
        ## These lines allow you to set a breakpoint in the app
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        #qDebug('Reversing point %s %s' % (x, y))
        if x and y:

            # Get current extent
            scale = 1
            extent = self.canvas.extent()
            width = extent.width() * scale
            height = extent.height() * scale
            
            # Recenter
            rect = QgsRectangle(  \
                            x - width/2.0 \
                            , y - height/2.0 \
                            , x + width/2.0 \
                            , y + height/2.0)
    
            # Set the extent to our new rectangle
            self.canvas.setExtent(rect)
            # Refresh the map
            self.canvas.refresh()
            
            # create layer
            if not QgsMapLayerRegistry.instance().mapLayer(self.layerid):
                self.layer = QgsVectorLayer("Point", QString.fromUtf8("Resultados de conversión"), "memory")
                self.provider = self.layer.dataProvider()
                self.layer.setCrs(get_dest_projection())

                # add fields
                self.provider.addAttributes( [
                    QgsField("nombre", QVariant.String),
                    QgsField("x", QVariant.Double),
                    QgsField("y", QVariant.Double),
                ] )
            
                # Makes fields visible
                self.layer.updateFieldMap()
            
                # Labels on
                label = self.layer.label()
                label.setLabelField(QgsLabel.Text, 0)
                self.layer.enableLabels(True)

                # add layer if not already
                QgsMapLayerRegistry.instance().addMapLayer(self.layer)

                # store layer id
                self.layerid = QgsMapLayerRegistry.instance().mapLayers().keys()[-1]
                self.canvas.refresh()
            text = ""
            text, ok = QInputDialog.getText(self, QString.fromUtf8('IDECanarias'), QString.fromUtf8('Introduzca una descripción:'))
            
            # add a feature
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(self._pointutm))
            fet.setAttributeMap( {
                    0 : QVariant(str(text)),
                    1 : QVariant(self._pointutm[0]),
                    2 : QVariant(self._pointutm[1]),
                } )
            self.provider.addFeatures([fet])
    
            # update layer's extent when new features have been added
            # because change of extent in provider is not propagated to the layer
            self.layer.updateExtents()
            self.canvas.refresh()
        else:
            self.alert("Coordenadas incorrectas")
            
    def reverse_action(self, point):
        """
        """
        if point and (point != self._pointutm):
            self._pointutm = point
        
        if self._pointutm == None:
            return
        
        pt = pointToWGS84(self._pointutm)
        self._point = pt
        
        latitude = pt[1]    # 28....
        longitude = pt[0]   # -16....
       
        # Convert to deg, min, secs
        latitude_sign = 0
        if latitude < 0:
            latitude_sign = -1

        longitude_sign = 0
        if longitude < 0:
            longitude_sign = -1
        
        latitude_deg = math.floor(math.fabs(latitude))
        latitude_min = math.floor((math.fabs(latitude) - latitude_deg) * 60)
        latitude_min_ = (math.fabs(latitude) - latitude_deg) * 60
        #latitude_sec = math.ceil(((math.fabs(latitude) - latitude_deg) * 60 - latitude_min) * 60)
        latitude_sec = ((math.fabs(latitude) - latitude_deg) * 60 - latitude_min) * 60
        
        latitude_dir = "S"
        if latitude_sign == 0:
            latitude_dir = "N"
        
        longitude_deg = math.floor(math.fabs(longitude))
        longitude_min = math.floor((math.fabs(longitude) - longitude_deg) * 60)
        longitude_min_ = (math.fabs(longitude) - longitude_deg) * 60
        #longitude_sec = math.ceil(((math.fabs(longitude) - longitude_deg) * 60 - longitude_min) * 60)
        longitude_sec = ((math.fabs(longitude) - longitude_deg) * 60 - longitude_min) * 60
        
        longitude_dir = "O"
        if longitude_sign == 0:
            longitude_dir = "E"
        
        data = ""
        if self._radio == 0:
            data = "%02.0fº %02.0f\' %06.4f\'\' %s, %02.0fº %02.0f\' %06.4f\'\' %s" % (latitude_deg, latitude_min, latitude_sec, latitude_dir, longitude_deg, longitude_min, longitude_sec, longitude_dir) 
        elif self._radio == 1:
            data = "%02.0fº %08.5f\' %s, %02.0fº %08.5f\' %s" % (latitude_deg, latitude_min_, latitude_dir, longitude_deg, longitude_min_, longitude_dir)
        elif self._radio == 2:
            data = "%.8f, %.8f" % (latitude, longitude)            
        elif self._radio == 3:
            #data = "%s; %s" % ('{0:,.2f}'.format(self._point[0]), '{0:,.2f}'.format(self._point[1]))
            data = "%s, %s" % ('{0:.2f}'.format(self._pointutm[0]), '{0:.2f}'.format(self._pointutm[1]))
        else:
            data = "" 
        self.ui.txtCoordinates.setText(QString.fromUtf8(data))
     
    def onClick_btnSearch(self):
        """
        """
        texto = self.ui.txtSearch.text()
        if not texto:
            texto = "grafcan"

        if self.chkRemote:
            self.http.setHost('visor.grafcan.es', 80)
            url = QUrl('/busquedas/toponimoxml/1/50/?texto=%s' % texto)
            path = url.toEncoded()
            self.http.get(str(path))
        else:
            try:
                conn = psycopg2.connect(self.conn_string)
                conn.set_client_encoding('LATIN1')
                cursor = conn.cursor()
                sql = "select * from topo.getbytext('%s',1,50) as (id integer, localizacion text, clasificacion character varying(255), nombre text, descripcion text, rank real, x double precision, y double precision, imagen character varying(64), codigo character varying(10), total bigint)" % texto
                cursor.execute(sql)
                self.ui.lblResult.setText(self.tr("%1 lugar(es) encontrados").arg(cursor.rowcount) + QString.fromUtf8(" (Haz doble click para ver su localización)"))
                self.lid = []
                lidd = []
                self.ui.tblResult.clear()
                self.ui.tblResult.setRowCount(0)
                self.ui.tblResult.setHorizontalHeaderLabels(self.tblResultHeader)
                for record in cursor.fetchall():
                    lidd.append("%s - %s [%s]" % (record[3], record[2], record[1]))
                    self.lid.append(record)
                    row = self.ui.tblResult.rowCount()
                    self.ui.tblResult.insertRow(row)
                    item001 = QTableWidgetItem(record[3])
                    item002 = QTableWidgetItem(record[2])
                    item003 = QTableWidgetItem(record[1])
                    self.ui.tblResult.setItem(row, 0, item001)
                    self.ui.tblResult.setItem(row, 1, item002)
                    self.ui.tblResult.setItem(row, 2, item003)
                self.ui.tblResult.resizeColumnsToContents()
                cursor.close()
            except:
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                self.alert(self.tr("Database connection failed!\n ->%1").arg(exceptionValue))
                
    def onDblClick_tblResult(self, i, j):
        """
        """
        if self.chkRemote:
            id = self.lid[i]["id"]
            self.i = i
            self.httpogr.setHost('visor.grafcan.es', 80)
            self.httpogr.get('/busquedas/toponimiagml/1/50/qgis/1/%d/' % int(id))
        else:
            id = self.lid[i][0]
            localizacion = self.lid[i][1]
            clasificacion = self.lid[i][2]
            nombre = self.lid[i][3]
            fngml = "topo.getgml"
            try:
                conn = psycopg2.connect(self.conn_string)
                conn.set_client_encoding('LATIN1')
                
                # GEOM
                cursor = conn.cursor()
                sql = "select * from %s(%d)" % (fngml, id)
                cursor.execute(sql)
                row = cursor.fetchone()
                gml = ""
                if row[0]:
                    geometria = row[0]
                cursor.close()
                
                # FILE
                filename = os.path.join(str(QtCore.QDir.tempPath()), "XXXXXX.gml")
                file = QtCore.QTemporaryFile(filename)
                file.setAutoRemove(False)
                if not file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
                    self.alert(self.tr("No puedo escribir en %1:\n%2.").arg(filename).arg(file.errorString()))
                    return False
    
                bbox = ""
                gml = """<?xml version="1.0" encoding="UTF-8"?>
<wfs:FeatureCollection 
    xmlns:ms="http://mapserver.gis.umn.edu/mapserver" 
    xmlns:wfs="http://www.opengis.net/wfs" 
    xmlns:gml="http://www.opengis.net/gml" 
    xmlns:ogc="http://www.opengis.net/ogc" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.0.0/WFS-basic.xsd">
    <gml:boundedBy>
        <gml:Box srsName="EPSG:32628">
            <gml:coordinates>%s</gml:coordinates>
        </gml:Box>
    </gml:boundedBy>
    <gml:featureMember>
        <ms:capa fid="1">
            <ms:Nombre>%s</ms:Nombre>
            <ms:Clasificacion>%s</ms:Clasificacion>
            <ms:Localizacion>%s</ms:Localizacion>
            <ms:msGeometry>%s</ms:msGeometry>
        </ms:capa>
    </gml:featureMember>
</wfs:FeatureCollection>""" % (bbox, nombre, clasificacion, localizacion, geometria)
                
                outstr = QtCore.QTextStream(file)
                outstr.setCodec("UTF-8")
                outstr << gml
                filename = str(file.fileName())
                file.close()
                
                # show in qgis
                basename = os.path.basename(filename)
                self.iface.addVectorLayer(filename, "%s_%d" % (nombre, id), 'ogr')
                src = self.canvas.layers()[0].srs()
                dest = self.canvas.mapRenderer().destinationSrs()
                coodTrans = QgsCoordinateTransform(src, dest)
                extent = self.canvas.layers()[0].extent()
                newextent = coodTrans.transform(extent)
                self.canvas.setExtent(newextent)
                self.canvas.refresh()
                    
            except:
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print exceptionType, exceptionValue, exceptionTraceback
                self.alert(self.tr("Database connection failed!\n ->%1").arg(exceptionValue))
 
    def onDone_httpogr(self, error):
        """
        """
        filename = os.path.join(str(QtCore.QDir.tempPath()), "XXXXXX.gml")
        file = QtCore.QTemporaryFile(filename)
        file.setAutoRemove(False)
        
        if not file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            self.alert(self.tr("No puedo escribir en %1:\n%2.").arg(filename).arg(file.errorString()))
            return False

        outstr = QtCore.QTextStream(file)
        outstr << self.httpogr.readAll()
        filename = str(file.fileName())
        file.close()
        basename = os.path.basename(filename)
        
        id = None
        nombre = None        
        if self.i <> None:
            id = self.lid[self.i]["id"]
            nombre = self.lid[self.i]["nombre"]
            
            # show in qgis
            basename = os.path.basename(filename)
            self.iface.addVectorLayer(filename, "%s_%s" % (nombre, id), 'ogr')
            src = self.canvas.layers()[0].srs()
            dest = self.canvas.mapRenderer().destinationSrs()
            coodTrans = QgsCoordinateTransform(src, dest)
            extent = self.canvas.layers()[0].extent()
            newextent = coodTrans.transform(extent)
            self.canvas.setExtent(newextent)
            self.canvas.refresh()
                
        
    def onDone_http(self, error):
        """
        """
        doc = QtXml.QDomDocument("IDE")
        response = str(self.http.readAll())
        doc.setContent(response)
        id = nombre = clasificacion = localizacion = None
        
        self.ui.tblResult.clear()
        self.ui.tblResult.setRowCount(0)
        self.ui.tblResult.setHorizontalHeaderLabels(self.tblResultHeader)
        
        self.lid = []
        lidd = []
        root = doc.documentElement()
        node = root.firstChild()
        while (not node.isNull()):
            if(node.toElement().tagName() == "row"):
                child = node.firstChild()
                while (not child.isNull()):
                    if(child.toElement().tagName() == "id"):
                        try:
                            child2 = child.firstChild()
                            id = child2.toText().data()
                            #lidd.append(e["id"])
                        except:
                            QMessageBox.warning(self, "Error", "Could not parse xml file. Problem parsing %s." % (child2.toElement().tagName()))
                    elif (child.toElement().tagName() == "nombre"):
                        try:
                            child2 = child.firstChild()
                            nombre = child2.toText().data()
                            #lidd.append(e["nombre"])
                        except:
                            QMessageBox.warning(self, "Error", "Could not parse xml file. Problem parsing %s." % (child2.toElement().tagName()))
                    elif (child.toElement().tagName() == "clasificacion"):
                        try:
                            child2 = child.firstChild()
                            clasificacion = child2.toText().data()
                        except:
                            QMessageBox.warning(self, "Error", "Could not parse xml file. Problem parsing %s." % (child2.toElement().tagName()))                                                
                    elif (child.toElement().tagName() == "localizacion"):
                        try:
                            child2 = child.firstChild()
                            localizacion = child2.toText().data()
                        except:
                            QMessageBox.warning(self, "Error", "Could not parse xml file. Problem parsing %s." % (child2.toElement().tagName()))                                                
                                
                    child = child.nextSibling()
                e = {'id': id,
                         'nombre':  nombre,
                         'clasificacion': clasificacion,
                         'localizacion': localizacion
                         }

                #lidd.append(e["nombre"])
                lidd.append("%s - %s [%s]" % (clasificacion, localizacion, nombre))
                
            self.lid.append(e)
            row = self.ui.tblResult.rowCount()
            self.ui.tblResult.insertRow(row)
            item001 = QTableWidgetItem(nombre)
            item002 = QTableWidgetItem(clasificacion)
            item003 = QTableWidgetItem(localizacion)
            self.ui.tblResult.setItem(row, 0, item001)
            self.ui.tblResult.setItem(row, 1, item002)
            self.ui.tblResult.setItem(row, 2, item003)
            node = node.nextSibling()
        
        self.ui.lblResult.setText(self.tr("%1 lugar(es) encontrados").arg(len(self.lid)) + QString.fromUtf8(" (Haz doble click para ver su localización)"))
        self.ui.tblResult.resizeColumnsToContents()

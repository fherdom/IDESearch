# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name			 	 : IDECANARIAS Search
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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *

# Initialize Qt resources from file resources.py
import resources

# Import the code for the dock
from IDESearchDock import IDESearchDock

# Import the code for the dialog
from IDESearchDialog import IDESearchDialog

class IDESearch:
    """
    """
     
    def __init__(self, iface):
        """
        """
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.appname = QString.fromUtf8("Búsquedas IDECANARIAS")

        # Install dock
        self.dock = IDESearchDock(self.iface)
        self.iface.addDockWidget(Qt.BottomDockWidgetArea, self.dock)
        
    def initGui(self):
        """
        """
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/IDESearch/icon.png"), self.appname, self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("activated()"), self.run) 
        
        # Add toolbar button and menu item
        #self.iface.addToolBarIcon(self.action)
        #self.iface.addPluginToMenu(self.appname, self.action)

    def unload(self):
        """
        """
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(self.appname, self.action)
        self.iface.removeToolBarIcon(self.action)
        
    # run method that performs all the real work
    def run(self):
        """
        """
        # create and show the dialog 
        dlg = IDESearchDialog(self.iface)
        # show the dialog
        dlg.show()
        result = dlg.exec_() 
        # See if OK was pressed
        if result == 1: 
          # do something useful (delete the line containing pass and
          # substitute with your code
          pass 

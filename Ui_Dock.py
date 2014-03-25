# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_iDock.ui'
#
# Created: Wed Dec  5 10:40:15 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(322, 396)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.txtSearch = QtGui.QLineEdit(self.tab)
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
        self.verticalLayout.addWidget(self.txtSearch)
        self.chkBBOX = QtGui.QCheckBox(self.tab)
        self.chkBBOX.setObjectName(_fromUtf8("chkBBOX"))
        self.verticalLayout.addWidget(self.chkBBOX)
        self.tblResult = QtGui.QTableWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblResult.sizePolicy().hasHeightForWidth())
        self.tblResult.setSizePolicy(sizePolicy)
        self.tblResult.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblResult.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblResult.setColumnCount(3)
        self.tblResult.setObjectName(_fromUtf8("tblResult"))
        self.tblResult.setRowCount(0)
        self.verticalLayout.addWidget(self.tblResult)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblResult = QtGui.QLabel(self.groupBox)
        self.lblResult.setObjectName(_fromUtf8("lblResult"))
        self.horizontalLayout_2.addWidget(self.lblResult)
        self.btnLoad = QtGui.QPushButton(self.groupBox)
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.horizontalLayout_2.addWidget(self.btnLoad)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget = QtGui.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 5, 301, 183))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnClipboard = QtGui.QPushButton(self.layoutWidget)
        self.btnClipboard.setObjectName(_fromUtf8("btnClipboard"))
        self.gridLayout_2.addWidget(self.btnClipboard, 3, 0, 1, 1)
        self.txtCoordinates = QtGui.QLineEdit(self.layoutWidget)
        self.txtCoordinates.setObjectName(_fromUtf8("txtCoordinates"))
        self.gridLayout_2.addWidget(self.txtCoordinates, 1, 0, 1, 1)
        self.btnGo = QtGui.QPushButton(self.layoutWidget)
        self.btnGo.setObjectName(_fromUtf8("btnGo"))
        self.gridLayout_2.addWidget(self.btnGo, 2, 0, 1, 1)
        self.btnGet = QtGui.QPushButton(self.layoutWidget)
        self.btnGet.setObjectName(_fromUtf8("btnGet"))
        self.gridLayout_2.addWidget(self.btnGet, 4, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radioutm = QtGui.QRadioButton(self.layoutWidget)
        self.radioutm.setObjectName(_fromUtf8("radioutm"))
        self.gridLayout_3.addWidget(self.radioutm, 1, 0, 1, 1)
        self.radiodms = QtGui.QRadioButton(self.layoutWidget)
        self.radiodms.setChecked(True)
        self.radiodms.setObjectName(_fromUtf8("radiodms"))
        self.gridLayout_3.addWidget(self.radiodms, 0, 0, 1, 1)
        self.radiodm = QtGui.QRadioButton(self.layoutWidget)
        self.radiodm.setObjectName(_fromUtf8("radiodm"))
        self.gridLayout_3.addWidget(self.radiodm, 0, 1, 1, 1)
        self.radiod = QtGui.QRadioButton(self.layoutWidget)
        self.radiod.setObjectName(_fromUtf8("radiod"))
        self.gridLayout_3.addWidget(self.radiod, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        Dialog.setWidget(self.dockWidgetContents)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Búsquedas IDECanarias", None, QtGui.QApplication.UnicodeUTF8))
        self.chkBBOX.setText(QtGui.QApplication.translate("Dialog", "Limitar la búsqueda a la extensión actual", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResult.setText(QtGui.QApplication.translate("Dialog", "Encontrado (s)", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoad.setText(QtGui.QApplication.translate("Dialog", "Cargar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Lugar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClipboard.setText(QtGui.QApplication.translate("Dialog", "Copiar al portapapeles", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGo.setText(QtGui.QApplication.translate("Dialog", "Ir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGet.setText(QtGui.QApplication.translate("Dialog", "Empezar captura", None, QtGui.QApplication.UnicodeUTF8))
        self.radioutm.setText(QtGui.QApplication.translate("Dialog", "UTM", None, QtGui.QApplication.UnicodeUTF8))
        self.radiodms.setText(QtGui.QApplication.translate("Dialog", "Grad. Min. Seg.", None, QtGui.QApplication.UnicodeUTF8))
        self.radiodm.setText(QtGui.QApplication.translate("Dialog", "Grad. Min.", None, QtGui.QApplication.UnicodeUTF8))
        self.radiod.setText(QtGui.QApplication.translate("Dialog", "Grados", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Coordenadas", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDockWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


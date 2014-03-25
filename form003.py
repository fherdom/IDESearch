# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form003.ui'
#
# Created: Fri Jul  6 12:22:59 2012
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
        Dialog.resize(324, 311)
        Dialog.setFloating(True)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 321, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab001 = QtGui.QWidget()
        self.tab001.setObjectName(_fromUtf8("tab001"))
        self.gridLayout = QtGui.QGridLayout(self.tab001)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tblResult = QtGui.QTableWidget(self.tab001)
        self.tblResult.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblResult.sizePolicy().hasHeightForWidth())
        self.tblResult.setSizePolicy(sizePolicy)
        self.tblResult.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblResult.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblResult.setShowGrid(True)
        self.tblResult.setColumnCount(3)
        self.tblResult.setObjectName(_fromUtf8("tblResult"))
        self.tblResult.setRowCount(0)
        self.gridLayout.addWidget(self.tblResult, 1, 0, 1, 1)
        self.lblResult = QtGui.QLabel(self.tab001)
        self.lblResult.setObjectName(_fromUtf8("lblResult"))
        self.gridLayout.addWidget(self.lblResult, 2, 0, 1, 1)
        self.txtSearch = QtGui.QLineEdit(self.tab001)
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
        self.gridLayout.addWidget(self.txtSearch, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab001, _fromUtf8(""))
        self.tab002 = QtGui.QWidget()
        self.tab002.setObjectName(_fromUtf8("tab002"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab002)
        self.groupBox_7.setEnabled(True)
        self.groupBox_7.setGeometry(QtCore.QRect(5, 10, 311, 186))
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_7)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 226, 50))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radioutm = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioutm.setObjectName(_fromUtf8("radioutm"))
        self.gridLayout_3.addWidget(self.radioutm, 1, 0, 1, 1)
        self.radiodms = QtGui.QRadioButton(self.layoutWidget_2)
        self.radiodms.setChecked(True)
        self.radiodms.setObjectName(_fromUtf8("radiodms"))
        self.gridLayout_3.addWidget(self.radiodms, 0, 0, 1, 1)
        self.radiodm = QtGui.QRadioButton(self.layoutWidget_2)
        self.radiodm.setObjectName(_fromUtf8("radiodm"))
        self.gridLayout_3.addWidget(self.radiodm, 0, 1, 1, 1)
        self.radiod = QtGui.QRadioButton(self.layoutWidget_2)
        self.radiod.setObjectName(_fromUtf8("radiod"))
        self.gridLayout_3.addWidget(self.radiod, 1, 1, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.groupBox_7)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 55, 301, 127))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.txtCoordinates = QtGui.QLineEdit(self.layoutWidget)
        self.txtCoordinates.setObjectName(_fromUtf8("txtCoordinates"))
        self.gridLayout_2.addWidget(self.txtCoordinates, 0, 0, 1, 1)
        self.btnGet = QtGui.QPushButton(self.layoutWidget)
        self.btnGet.setObjectName(_fromUtf8("btnGet"))
        self.gridLayout_2.addWidget(self.btnGet, 3, 0, 1, 1)
        self.btnClipboard = QtGui.QPushButton(self.layoutWidget)
        self.btnClipboard.setObjectName(_fromUtf8("btnClipboard"))
        self.gridLayout_2.addWidget(self.btnClipboard, 2, 0, 1, 1)
        self.btnGo = QtGui.QPushButton(self.layoutWidget)
        self.btnGo.setObjectName(_fromUtf8("btnGo"))
        self.gridLayout_2.addWidget(self.btnGo, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab002, _fromUtf8(""))
        Dialog.setWidget(self.dockWidgetContents)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Búsquedas IDECanarias", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResult.setText(QtGui.QApplication.translate("Dialog", "Encontrado (s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab001), QtGui.QApplication.translate("Dialog", "Lugar", None, QtGui.QApplication.UnicodeUTF8))
        self.radioutm.setText(QtGui.QApplication.translate("Dialog", "UTM", None, QtGui.QApplication.UnicodeUTF8))
        self.radiodms.setText(QtGui.QApplication.translate("Dialog", "Grad. Min. Seg.", None, QtGui.QApplication.UnicodeUTF8))
        self.radiodm.setText(QtGui.QApplication.translate("Dialog", "Grad. Min.", None, QtGui.QApplication.UnicodeUTF8))
        self.radiod.setText(QtGui.QApplication.translate("Dialog", "Grados", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGet.setText(QtGui.QApplication.translate("Dialog", "Empezar captura", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClipboard.setText(QtGui.QApplication.translate("Dialog", "Copiar al portapapeles", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGo.setText(QtGui.QApplication.translate("Dialog", "Ir", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab002), QtGui.QApplication.translate("Dialog", "Coordenadas", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDockWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_nmea.ui'
#
# Created: Sun Jun 30 19:45:00 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_nmea(object):
    def setupUi(self, nmea):
        nmea.setObjectName(_fromUtf8("nmea"))
        nmea.resize(777, 686)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(nmea.sizePolicy().hasHeightForWidth())
        nmea.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(nmea)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(nmea)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.nmeaBrowser = QtGui.QTextBrowser(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nmeaBrowser.sizePolicy().hasHeightForWidth())
        self.nmeaBrowser.setSizePolicy(sizePolicy)
        self.nmeaBrowser.setMinimumSize(QtCore.QSize(650, 0))
        self.nmeaBrowser.setObjectName(_fromUtf8("nmeaBrowser"))
        self.horizontalLayout.addWidget(self.nmeaBrowser)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.addBut = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBut.sizePolicy().hasHeightForWidth())
        self.addBut.setSizePolicy(sizePolicy)
        self.addBut.setObjectName(_fromUtf8("addBut"))
        self.verticalLayout_3.addWidget(self.addBut)
        spacerItem = QtGui.QSpacerItem(30, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.senCom = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senCom.sizePolicy().hasHeightForWidth())
        self.senCom.setSizePolicy(sizePolicy)
        self.senCom.setObjectName(_fromUtf8("senCom"))
        self.verticalLayout_3.addWidget(self.senCom)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.matplot1 = mplc(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matplot1.sizePolicy().hasHeightForWidth())
        self.matplot1.setSizePolicy(sizePolicy)
        self.matplot1.setObjectName(_fromUtf8("matplot1"))
        self.horizontalLayout_3.addWidget(self.matplot1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mat1Combo = QtGui.QComboBox(self.tab_2)
        self.mat1Combo.setObjectName(_fromUtf8("mat1Combo"))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mat1Combo)
        self.mat2Combo = QtGui.QComboBox(self.tab_2)
        self.mat2Combo.setObjectName(_fromUtf8("mat2Combo"))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mat2Combo)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(nmea)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(nmea)

    def retranslateUi(self, nmea):
        nmea.setWindowTitle(_translate("nmea", "nmea_main", None))
        self.addBut.setText(_translate("nmea", "add layer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("nmea", "Tab 1", None))
        self.mat1Combo.setItemText(0, _translate("nmea", "numsv", None))
        self.mat1Combo.setItemText(1, _translate("nmea", "dop", None))
        self.mat1Combo.setItemText(2, _translate("nmea", "vdop", None))
        self.mat1Combo.setItemText(3, _translate("nmea", "pdop", None))
        self.mat1Combo.setItemText(4, _translate("nmea", "msl", None))
        self.mat1Combo.setItemText(5, _translate("nmea", "geoid", None))
        self.mat1Combo.setItemText(6, _translate("nmea", "speed", None))
        self.mat1Combo.setItemText(7, _translate("nmea", "fixstatus", None))
        self.mat2Combo.setItemText(0, _translate("nmea", "dop", None))
        self.mat2Combo.setItemText(1, _translate("nmea", "numsv", None))
        self.mat2Combo.setItemText(2, _translate("nmea", "vdop", None))
        self.mat2Combo.setItemText(3, _translate("nmea", "pdop", None))
        self.mat2Combo.setItemText(4, _translate("nmea", "msl", None))
        self.mat2Combo.setItemText(5, _translate("nmea", "geoid", None))
        self.mat2Combo.setItemText(6, _translate("nmea", "speed", None))
        self.mat2Combo.setItemText(7, _translate("nmea", "datastatus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("nmea", "Tab 2", None))

from graphs import mplc

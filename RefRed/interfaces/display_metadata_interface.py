# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//display_metadata_interface.ui'
#
# Created: Mon Oct 26 13:30:28 2015
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.searchLabel = QtGui.QLabel(self.centralwidget)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout_3.addWidget(self.searchLabel)
        self.searchLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_3.addWidget(self.searchLineEdit)
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setText("")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_3.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Metadata = QtGui.QWidget()
        self.Metadata.setObjectName("Metadata")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Metadata)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.metadataTable = QtGui.QTableWidget(self.Metadata)
        self.metadataTable.setObjectName("metadataTable")
        self.metadataTable.setColumnCount(3)
        self.metadataTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout_4.addWidget(self.metadataTable)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.saveMetadataAsAsciiButton = QtGui.QPushButton(self.Metadata)
        self.saveMetadataAsAsciiButton.setEnabled(False)
        self.saveMetadataAsAsciiButton.setObjectName("saveMetadataAsAsciiButton")
        self.horizontalLayout_2.addWidget(self.saveMetadataAsAsciiButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.Metadata, "")
        self.Configure = QtGui.QWidget()
        self.Configure.setObjectName("Configure")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Configure)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.configureTable = QtGui.QTableWidget(self.Configure)
        self.configureTable.setAlternatingRowColors(True)
        self.configureTable.setObjectName("configureTable")
        self.configureTable.setColumnCount(4)
        self.configureTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.configureTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.configureTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.configureTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.configureTable.setHorizontalHeaderItem(3, item)
        self.configureTable.horizontalHeader().setSortIndicatorShown(False)
        self.configureTable.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_5.addWidget(self.configureTable)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.unselectAllButton = QtGui.QPushButton(self.Configure)
        self.unselectAllButton.setObjectName("unselectAllButton")
        self.horizontalLayout.addWidget(self.unselectAllButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.exportConfigurationButton = QtGui.QPushButton(self.Configure)
        self.exportConfigurationButton.setObjectName("exportConfigurationButton")
        self.horizontalLayout.addWidget(self.exportConfigurationButton)
        self.importConfigurationButton = QtGui.QPushButton(self.Configure)
        self.importConfigurationButton.setObjectName("importConfigurationButton")
        self.horizontalLayout.addWidget(self.importConfigurationButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.Configure, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), MainWindow.userChangedTab)
        QtCore.QObject.connect(self.saveMetadataAsAsciiButton, QtCore.SIGNAL("clicked()"), MainWindow.saveMetadataListAsAscii)
        QtCore.QObject.connect(self.exportConfigurationButton, QtCore.SIGNAL("clicked()"), MainWindow.exportConfiguration)
        QtCore.QObject.connect(self.importConfigurationButton, QtCore.SIGNAL("clicked()"), MainWindow.importConfiguration)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), MainWindow.clearSearchLineEdit)
        QtCore.QObject.connect(self.unselectAllButton, QtCore.SIGNAL("clicked()"), MainWindow.unselectAll)
        QtCore.QObject.connect(self.searchLineEdit, QtCore.SIGNAL("textEdited(QString)"), MainWindow.liveEditSearchLineEdit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.searchLabel.setText(QtGui.QApplication.translate("MainWindow", "loop", None, QtGui.QApplication.UnicodeUTF8))
        self.metadataTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.metadataTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.metadataTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Units", None, QtGui.QApplication.UnicodeUTF8))
        self.saveMetadataAsAsciiButton.setText(QtGui.QApplication.translate("MainWindow", "Save List of Metadata as ASCII ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Metadata), QtGui.QApplication.translate("MainWindow", "Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Display ?", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Units", None, QtGui.QApplication.UnicodeUTF8))
        self.unselectAllButton.setText(QtGui.QApplication.translate("MainWindow", "Unselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.exportConfigurationButton.setText(QtGui.QApplication.translate("MainWindow", "Export Configuration ...", None, QtGui.QApplication.UnicodeUTF8))
        self.importConfigurationButton.setText(QtGui.QApplication.translate("MainWindow", "Import Configuration ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Configure), QtGui.QApplication.translate("MainWindow", "Configure", None, QtGui.QApplication.UnicodeUTF8))


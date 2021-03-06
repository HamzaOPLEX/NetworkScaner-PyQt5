from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from scapy.all import *

import icons_rc
from PyQt5.QtWidgets import (QFileDialog, QLabel, QMainWindow, QMessageBox,QSizePolicy, QTableWidget, QTableWidgetItem)
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 660)
        MainWindow.setMinimumSize(QtCore.QSize(648, 660))
        MainWindow.setMaximumSize(QtCore.QSize(648, 660))
        MainWindow.setAutoFillBackground(False)
        THEMEFILE = open('themes/style.css').read()
        MainWindow.setStyleSheet(THEMEFILE)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Ping_tab = QtWidgets.QWidget()
        self.Ping_tab.setObjectName("Ping_tab")
        self.StartButtn = QtWidgets.QPushButton(self.Ping_tab)
        self.StartButtn.setGeometry(QtCore.QRect(11, 9, 91, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartButtn.setIcon(icon)
        self.StartButtn.setIconSize(QtCore.QSize(30, 30))
        self.StartButtn.setCheckable(False)
        self.StartButtn.setAutoDefault(False)
        self.StartButtn.setDefault(False)
        self.StartButtn.setFlat(False)
        self.StartButtn.setObjectName("StartButtn")
        self.StatusTable = QtWidgets.QTableWidget(self.Ping_tab)
        self.StatusTable.setGeometry(QtCore.QRect(10, 100, 591, 411))
        self.StatusTable.setObjectName("StatusTable")
        self.StatusTable.setColumnCount(4)
        self.StatusTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable.setHorizontalHeaderItem(3, item)
        self.PauseButtn = QtWidgets.QPushButton(self.Ping_tab)
        self.PauseButtn.setEnabled(True)
        self.PauseButtn.setGeometry(QtCore.QRect(111, 9, 88, 41))
        self.PauseButtn.setStyleSheet("")
        self.PauseButtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PauseButtn.setIcon(icon1)
        self.PauseButtn.setIconSize(QtCore.QSize(30, 30))
        self.PauseButtn.setCheckable(False)
        self.PauseButtn.setChecked(False)
        self.PauseButtn.setFlat(True)
        self.PauseButtn.setObjectName("PauseButtn")
        self.progressBar = QtWidgets.QProgressBar(self.Ping_tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 60, 591, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.SaveExcelButtn = QtWidgets.QPushButton(self.Ping_tab)
        self.SaveExcelButtn.setGeometry(QtCore.QRect(260, 520, 88, 61))
        self.SaveExcelButtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveExcelButtn.setIcon(icon2)
        self.SaveExcelButtn.setIconSize(QtCore.QSize(45, 45))
        self.SaveExcelButtn.setObjectName("SaveExcelButtn")
        self.SelectGroupPing = QtWidgets.QComboBox(self.Ping_tab)
        self.SelectGroupPing.setGeometry(QtCore.QRect(320, 20, 281, 31))
        self.SelectGroupPing.setObjectName("SelectGroupPing")
        self.SelectGroupPing.addItem("")
        self.label_5 = QtWidgets.QLabel(self.Ping_tab)
        self.label_5.setGeometry(QtCore.QRect(320, 0, 271, 20))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.Ping_tab, "")
        self.config_tab = QtWidgets.QWidget()
        self.config_tab.setObjectName("config_tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.config_tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 621, 581))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Areas_Config = QtWidgets.QWidget()
        self.Areas_Config.setObjectName("Areas_Config")
        self.pushButton = QtWidgets.QPushButton(self.Areas_Config)
        self.pushButton.setGeometry(QtCore.QRect(480, 60, 131, 41))
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Areas_Config)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 110, 131, 41))
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Areas_Config)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 461, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.Areas_Config)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 60, 461, 481))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.setColumnHidden(0,True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.tableWidget_4.setColumnHidden(0,True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.EditHost_3 = QtWidgets.QPushButton(self.Areas_Config)
        self.EditHost_3.setGeometry(QtCore.QRect(480, 160, 131, 41))
        self.EditHost_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EditHost_3.setIcon(icon5)
        self.EditHost_3.setIconSize(QtCore.QSize(35, 35))
        self.EditHost_3.setObjectName("EditHost_3")
        self.tabWidget_2.addTab(self.Areas_Config, "")
        self.Groups_config = QtWidgets.QWidget()
        self.Groups_config.setObjectName("Groups_config")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Groups_config)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 331, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.Groups_config)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 60, 131, 41))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.Groups_config)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 110, 131, 41))
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.EditHost_2 = QtWidgets.QPushButton(self.Groups_config)
        self.EditHost_2.setGeometry(QtCore.QRect(480, 160, 131, 41))
        self.EditHost_2.setText("")
        self.EditHost_2.setIcon(icon5)
        self.EditHost_2.setIconSize(QtCore.QSize(35, 35))
        self.EditHost_2.setObjectName("EditHost_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.Groups_config)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 60, 461, 481))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.tableWidget_3.setColumnHidden(0,True)
        self.AreaCombo_2 = QtWidgets.QComboBox(self.Groups_config)
        self.AreaCombo_2.setGeometry(QtCore.QRect(350, 20, 121, 31))
        self.AreaCombo_2.setObjectName("AreaCombo_2")
        self.label_6 = QtWidgets.QLabel(self.Groups_config)
        self.label_6.setGeometry(QtCore.QRect(350, 0, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Groups_config)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 121, 16))
        self.label_7.setObjectName("label_7")
        self.tabWidget_2.addTab(self.Groups_config, "")
        self.Hosts_Config = QtWidgets.QWidget()
        self.Hosts_Config.setObjectName("Hosts_Config")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Hosts_Config)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 80, 461, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnHidden(0,True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.hostname = QtWidgets.QLineEdit(self.Hosts_Config)
        self.hostname.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.hostname.setObjectName("hostname")
        self.ipaddr = QtWidgets.QLineEdit(self.Hosts_Config)
        self.ipaddr.setGeometry(QtCore.QRect(180, 30, 161, 31))
        self.ipaddr.setObjectName("ipaddr")
        self.GroupCombo = QtWidgets.QComboBox(self.Hosts_Config)
        self.GroupCombo.setGeometry(QtCore.QRect(350, 30, 121, 31))
        self.GroupCombo.setObjectName("GroupCombo")
        self.label = QtWidgets.QLabel(self.Hosts_Config)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Hosts_Config)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Hosts_Config)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Hosts_Config)
        self.label_4.setGeometry(QtCore.QRect(480, 10, 121, 16))
        self.label_4.setObjectName("label_4")
        self.RemoveHost = QtWidgets.QPushButton(self.Hosts_Config)
        self.RemoveHost.setGeometry(QtCore.QRect(480, 130, 131, 41))
        self.RemoveHost.setText("")
        self.RemoveHost.setIcon(icon4)
        self.RemoveHost.setIconSize(QtCore.QSize(30, 30))
        self.RemoveHost.setObjectName("RemoveHost")
        self.AddHost = QtWidgets.QPushButton(self.Hosts_Config)
        self.AddHost.setGeometry(QtCore.QRect(480, 80, 131, 41))
        self.AddHost.setText("")
        self.AddHost.setIcon(icon3)
        self.AddHost.setIconSize(QtCore.QSize(30, 30))
        self.AddHost.setObjectName("AddHost")
        self.EditHost = QtWidgets.QPushButton(self.Hosts_Config)
        self.EditHost.setGeometry(QtCore.QRect(480, 180, 131, 41))
        self.EditHost.setText("")
        self.EditHost.setIcon(icon5)
        self.EditHost.setIconSize(QtCore.QSize(35, 35))
        self.EditHost.setObjectName("EditHost")
        self.tabWidget_2.addTab(self.Hosts_Config, "")
        self.tabWidget.addTab(self.config_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 30))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionContact_us = QtWidgets.QAction(MainWindow)
        self.actionContact_us.setObjectName("actionContact_us")
        self.actionLight_Theme = QtWidgets.QAction(MainWindow)
        self.actionLight_Theme.setObjectName("actionLight_Theme")
        self.actionDark_Theme = QtWidgets.QAction(MainWindow)
        self.actionDark_Theme.setObjectName("actionDark_Theme")
        self.actionSCAN_shift_s = QtWidgets.QAction(MainWindow)
        self.actionSCAN_shift_s.setObjectName("actionSCAN_shift_s")
        self.actionSTOP_shift_p = QtWidgets.QAction(MainWindow)
        self.actionSTOP_shift_p.setObjectName("actionSTOP_shift_p")
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionNew_File)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_Us)
        self.menuAbout.addAction(self.actionContact_us)
        self.menuEdit.addAction(self.actionLight_Theme)
        self.menuEdit.addAction(self.actionDark_Theme)
        self.menuRun.addAction(self.actionSCAN_shift_s)
        self.menuRun.addAction(self.actionSTOP_shift_p)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(2)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionSTOP_shift_p.triggered.connect(self.PauseButtn.animateClick)
        self.actionSCAN_shift_s.triggered.connect(self.StartButtn.animateClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Oplex Pinger - By HamzaOPLEX "))
        self.StartButtn.setText(_translate("MainWindow", "START"))
        self.StartButtn.setShortcut(_translate("MainWindow", "Shift+S"))
        item = self.StatusTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Area"))
        item = self.StatusTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Group"))
        item = self.StatusTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP"))
        item = self.StatusTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.PauseButtn.setShortcut(_translate("MainWindow", "Shift+P"))
        self.SelectGroupPing.setItemText(0, _translate("MainWindow", "*"))
        self.label_5.setText(_translate("MainWindow", "Select Group To Ping :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ping_tab), _translate("MainWindow", "Pinger"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the area name here"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Area Name"))        
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Areas_Config), _translate("MainWindow", "Areas Config"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter the group name here"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Group Name"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "belong to area"))
        self.label_6.setText(_translate("MainWindow", "AREA"))
        self.label_7.setText(_translate("MainWindow", "Group Name : "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Groups_config), _translate("MainWindow", "Groups Config"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "hostname"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ip address"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "belong to group"))
        self.label.setText(_translate("MainWindow", "HOSTNAME"))
        self.label_2.setText(_translate("MainWindow", "IP ADDRESS"))
        self.label_3.setText(_translate("MainWindow", "GROUP"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Hosts_Config), _translate("MainWindow", "Hosts Config"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config_tab), _translate("MainWindow", "Configuration"))
        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About us"))
        self.actionContact_us.setText(_translate("MainWindow", "Contact us"))
        self.actionLight_Theme.setText(_translate("MainWindow", "Light Theme"))
        self.actionDark_Theme.setText(_translate("MainWindow", "Dark Theme"))
        self.actionSCAN_shift_s.setText(_translate("MainWindow", "SCAN              shift+s"))
        self.actionSTOP_shift_p.setText(_translate("MainWindow", "STOP               shift+p"))
        self.StartButtn.clicked.connect(self.PingHandler)

        self.pushButton.clicked.connect(partial(self.AreaHandler,'add'))
        self.pushButton_4.clicked.connect(partial(self.GroupsHandler,'add'))
        self.AddHost.clicked.connect(partial(self.HostHandler,'add'))
        self.ConnectToDb()
        self.PrepareData()
        self.pushButton_2.clicked.connect(partial(self.AreaHandler,'delete'))
        self.pushButton_6.clicked.connect(partial(self.GroupsHandler,'delete'))
        self.RemoveHost.clicked.connect(partial(self.HostHandler,'delete'))
        self.clicked_buttn = ''
        self.tableWidget_4.itemChanged.connect(partial(self.getEditedItems,self.tableWidget_4,"areas","area_name"))

    def MessageHandler(self, type, title, showmsg):
        def msgbtn(i):
            self.clicked_buttn =  i.text()
        msg = QMessageBox()
        if type == 'Err':
            msg.setWindowTitle(title)
            msg.setText(showmsg)
            msg.setIcon(QMessageBox.Critical)
            return msg
        elif type == 'Info':
            msg.setWindowTitle(title)
            msg.setText(showmsg)
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.buttonClicked.connect(msgbtn)
            return msg

    def getEditedItems(self,tableobj,dbtable,colomn,items):
        try :
            try : 
                ID =  tableobj.item(items.row(),0).text()
                NEW_DATA =   tableobj.item(items.row(),1).text()
                self.cur.execute(f'UPDATE {dbtable} SET {colomn} = "{NEW_DATA}" WHERE id="{ID}"')
                self.database_connection.commit()
                self.PrepareData(tableprepare=False)
            except sqlite3.IntegrityError:
                    msg = self.MessageHandler('Err', 'inpute not uniq', 'Area name must be uniq')
                    msg.exec_()
                    tableobj.setRowCount(0)
                    self.PrepareData()
        except AttributeError: 
            pass

    def ConnectToDb(self):
        self.database_connection = sqlite3.connect('Database_Config/config.db')
        self.cur = self.database_connection.cursor()
        
    def PrepareData(self,tableprepare=True):
        areas = list(self.cur.execute(f'SELECT * FROM areas'))
        groups =  list(self.cur.execute(f'SELECT * FROM groups'))
        hosts = list(self.cur.execute(f'SELECT * FROM hosts'))

        # fill all comboboxes with data
        self.GroupCombo.clear()
        self.GroupCombo.addItems([f'{i[0]}-{i[1]}' for i in groups])
        self.AreaCombo_2.clear()
        self.AreaCombo_2.addItems([f'{i[0]}-{i[1]}' for i in areas])
        self.SelectGroupPing.clear()
        self.SelectGroupPing.addItems([f'{i[0]}-{i[1]}' for i in groups])
        if tableprepare : 
            if areas:
                self.InsertData2Table(areas,self.tableWidget_4)
            if groups:
                self.InsertData2Table(groups,self.tableWidget_3)
            if hosts:
                self.InsertData2Table(hosts,self.tableWidget_2)

    def InsertData2Table(self,data,table):
        # get one row length
        table.setRowCount(0)
        row_lenght = len(data[0])
        for d in data :
            currentRowCount = table.rowCount()
            table.insertRow(currentRowCount)
            for index in range(row_lenght):
                table.setItem(currentRowCount,index , QTableWidgetItem(str(d[index])))

    def getNewId(self,TableName):
        ids = list(self.cur.execute(f'SELECT id FROM {TableName}'))
        ids = [i[0] for i in ids]
        n = 1
        while n in ids:
            n = n + 1
        return n

    def RemoveSelectedRows(self,table,id_colomn,db_table_name):
            SelectedRows = table.selectedItems()
            if SelectedRows : 
                for i in SelectedRows :
                    try : 
                        ID = table.item(i.row(), 0).text()
                        DeleteQuery = f"DELETE FROM {db_table_name} WHERE id={ID};"
                        self.cur.execute(DeleteQuery)
                        self.database_connection.commit()
                    except Exception as err:
                        print(err)
                table.setRowCount(0)
                self.PrepareData()

    ########### Area Handler ###################
    def AreaHandler(self,action):
        areaname = self.lineEdit.text()
        if action == 'add':
            if areaname:
                ID = self.getNewId('areas')
                try : 
                    self.cur.execute(f'INSERT INTO areas VALUES({ID},"{areaname}")')
                    self.database_connection.commit()
                    self.PrepareData()
                    self.lineEdit.clear()
                except sqlite3.IntegrityError:
                    msg = self.MessageHandler('Err', 'inpute not uniq', 'Area name must be uniq')
                    msg.exec_()            
            elif not areaname:
                msg = self.MessageHandler('Err', 'inpute require', 'Area name: field require')
                msg.exec_()
        elif action == 'delete':
            MSG_header = 'all groups and hosts that belong to this area will be deleted'
            MSG_tail = 'Are You Sure To Delete This Areas ?'
            msg = self.MessageHandler('Info', MSG_tail, MSG_header)
            msg.exec_()
            if self.clicked_buttn != 'Cancel':
                self.RemoveSelectedRows(self.tableWidget_4,0,'areas')

    def GroupsHandler(self,action):
        groupname = self.lineEdit_2.text()
        area = str(self.AreaCombo_2.currentText()).split('-')[0]
        if action == 'add':
            if groupname:
                if area :
                    ID = self.getNewId('groups')
                    try : 
                        self.cur.execute(f'INSERT INTO groups VALUES({ID},"{groupname}","{area}")')
                        self.database_connection.commit()
                        self.PrepareData()
                        self.lineEdit_2.clear()
                    except sqlite3.IntegrityError:
                        msg = self.MessageHandler('Err', 'inpute not uniq', 'Group name must be uniq')
                        msg.exec_()
                elif not area :
                    msg = self.MessageHandler('Err', 'area require', 'please add at least one area')
                    msg.exec_()
            elif not groupname:
                msg = self.MessageHandler('Err', 'inpute require', 'Group name: field require')
                msg.exec_()
        elif action == 'delete':
            MSG_header = 'allhosts that belong to this group will be deleted'
            MSG_tail = 'Are You Sure To Delete This Group ?'
            msg = self.MessageHandler('Info', MSG_tail, MSG_header)
            msg.exec_()
            if self.clicked_buttn != 'Cancel':
                self.RemoveSelectedRows(self.tableWidget_3,0,'groups')

    def HostHandler(self,action):
        hostname = self.hostname.text()
        ip = self.ipaddr.text()
        group = str(self.GroupCombo.currentText()).split('-')[0]
        if action == 'add':
            if hostname and ip and group:
                if group :
                    ID = self.getNewId('hosts')
                    try : 
                        self.cur.execute(f'INSERT INTO hosts VALUES({ID},"{hostname}","{ip}","{group}")')
                        self.database_connection.commit()
                        self.PrepareData()
                        self.hostname.clear()
                        self.ipaddr.clear()
                    except sqlite3.IntegrityError:
                        msg = self.MessageHandler('Err', 'inpute not uniq', 'host must be uniq')
                        msg.exec_()
                elif not group :
                    msg = self.MessageHandler('Err', 'group require', 'please add at least one host')
                    msg.exec_()
            elif not groupname:
                msg = self.MessageHandler('Err', 'inpute require', 'Group name: field require')
                msg.exec_()
        elif action == 'delete':
            MSG_header = 'Are You Sure To Delete This hosts ?'
            MSG_tail = 'Yes Or No ?'
            msg = self.MessageHandler('Info', MSG_tail, MSG_header)
            msg.exec_()
            if self.clicked_buttn != 'Cancel':
                self.RemoveSelectedRows(self.tableWidget_2,0,'hosts')

    def PingHandler(self):
        group_id = str(self.SelectGroupPing.currentText()).split('-')[0]
        query = f'SELECT ip FROM hosts WHERE hgroup={group_id}'
        ips = self.cur.execute(query)
        self.database_connection.commit()
        TABLE_OUTPUT_DATA = []
        for ip in ips:
            ip = ip[0]
            area = 'ip[1]'
            group = 'ip[2]'
            icmp = IP(dst=ip)/ICMP()
            resp = sr1(icmp,timeout=2)
            if resp == None:
                TABLE_OUTPUT_DATA.append({
                            'ip':ip,
                            'status':'DOWN',
                            'area':area,
                            'group':group
                            })
            else:
                TABLE_OUTPUT_DATA.append({
                            'ip':ip,
                            'status':'UP',
                            'area':area,
                            'group':group
                            })
        self.StatusTable.setRowCount(0)
        row_lenght = len(TABLE_OUTPUT_DATA)
        for row in TABLE_OUTPUT_DATA:
            currentRowCount = self.StatusTable.rowCount()
            self.StatusTable.insertRow(currentRowCount)
            for clmn in row.keys():
                self.StatusTable.setItem(currentRowCount,list(row.keys()).index(clmn) , QTableWidgetItem(str(row[clmn])))



































if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
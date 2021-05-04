from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 660)
        MainWindow.setMinimumSize(QtCore.QSize(648, 660))
        MainWindow.setMaximumSize(QtCore.QSize(648, 660))
        MainWindow.setAutoFillBackground(False)
        theme = open('themes/style.css')
        MainWindow.setStyleSheet(theme.read())
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
        self.ScanButtonIPscanner = QtWidgets.QPushButton(self.Ping_tab)
        self.ScanButtonIPscanner.setGeometry(QtCore.QRect(11, 9, 91, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ScanButtonIPscanner.setIcon(icon)
        self.ScanButtonIPscanner.setIconSize(QtCore.QSize(30, 30))
        self.ScanButtonIPscanner.setCheckable(False)
        self.ScanButtonIPscanner.setAutoDefault(False)
        self.ScanButtonIPscanner.setDefault(False)
        self.ScanButtonIPscanner.setFlat(False)
        self.ScanButtonIPscanner.setObjectName("ScanButtonIPscanner")
        self.tableWidget = QtWidgets.QTableWidget(self.Ping_tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 591, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.PauseBottonIPscanner = QtWidgets.QPushButton(self.Ping_tab)
        self.PauseBottonIPscanner.setEnabled(True)
        self.PauseBottonIPscanner.setGeometry(QtCore.QRect(111, 9, 88, 41))
        self.PauseBottonIPscanner.setStyleSheet("")
        self.PauseBottonIPscanner.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PauseBottonIPscanner.setIcon(icon1)
        self.PauseBottonIPscanner.setIconSize(QtCore.QSize(30, 30))
        self.PauseBottonIPscanner.setCheckable(False)
        self.PauseBottonIPscanner.setChecked(False)
        self.PauseBottonIPscanner.setFlat(True)
        self.PauseBottonIPscanner.setObjectName("PauseBottonIPscanner")
        self.progressBar = QtWidgets.QProgressBar(self.Ping_tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 60, 591, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_11 = QtWidgets.QPushButton(self.Ping_tab)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 550, 181, 21))
        self.pushButton_11.setObjectName("pushButton_11")
        self.comboBox = QtWidgets.QComboBox(self.Ping_tab)
        self.comboBox.setGeometry(QtCore.QRect(320, 10, 281, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabWidget.addTab(self.Ping_tab, "")
        self.config_tab = QtWidgets.QWidget()
        self.config_tab.setObjectName("config_tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.config_tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 621, 581))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Areas_Config = QtWidgets.QWidget()
        self.Areas_Config.setObjectName("Areas_Config")
        self.listWidget = QtWidgets.QListWidget(self.Areas_Config)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 461, 481))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.Areas_Config)
        self.pushButton.setGeometry(QtCore.QRect(480, 60, 131, 41))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Areas_Config)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 110, 131, 41))
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Areas_Config)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 160, 131, 41))
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.Areas_Config)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 461, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget_2.addTab(self.Areas_Config, "")
        self.Groups_config = QtWidgets.QWidget()
        self.Groups_config.setObjectName("Groups_config")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Groups_config)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 10, 461, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.Groups_config)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 60, 461, 481))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.Groups_config)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 60, 131, 41))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Groups_config)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 160, 131, 41))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Groups_config)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 110, 131, 41))
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget_2.addTab(self.Groups_config, "")
        self.Hosts_Config = QtWidgets.QWidget()
        self.Hosts_Config.setObjectName("Hosts_Config")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Hosts_Config)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 80, 461, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Hosts_Config)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Hosts_Config)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 30, 161, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.Hosts_Config)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 30, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.Hosts_Config)
        self.comboBox_3.setGeometry(QtCore.QRect(480, 30, 131, 31))
        self.comboBox_3.setObjectName("comboBox_3")
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
        self.pushButton_7 = QtWidgets.QPushButton(self.Hosts_Config)
        self.pushButton_7.setGeometry(QtCore.QRect(480, 130, 131, 41))
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.Hosts_Config)
        self.pushButton_8.setGeometry(QtCore.QRect(480, 80, 131, 41))
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.Hosts_Config)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 180, 131, 41))
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
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
        self.actionSTOP_shift_p.triggered.connect(self.PauseBottonIPscanner.animateClick)
        self.actionSCAN_shift_s.triggered.connect(self.ScanButtonIPscanner.animateClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ScanButtonIPscanner.setText(_translate("MainWindow", "START"))
        self.ScanButtonIPscanner.setShortcut(_translate("MainWindow", "Shift+S"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Area"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Group"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.PauseBottonIPscanner.setShortcut(_translate("MainWindow", "Shift+P"))
        self.pushButton_11.setText(_translate("MainWindow", "SAVE AS EXCEL FILE"))
        self.comboBox.setItemText(0, _translate("MainWindow", "*"))
        self.comboBox.setItemText(1, _translate("MainWindow", "GROUP NAME 01"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GROUP NAME 02"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ping_tab), _translate("MainWindow", "Pinger"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the area name here"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Areas_Config), _translate("MainWindow", "Areas Config"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter the group name here"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Groups_config), _translate("MainWindow", "Groups Config"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "hostname"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ip address"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "belong to area"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "belong to group"))
        self.label.setText(_translate("MainWindow", "HOSTNAME"))
        self.label_2.setText(_translate("MainWindow", "IP ADDRESS$"))
        self.label_3.setText(_translate("MainWindow", "AREA"))
        self.label_4.setText(_translate("MainWindow", "GROUP"))
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




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
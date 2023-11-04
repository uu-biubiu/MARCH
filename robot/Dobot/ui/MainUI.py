# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2159, 1346)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Robot_label = QtWidgets.QLabel(self.centralwidget)
        self.Robot_label.setGeometry(QtCore.QRect(50, 450, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Robot_label.setFont(font)
        self.Robot_label.setObjectName("Robot_label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-20, 410, 2021, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Init_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Init_pushButton.setGeometry(QtCore.QRect(100, 90, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Init_pushButton.setFont(font)
        self.Init_pushButton.setObjectName("Init_pushButton")
        self.velocityRatio_label = QtWidgets.QLabel(self.centralwidget)
        self.velocityRatio_label.setGeometry(QtCore.QRect(60, 220, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.velocityRatio_label.setFont(font)
        self.velocityRatio_label.setObjectName("velocityRatio_label")
        self.accelerationRatio_label = QtWidgets.QLabel(self.centralwidget)
        self.accelerationRatio_label.setGeometry(QtCore.QRect(30, 260, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.accelerationRatio_label.setFont(font)
        self.accelerationRatio_label.setObjectName("accelerationRatio_label")
        self.v_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.v_horizontalSlider.setGeometry(QtCore.QRect(160, 220, 141, 21))
        self.v_horizontalSlider.setMinimum(1)
        self.v_horizontalSlider.setMaximum(100)
        self.v_horizontalSlider.setProperty("value", 5)
        self.v_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.v_horizontalSlider.setObjectName("v_horizontalSlider")
        self.a_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.a_horizontalSlider.setGeometry(QtCore.QRect(160, 270, 141, 21))
        self.a_horizontalSlider.setMinimum(1)
        self.a_horizontalSlider.setMaximum(100)
        self.a_horizontalSlider.setProperty("value", 5)
        self.a_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.a_horizontalSlider.setObjectName("a_horizontalSlider")
        self.setVelocity_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.setVelocity_pushButton.setGeometry(QtCore.QRect(430, 230, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.setVelocity_pushButton.setFont(font)
        self.setVelocity_pushButton.setObjectName("setVelocity_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pushButton.setGeometry(QtCore.QRect(1510, 490, 70, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.stop_pushButton.setFont(font)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.Pressure_label = QtWidgets.QLabel(self.centralwidget)
        self.Pressure_label.setGeometry(QtCore.QRect(260, 460, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Pressure_label.setFont(font)
        self.Pressure_label.setObjectName("Pressure_label")
        self.pressure_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pressure_label_2.setGeometry(QtCore.QRect(200, 510, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pressure_label_2.setFont(font)
        self.pressure_label_2.setObjectName("pressure_label_2")
        self.pressure_unit = QtWidgets.QLabel(self.centralwidget)
        self.pressure_unit.setGeometry(QtCore.QRect(370, 520, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pressure_unit.setFont(font)
        self.pressure_unit.setObjectName("pressure_unit")
        self.Valve_label = QtWidgets.QLabel(self.centralwidget)
        self.Valve_label.setGeometry(QtCore.QRect(510, 450, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Valve_label.setFont(font)
        self.Valve_label.setObjectName("Valve_label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 500, 111, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.xPoint_lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.xPoint_lineEdit_2.setObjectName("xPoint_lineEdit_2")
        self.verticalLayout_2.addWidget(self.xPoint_lineEdit_2)
        self.yPoint_lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.yPoint_lineEdit_2.setObjectName("yPoint_lineEdit_2")
        self.verticalLayout_2.addWidget(self.yPoint_lineEdit_2)
        self.zPoint_lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.zPoint_lineEdit_2.setObjectName("zPoint_lineEdit_2")
        self.verticalLayout_2.addWidget(self.zPoint_lineEdit_2)
        self.rAngle_lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.rAngle_lineEdit_2.setObjectName("rAngle_lineEdit_2")
        self.verticalLayout_2.addWidget(self.rAngle_lineEdit_2)
        self.v_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.v_lineEdit.setEnabled(False)
        self.v_lineEdit.setGeometry(QtCore.QRect(320, 230, 41, 21))
        self.v_lineEdit.setReadOnly(False)
        self.v_lineEdit.setObjectName("v_lineEdit")
        self.a_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.a_lineEdit.setEnabled(False)
        self.a_lineEdit.setGeometry(QtCore.QRect(320, 270, 41, 21))
        self.a_lineEdit.setReadOnly(False)
        self.a_lineEdit.setObjectName("a_lineEdit")
        self.v_label = QtWidgets.QLabel(self.centralwidget)
        self.v_label.setGeometry(QtCore.QRect(370, 230, 21, 21))
        self.v_label.setObjectName("v_label")
        self.a_label = QtWidgets.QLabel(self.centralwidget)
        self.a_label.setGeometry(QtCore.QRect(370, 270, 21, 21))
        self.a_label.setObjectName("a_label")
        self.airpressure_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.airpressure_lineEdit.setGeometry(QtCore.QRect(1390, 80, 51, 41))
        self.airpressure_lineEdit.setObjectName("airpressure_lineEdit")
        self.pulseTime_label = QtWidgets.QLabel(self.centralwidget)
        self.pulseTime_label.setGeometry(QtCore.QRect(440, 520, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pulseTime_label.setFont(font)
        self.pulseTime_label.setObjectName("pulseTime_label")
        self.pulseTime_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pulseTime_lineEdit.setGeometry(QtCore.QRect(540, 510, 61, 41))
        self.pulseTime_lineEdit.setObjectName("pulseTime_lineEdit")
        self.pulseTime_unit = QtWidgets.QLabel(self.centralwidget)
        self.pulseTime_unit.setGeometry(QtCore.QRect(610, 520, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pulseTime_unit.setFont(font)
        self.pulseTime_unit.setObjectName("pulseTime_unit")
        self.xAdd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.xAdd_pushButton.setGeometry(QtCore.QRect(730, 210, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.xAdd_pushButton.setFont(font)
        self.xAdd_pushButton.setObjectName("xAdd_pushButton")
        self.xReduce_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.xReduce_pushButton.setGeometry(QtCore.QRect(730, 330, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.xReduce_pushButton.setFont(font)
        self.xReduce_pushButton.setObjectName("xReduce_pushButton")
        self.yAdd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.yAdd_pushButton.setGeometry(QtCore.QRect(790, 270, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.yAdd_pushButton.setFont(font)
        self.yAdd_pushButton.setObjectName("yAdd_pushButton")
        self.yReduce_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.yReduce_pushButton.setGeometry(QtCore.QRect(670, 270, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.yReduce_pushButton.setFont(font)
        self.yReduce_pushButton.setObjectName("yReduce_pushButton")
        self.rReduce_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rReduce_pushButton.setGeometry(QtCore.QRect(930, 260, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.rReduce_pushButton.setFont(font)
        self.rReduce_pushButton.setObjectName("rReduce_pushButton")
        self.zAdd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.zAdd_pushButton.setGeometry(QtCore.QRect(990, 200, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.zAdd_pushButton.setFont(font)
        self.zAdd_pushButton.setObjectName("zAdd_pushButton")
        self.rAdd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rAdd_pushButton.setGeometry(QtCore.QRect(1050, 260, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.rAdd_pushButton.setFont(font)
        self.rAdd_pushButton.setObjectName("rAdd_pushButton")
        self.zReduce_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.zReduce_pushButton.setGeometry(QtCore.QRect(990, 320, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.zReduce_pushButton.setFont(font)
        self.zReduce_pushButton.setObjectName("zReduce_pushButton")
        self.space_label = QtWidgets.QLabel(self.centralwidget)
        self.space_label.setGeometry(QtCore.QRect(650, 80, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.space_label.setFont(font)
        self.space_label.setObjectName("space_label")
        self.space_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.space_lineEdit.setGeometry(QtCore.QRect(730, 90, 51, 31))
        self.space_lineEdit.setObjectName("space_lineEdit")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 500, 51, 231))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.x_label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.x_label_2.setFont(font)
        self.x_label_2.setObjectName("x_label_2")
        self.verticalLayout_3.addWidget(self.x_label_2)
        self.y_label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.y_label_2.setFont(font)
        self.y_label_2.setObjectName("y_label_2")
        self.verticalLayout_3.addWidget(self.y_label_2)
        self.z_label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.z_label_2.setFont(font)
        self.z_label_2.setObjectName("z_label_2")
        self.verticalLayout_3.addWidget(self.z_label_2)
        self.r_label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.r_label_2.setFont(font)
        self.r_label_2.setObjectName("r_label_2")
        self.verticalLayout_3.addWidget(self.r_label_2)
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushButton.setGeometry(QtCore.QRect(70, 790, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setObjectName("add_pushButton")
        self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pushButton.setGeometry(QtCore.QRect(500, 790, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.insert_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.insert_pushButton.setGeometry(QtCore.QRect(280, 790, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.insert_pushButton.setFont(font)
        self.insert_pushButton.setObjectName("insert_pushButton")
        self.run_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.run_pushButton.setGeometry(QtCore.QRect(1090, 490, 70, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.run_pushButton.setFont(font)
        self.run_pushButton.setObjectName("run_pushButton")
        self.pause_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pause_pushButton.setGeometry(QtCore.QRect(1300, 490, 70, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pause_pushButton.setFont(font)
        self.pause_pushButton.setObjectName("pause_pushButton")
        self.grab_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.grab_radioButton.setGeometry(QtCore.QRect(680, 530, 81, 16))
        self.grab_radioButton.setChecked(True)
        self.grab_radioButton.setObjectName("grab_radioButton")
        self.release_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.release_radioButton.setGeometry(QtCore.QRect(680, 600, 91, 21))
        self.release_radioButton.setObjectName("release_radioButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 450, 111, 51))
        self.label.setObjectName("label")
        self.space_unit = QtWidgets.QLabel(self.centralwidget)
        self.space_unit.setGeometry(QtCore.QRect(790, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.space_unit.setFont(font)
        self.space_unit.setObjectName("space_unit")
        self.angle_label = QtWidgets.QLabel(self.centralwidget)
        self.angle_label.setGeometry(QtCore.QRect(650, 150, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.angle_label.setFont(font)
        self.angle_label.setObjectName("angle_label")
        self.angle_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.angle_lineEdit.setGeometry(QtCore.QRect(730, 150, 51, 31))
        self.angle_lineEdit.setObjectName("angle_lineEdit")
        self.angle_unit = QtWidgets.QLabel(self.centralwidget)
        self.angle_unit.setGeometry(QtCore.QRect(790, 160, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.angle_unit.setFont(font)
        self.angle_unit.setObjectName("angle_unit")
        self.projectname_label = QtWidgets.QLabel(self.centralwidget)
        self.projectname_label.setGeometry(QtCore.QRect(850, 440, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.projectname_label.setFont(font)
        self.projectname_label.setObjectName("projectname_label")
        self.projectName_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.projectName_lineEdit.setEnabled(False)
        self.projectName_lineEdit.setGeometry(QtCore.QRect(1000, 440, 631, 31))
        self.projectName_lineEdit.setObjectName("projectName_lineEdit")
        self.save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.save_pushButton.setGeometry(QtCore.QRect(1680, 440, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setObjectName("save_pushButton")
        self.load_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.load_pushButton.setGeometry(QtCore.QRect(1790, 440, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.load_pushButton.setFont(font)
        self.load_pushButton.setObjectName("load_pushButton")
        self.setPressure_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.setPressure_pushButton.setGeometry(QtCore.QRect(1250, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.setPressure_pushButton.setFont(font)
        self.setPressure_pushButton.setObjectName("setPressure_pushButton")
        self.readPressure_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.readPressure_pushButton.setGeometry(QtCore.QRect(1410, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.readPressure_pushButton.setFont(font)
        self.readPressure_pushButton.setObjectName("readPressure_pushButton")
        self.airpressure_label = QtWidgets.QLabel(self.centralwidget)
        self.airpressure_label.setGeometry(QtCore.QRect(1270, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.airpressure_label.setFont(font)
        self.airpressure_label.setObjectName("airpressure_label")
        self.purgeOn_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.purgeOn_pushButton.setGeometry(QtCore.QRect(1340, 250, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.purgeOn_pushButton.setFont(font)
        self.purgeOn_pushButton.setObjectName("purgeOn_pushButton")
        self.pressure_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pressure_lineEdit.setGeometry(QtCore.QRect(290, 510, 71, 41))
        self.pressure_lineEdit.setObjectName("pressure_lineEdit")
        self.airpressure_unit = QtWidgets.QLabel(self.centralwidget)
        self.airpressure_unit.setGeometry(QtCore.QRect(1460, 90, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.airpressure_unit.setFont(font)
        self.airpressure_unit.setObjectName("airpressure_unit")
        self.valveStart_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.valveStart_pushButton.setGeometry(QtCore.QRect(1600, 300, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.valveStart_pushButton.setFont(font)
        self.valveStart_pushButton.setObjectName("valveStart_pushButton")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(1630, 210, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.time_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.time_lineEdit.setGeometry(QtCore.QRect(1730, 220, 61, 31))
        self.time_lineEdit.setObjectName("time_lineEdit")
        self.grab_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.grab_pushButton.setGeometry(QtCore.QRect(350, 90, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.grab_pushButton.setFont(font)
        self.grab_pushButton.setObjectName("grab_pushButton")
        self.time_unit = QtWidgets.QLabel(self.centralwidget)
        self.time_unit.setGeometry(QtCore.QRect(1800, 230, 31, 21))
        self.time_unit.setObjectName("time_unit")
        self.valveStop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.valveStop_pushButton.setEnabled(False)
        self.valveStop_pushButton.setGeometry(QtCore.QRect(1760, 300, 121, 41))
        self.valveStop_pushButton.setObjectName("valveStop_pushButton")
        self.r_label = QtWidgets.QLabel(self.centralwidget)
        self.r_label.setGeometry(QtCore.QRect(860, 150, 39, 37))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.r_label.setFont(font)
        self.r_label.setObjectName("r_label")
        self.x_label = QtWidgets.QLabel(self.centralwidget)
        self.x_label.setGeometry(QtCore.QRect(860, 10, 39, 45))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.x_label.setFont(font)
        self.x_label.setObjectName("x_label")
        self.y_label = QtWidgets.QLabel(self.centralwidget)
        self.y_label.setGeometry(QtCore.QRect(860, 62, 39, 37))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.y_label.setFont(font)
        self.y_label.setObjectName("y_label")
        self.xPoint_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.xPoint_lineEdit.setEnabled(False)
        self.xPoint_lineEdit.setGeometry(QtCore.QRect(900, 20, 91, 31))
        self.xPoint_lineEdit.setObjectName("xPoint_lineEdit")
        self.zPoint_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.zPoint_lineEdit.setEnabled(False)
        self.zPoint_lineEdit.setGeometry(QtCore.QRect(900, 110, 91, 31))
        self.zPoint_lineEdit.setObjectName("zPoint_lineEdit")
        self.yPoint_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yPoint_lineEdit.setEnabled(False)
        self.yPoint_lineEdit.setGeometry(QtCore.QRect(900, 60, 91, 31))
        self.yPoint_lineEdit.setObjectName("yPoint_lineEdit")
        self.rAngle_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rAngle_lineEdit.setEnabled(False)
        self.rAngle_lineEdit.setGeometry(QtCore.QRect(900, 150, 91, 31))
        self.rAngle_lineEdit.setObjectName("rAngle_lineEdit")
        self.z_label = QtWidgets.QLabel(self.centralwidget)
        self.z_label.setGeometry(QtCore.QRect(860, 106, 39, 37))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.z_label.setFont(font)
        self.z_label.setObjectName("z_label")
        self.coordinateSystem_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.coordinateSystem_comboBox.setGeometry(QtCore.QRect(640, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coordinateSystem_comboBox.setFont(font)
        self.coordinateSystem_comboBox.setObjectName("coordinateSystem_comboBox")
        self.coordinateSystem_comboBox.addItem("")
        self.coordinateSystem_comboBox.addItem("")
        self.joint1_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.joint1_lineEdit.setEnabled(False)
        self.joint1_lineEdit.setGeometry(QtCore.QRect(1070, 20, 91, 31))
        self.joint1_lineEdit.setObjectName("joint1_lineEdit")
        self.joint2_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.joint2_lineEdit.setEnabled(False)
        self.joint2_lineEdit.setGeometry(QtCore.QRect(1070, 70, 91, 31))
        self.joint2_lineEdit.setObjectName("joint2_lineEdit")
        self.J1_label = QtWidgets.QLabel(self.centralwidget)
        self.J1_label.setGeometry(QtCore.QRect(1030, 30, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.J1_label.setFont(font)
        self.J1_label.setObjectName("J1_label")
        self.J2_label = QtWidgets.QLabel(self.centralwidget)
        self.J2_label.setGeometry(QtCore.QRect(1030, 80, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.J2_label.setFont(font)
        self.J2_label.setObjectName("J2_label")
        self.J4_label = QtWidgets.QLabel(self.centralwidget)
        self.J4_label.setGeometry(QtCore.QRect(1030, 160, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.J4_label.setFont(font)
        self.J4_label.setObjectName("J4_label")
        self.J3_label = QtWidgets.QLabel(self.centralwidget)
        self.J3_label.setGeometry(QtCore.QRect(1030, 120, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.J3_label.setFont(font)
        self.J3_label.setObjectName("J3_label")
        self.joint3_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.joint3_lineEdit.setEnabled(False)
        self.joint3_lineEdit.setGeometry(QtCore.QRect(1070, 110, 91, 31))
        self.joint3_lineEdit.setObjectName("joint3_lineEdit")
        self.joint4_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.joint4_lineEdit.setEnabled(False)
        self.joint4_lineEdit.setGeometry(QtCore.QRect(1070, 150, 91, 31))
        self.joint4_lineEdit.setObjectName("joint4_lineEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(600, 0, 20, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1190, 0, 20, 411))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1550, 0, 20, 411))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(800, 420, 16, 851))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(1560, 170, 421, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.emergencyStop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.emergencyStop_pushButton.setGeometry(QtCore.QRect(1660, 20, 120, 120))
        self.emergencyStop_pushButton.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 14pt \"Adobe Devanagari\";\n"
"border-radius:60px;\n"
"border: 10px groove gray;\n"
"background-color:rgb(255,0,0)")
        self.emergencyStop_pushButton.setObjectName("emergencyStop_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2159, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Robot_label.setText(_translate("MainWindow", "Robot"))
        self.Init_pushButton.setText(_translate("MainWindow", "Init"))
        self.velocityRatio_label.setText(_translate("MainWindow", "velocity:"))
        self.accelerationRatio_label.setText(_translate("MainWindow", "acceleration:"))
        self.setVelocity_pushButton.setText(_translate("MainWindow", "setVelocity"))
        self.stop_pushButton.setText(_translate("MainWindow", "Stop"))
        self.Pressure_label.setText(_translate("MainWindow", "Pressure"))
        self.pressure_label_2.setText(_translate("MainWindow", "pressure :"))
        self.pressure_unit.setText(_translate("MainWindow", "psi"))
        self.Valve_label.setText(_translate("MainWindow", "Valve"))
        self.xPoint_lineEdit_2.setText(_translate("MainWindow", "200.0000"))
        self.yPoint_lineEdit_2.setText(_translate("MainWindow", "0.0000"))
        self.zPoint_lineEdit_2.setText(_translate("MainWindow", "100.0000"))
        self.rAngle_lineEdit_2.setText(_translate("MainWindow", "0.0000"))
        self.v_lineEdit.setText(_translate("MainWindow", "5"))
        self.a_lineEdit.setText(_translate("MainWindow", "5"))
        self.v_label.setText(_translate("MainWindow", "%"))
        self.a_label.setText(_translate("MainWindow", "%"))
        self.airpressure_lineEdit.setText(_translate("MainWindow", "-0.6"))
        self.pulseTime_label.setText(_translate("MainWindow", "pulseTime :"))
        self.pulseTime_lineEdit.setText(_translate("MainWindow", "0"))
        self.pulseTime_unit.setText(_translate("MainWindow", "ms"))
        self.xAdd_pushButton.setText(_translate("MainWindow", "X+"))
        self.xReduce_pushButton.setText(_translate("MainWindow", "X-"))
        self.yAdd_pushButton.setText(_translate("MainWindow", "Y+"))
        self.yReduce_pushButton.setText(_translate("MainWindow", "Y-"))
        self.rReduce_pushButton.setText(_translate("MainWindow", "R-"))
        self.zAdd_pushButton.setText(_translate("MainWindow", "Z+"))
        self.rAdd_pushButton.setText(_translate("MainWindow", "R+"))
        self.zReduce_pushButton.setText(_translate("MainWindow", "Z-"))
        self.space_label.setText(_translate("MainWindow", "Space:"))
        self.space_lineEdit.setText(_translate("MainWindow", "20"))
        self.x_label_2.setText(_translate("MainWindow", "x :"))
        self.y_label_2.setText(_translate("MainWindow", "Y :"))
        self.z_label_2.setText(_translate("MainWindow", "Z :"))
        self.r_label_2.setText(_translate("MainWindow", "R :"))
        self.add_pushButton.setText(_translate("MainWindow", "add"))
        self.delete_pushButton.setText(_translate("MainWindow", "delete"))
        self.insert_pushButton.setText(_translate("MainWindow", "insert"))
        self.run_pushButton.setText(_translate("MainWindow", "Run"))
        self.pause_pushButton.setText(_translate("MainWindow", "||"))
        self.grab_radioButton.setText(_translate("MainWindow", "Grab"))
        self.release_radioButton.setText(_translate("MainWindow", "Release"))
        self.label.setText(_translate("MainWindow", "抓手状态"))
        self.space_unit.setText(_translate("MainWindow", "mm"))
        self.angle_label.setText(_translate("MainWindow", "Angle:"))
        self.angle_lineEdit.setText(_translate("MainWindow", "10"))
        self.angle_unit.setText(_translate("MainWindow", "°"))
        self.projectname_label.setText(_translate("MainWindow", "Project name:"))
        self.save_pushButton.setText(_translate("MainWindow", "Save"))
        self.load_pushButton.setText(_translate("MainWindow", "Load"))
        self.setPressure_pushButton.setText(_translate("MainWindow", "setPressure"))
        self.readPressure_pushButton.setText(_translate("MainWindow", "readPressure"))
        self.airpressure_label.setText(_translate("MainWindow", "airpressure :"))
        self.purgeOn_pushButton.setText(_translate("MainWindow", "purgeOn"))
        self.pressure_lineEdit.setText(_translate("MainWindow", "-0.6"))
        self.airpressure_unit.setText(_translate("MainWindow", "psi"))
        self.valveStart_pushButton.setText(_translate("MainWindow", "valveStart"))
        self.time_label.setText(_translate("MainWindow", "pulsetime:"))
        self.time_lineEdit.setText(_translate("MainWindow", "5000"))
        self.grab_pushButton.setText(_translate("MainWindow", "Grab"))
        self.time_unit.setText(_translate("MainWindow", "ms"))
        self.valveStop_pushButton.setText(_translate("MainWindow", "valveStop"))
        self.r_label.setText(_translate("MainWindow", "R :"))
        self.x_label.setText(_translate("MainWindow", "x :"))
        self.y_label.setText(_translate("MainWindow", "Y :"))
        self.xPoint_lineEdit.setText(_translate("MainWindow", "0.0000"))
        self.zPoint_lineEdit.setText(_translate("MainWindow", "0.0000"))
        self.yPoint_lineEdit.setText(_translate("MainWindow", "0.0000"))
        self.rAngle_lineEdit.setText(_translate("MainWindow", "0.0000"))
        self.z_label.setText(_translate("MainWindow", "Z :"))
        self.coordinateSystem_comboBox.setItemText(0, _translate("MainWindow", "笛卡尔坐标系"))
        self.coordinateSystem_comboBox.setItemText(1, _translate("MainWindow", "关节坐标系"))
        self.joint1_lineEdit.setText(_translate("MainWindow", "0.0000"))
        self.joint2_lineEdit.setText(_translate("MainWindow", "0.0000"))
        self.J1_label.setText(_translate("MainWindow", "J1:"))
        self.J2_label.setText(_translate("MainWindow", "J2:"))
        self.J4_label.setText(_translate("MainWindow", "J4:"))
        self.J3_label.setText(_translate("MainWindow", "J3:"))
        self.joint3_lineEdit.setText(_translate("MainWindow", "0.0000"))
        self.joint4_lineEdit.setText(_translate("MainWindow", "0.0000"))
        self.emergencyStop_pushButton.setText(_translate("MainWindow", "紧急暂停"))

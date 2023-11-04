# 导入程序运行必须模块
import datetime
import threading
import time
from pathlib import Path
import sys
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from threading import Timer

import serial
import xlrd
import xlwt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView
from qtpy.QtCore import Qt


# 导入designer工具生成的主界面模块
from ui.MainUI import Ui_MainWindow
import Warning
from Robot import RobotImpl
from Pressure import PressureImpl
from Valve import ValveImpl
from Precigenome.PGMFC import PGMFC


warning = Warning.Warning
# 储存为列表字典格式，例如[{0: '230.0000', 1: '0', 2: 'grab', ...}, {1: '100', 2: 'release', ...}]
global data, data_list
data = []
data_list = {}
global position
global bool_getPosition
global bool_itemRevise
#global bool_getWarning
global state
global timer
global timer_vlave


dobot_m1=RobotImpl()          #机械臂实例化
precigenome_claw = PressureImpl()  # 控制夹爪的流控仪
precigenome_chip = PressureImpl()   # 控制芯片的流控仪实例化
elec_valve=ValveImpl()        #电磁阀实例化

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

        # bool变量
        self.bool_dobotConnect=0    #判断robot是否connect的bool变量
        self.bool_clawConnect=0 #判断pressure是否connect的bool变量
        self.bool_chipConnect = 0  # 判断pressure是否connect的bool变量
        self.bool_valveConnect=0    #判断valve是否connect的bool变量
        self.bool_init=0            #判断是否初始化的bool变量

        self.bool_robotGrab = 0  #判断claw抓取和释放的bool变量
        self.bool_pressure = 0   #判断pressure on和off的bool变量
        self.bool_valve = 0      #判断pressure on和off的bool变量

        self.bool_run = 0        #判断process是否运行的bool变量


        ####################### 分割线上半部分的信号和槽。#############################
        # 添加Init按钮信号和槽。注意deviceInit函数不加小括号()
        self.Init_pushButton.clicked.connect(self.Init)

        # 添加滑块和setVelocity按钮信号和槽。
        self.v_horizontalSlider.valueChanged[int].connect(self.setVelocityRatio)
        self.a_horizontalSlider.valueChanged[int].connect(self.setaccelerationRatio)
        self.setVelocity_pushButton.clicked.connect(self.robot_setVelocity)
        # 添加grab按钮信号和槽。
        self.grab_pushButton.clicked.connect(self.robot_grab)

        # 添加坐标系下拉框的选项
        self.coordinateSystem_comboBox.currentIndexChanged.connect(self.refresh_coordinate)
        # 添加X+按钮信号和槽。
        self.xAdd_pushButton.clicked.connect(self.robot_xAdd)
        # 添加X-按钮信号和槽。
        self.xReduce_pushButton.clicked.connect(self.robot_xReduce)
        # 添加Y+按钮信号和槽。
        self.yAdd_pushButton.clicked.connect(self.robot_yAdd)
        # 添加Y-按钮信号和槽。
        self.yReduce_pushButton.clicked.connect(self.robot_yReduce)
        # 添加Z+按钮信号和槽。
        self.zAdd_pushButton.clicked.connect(self.robot_zAdd)
        # 添加Z-按钮信号和槽。
        self.zReduce_pushButton.clicked.connect(self.robot_zReduce)
        # 添加R+按钮信号和槽。
        self.rAdd_pushButton.clicked.connect(self.robot_rAdd)
        # 添加R-按钮信号和槽。
        self.rReduce_pushButton.clicked.connect(self.robot_rReduce)

        # Pressure的控制
        # 添加setPressure按钮信号和槽
        self.setPressure_pushButton.clicked.connect(self.pressure_setPressure)
        # 添加readPressure按钮和槽
        self.readPressure_pushButton.clicked.connect(self.pressure_readPressure)
        # 添加purgeOn按钮和槽
        self.purgeOn_pushButton.clicked.connect(self.pressure_purgeOn)

        # Valve的控制
        # 添加valveState按钮信号和槽。
        self.valveStart_pushButton.clicked.connect(self.valve_valveStart)
        self.valveStop_pushButton.clicked.connect(self.valve_valveStop)

        # 添加紧急停止按钮信号和槽。
        #self.emergencyStop_pushButton.clicked.connect(self.thread_emergencyStop)
        self.emergencyStop_pushButton.clicked.connect(self.emergencyStop)

        ####################### 分割线下半部分的信号和槽。#############################
        # table
        # 添加add按钮信号和槽。
        self.add_pushButton.clicked.connect(self.table_add)
        # 添加delete按钮信号和槽。
        self.delete_pushButton.clicked.connect(self.table_delete)
        # 添加insert按钮信号和槽。
        self.insert_pushButton.clicked.connect(self.table_insert)
        # 添加grab/release选择
        self.grab_radioButton.clicked.connect(self.grab_radio)
        self.release_radioButton.clicked.connect(self.release_radio)

        # 添加save和load按钮的信号和槽。
        self.save_pushButton.clicked.connect(self.data_save)
        self.load_pushButton.clicked.connect(self.data_load)
        # 添加run、pause、stop按钮的信号和槽。
        self.run_pushButton.clicked.connect(self.process_run)
        self.pause_pushButton.clicked.connect(self.process_pause)
        self.stop_pushButton.clicked.connect(self.process_stop)

    def initUI(self):
        self.table = QTableWidget(self)
        self.table.move(850, 580)
        self.table.setColumnCount(7)
        self.table.setFixedHeight(400)
        self.table.setFixedWidth(1000)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置选取方式为单个选取
        self.table.setHorizontalHeaderLabels(["X", "Y", "Z", "R", "pressure","pluseTime", "Claw"])  # 设置行表头
        # self.table.verticalHeader().setVisible(True)  # False隐藏列表头

    ####################### 分割线上半部分的实现 #############################
    # 设备初始化，Robot、Pressure、Valve的connect和Robot移动至初始位置
    def Init(self):
        if self.bool_init == 0:
            self.deviceInit()
        else:
            self.deviceDisconnect()

    def deviceInit(self):
        self.button_enable(0)
        self.Init_pushButton.setEnabled(1)

        bool_clawConnect = 0
        bool_chipConnect = 0
        bool_dobotConnect = 0
        bool_valveConnect = 0

        # 列出所有当前的com口
        port_list = list(serial.tools.list_ports.comports())
        port_list_name = []
        # get all com
        if len(port_list) <= 0:
            print("the serial port can't find!")
        else:
            for itms in port_list:
                port_list_name.append(itms.device)
        print(port_list_name)

        instrument_serial_numbers = PGMFC.detect()
        print(instrument_serial_numbers)
        if len(instrument_serial_numbers) == 2:
            print(instrument_serial_numbers[0])
            precigenome_claw.connect(instrument_serial_numbers[0])  # 流控仪检测到两个端口，小的端口为claw
            #precigenome_claw.setPressure(1, 10)
            #precigenome_claw.purgeOn(1)
            #time.sleep(3)
            #precigenome_claw.purgeOff(1)
            port = 'COM' + str(instrument_serial_numbers[0])
            print(port)
            port_list_name.remove(port)
            print(port_list_name)
            bool_clawConnect = 1

            precigenome_chip.connect(instrument_serial_numbers[1])
            #precigenome_chip.setPressure(1, 10)
            #precigenome_chip.purgeOn(1)
            #time.sleep(3)
            #precigenome_chip.purgeOff(1)
            port = 'COM' + str(instrument_serial_numbers[1])
            port_list_name.remove(port)
            print(port_list_name)
            bool_chipConnect = 1
        else:
            #print("请保证连接两台流控仪！")
            q_message = QMessageBox.information(self, "Tips", "请保证连接两台流控仪！", QMessageBox.Ok)


        if bool_clawConnect and bool_chipConnect:
            for i in range(0, len(port_list_name), 1):
                print(port_list_name[i])
                valve_state = elec_valve.connect(port_list_name[i])
                print(valve_state)
                if valve_state == 1:
                    bool_valveConnect = 1
                    break
                else:
                    if i == len(port_list_name) - 1:
                        #print("请保证单片机已连接")
                        q_message = QMessageBox.information(self, "Tips", "请保证单片机已连接", QMessageBox.Ok)
                        precigenome_claw.disconnect()
                        precigenome_chip.disconnect()

        if bool_valveConnect:
            print(len(port_list_name))
            for i in range(0, len(port_list_name), 1):
                print(port_list_name[i])
                dobot_state = dobot_m1.connect(port_list_name[i])
                print(dobot_state)
                if dobot_state == 1:
                    print("机械臂连接成功")
                    position = []
                    position = dobot_m1.getPosition()
                    print(position)
                    bool_dobotConnect = 1
                    port_list_name.remove(port_list_name[i])
                    print(port_list_name)
                    break
                else:
                    print(11111)
                    if i == len(port_list_name) - 1:
                        #print("请保证机械臂已连接")
                        q_message = QMessageBox.information(self, "Tips", "请保证机械臂已连接", QMessageBox.Ok)
                        precigenome_claw.disconnect()
                        precigenome_chip.disconnect()
                        elec_valve.disconnect()

        if bool_clawConnect and bool_chipConnect and bool_dobotConnect and bool_valveConnect:
            q_message = QMessageBox.information(self, "Tips", "初始化成功！", QMessageBox.Ok)
            self.bool_init = 1
            self.button_enable(1)
            self.Init_pushButton.setText("Disconnect")

            threads = []
            thread_getPosition = threading.Thread(target=self.get_position)
            threads.append(thread_getPosition)
            ##thread_getWarning = threading.Thread(target=self.get_warning)
            ##threads.append(thread_getWarning)

            for t in threads:
                timer_getPosition = Timer(1, self.get_position)
                timer_getPosition.start()
                ##timer_getWarning = Timer(1, self.get_warning)
                ##timer_getWarning.start()

                t.setDaemon(True)
                t.start()
            time.sleep(0.5)
            dobot_m1.setVelocity(5, 5)  # 设置速度和加速度均为5%
            # 移动至初始位置
            dobot_m1.MoveToPoint_Joint(-38.5066, 78.1401, 207.002, -81.0742)  # 移动至初始位置
            self.Release()  # 爪张开
            time.sleep(1)
            precigenome_claw.purgeOff(1)
            self.bool_robotGrab = 0
        else:
            self.button_enable(1)
            q_message = QMessageBox.information(self, "Tips", "初始化失败,请保证所有设备连接！", QMessageBox.Ok)


    def deviceDisconnect(self):
        global bool_getPosition
        global bool_itemRevise
        global bool_getWarning
        print("Disconnect")

        dobot_m1.stop()
        dobot_m1.disconnect()
        self.bool_dobotConnect=0
        time.sleep(0.5)

        self.Release()  # 爪张开
        self.bool_robotGrab = 0
        precigenome_claw.purgeOff(1)
        precigenome_claw.disconnect()
        self.bool_clawpconnect = 0
        time.sleep(0.5)

        precigenome_chip.purgeOff(1)
        self.bool_pressure = 0
        precigenome_chip.disconnect()
        self.bool_chipConnect = 0
        time.sleep(0.5)


        elec_valve.ValveState(2, 0)
        self.bool_valve=0
        elec_valve.disconnect()
        self.bool_valveConnect=0
        time.sleep(0.5)

        self.Init_pushButton.setText("Init")
        self.bool_init = 0
        print("结束运行！")
        bool_getPosition = False
        bool_itemRevise=False
        bool_getWarning = False

    def Grab(self):
        precigenome_claw.setPressure(1, -9,60000)  # 设置负压，runtime=60000s
        time.sleep(1)
        precigenome_claw.purgeOn(1)  # 关闭爪
        time.sleep(1)
        # logger.instance().log("Dobot Grabbing!")  # 输出到logger中
        print('Grabbing...')


    def Release(self):
        precigenome_claw.setPressure(1, 9,60000) #设置正压，runtime=60000s
        time.sleep(1)
        precigenome_claw.purgeOn(1)   #打开爪
        time.sleep(1)
        #logger.instance().log("Dobot softRelease!")  # 输出到logger中
        print('Releasing...')

    # grab按钮的实现
    def robot_grab(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.Ok)
        else:
            if self.bool_robotGrab == 0:
                self.Grab()
                self.bool_robotGrab = 1
                self.grab_pushButton.setText(u'Release')
            else:
                self.Release()
                self.bool_robotGrab = 0
                self.grab_pushButton.setText(u'Grab')

    # 显示速度比
    def setVelocityRatio(self, value):
        self.v_lineEdit.setText(str(value))

    # 显示加速度比
    def setaccelerationRatio(self, value):
        self.a_lineEdit.setText(str(value))

    def robot_setVelocity(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            velocityRatio = self.v_lineEdit.text()
            accelerationRatio = self.a_lineEdit.text()
            self.v_horizontalSlider.setValue(int(velocityRatio))
            self.a_horizontalSlider.setValue(int(accelerationRatio))
            dobot_m1 .setVelocity(int(velocityRatio), int(accelerationRatio))
            q_message = QMessageBox.information(self, "Tips", "设置成功! 速度为："+velocityRatio+"%,加速度为："+accelerationRatio+"%!", QMessageBox.Ok)

    def get_lineEdit(self)->bool:
        global space
        global angle
        space = float(self.space_lineEdit.text())
        angle = float(self.angle_lineEdit.text())
        judge_space=0
        judge_angle=0
        if space > 0 and space <= 50:
            judge_space = 1
        else:
            q_message = QMessageBox.information(self, "Tips", "space请在0-50mm之间！", QMessageBox.Ok)

        if angle > 0 and angle <= 45:
            judge_angle = 1
        else:
            q_message = QMessageBox.information(self, "Tips", "angle请在0-45°之间！", QMessageBox.Ok)
        if judge_angle and judge_space:
            return 1
        else:
            return 0

    def refresh_coordinate(self):
        if(self.coordinateSystem_comboBox.currentIndex()==1):
            self.xAdd_pushButton.setText("J1+")
            self.xReduce_pushButton.setText("J1-")
            self.yAdd_pushButton.setText("J2+")
            self.yReduce_pushButton.setText("J2-")
            self.zAdd_pushButton.setText("J3+")
            self.zReduce_pushButton.setText("J3-")
            self.rAdd_pushButton.setText("J4+")
            self.rReduce_pushButton.setText("J4-")
        else:
            self.xAdd_pushButton.setText("X+")
            self.xReduce_pushButton.setText("X-")
            self.yAdd_pushButton.setText("Y+")
            self.yReduce_pushButton.setText("Y")
            self.zAdd_pushButton.setText("Z+")
            self.zReduce_pushButton.setText("Z-")
            self.rAdd_pushButton.setText("R+")
            self.rReduce_pushButton.setText("R-")

    def robot_xAdd(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.Ok)
        else:
            if self.get_lineEdit():
                if(self.coordinateSystem_comboBox.currentIndex()==0):
                    position[0]=position[0]+space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                else:
                    position[4]=position[4]+space
                    dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6], position[7])
                '''position[0]=position[0]+space
                dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                self.xPoint_lineEdit.setText(str(float('%.4f' % position[0])))
                QApplication.processEvents()  # 刷新界面 
                if (position[0]+space)<=350:
                    position[0]=position[0]+space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                    self.xPoint_lineEdit.setText(str(float('%.2f' % position[0])))
                    QApplication.processEvents()  # 刷新界面
                else:
                    q_message = QMessageBox.information(self, "Tips", "X轴右超限！", QMessageBox.Ok)'''
            else:
                pass


    def robot_xReduce(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            if self.get_lineEdit():
                if (self.coordinateSystem_comboBox.currentIndex() == 0):
                    position[0] = position[0] - space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                else:
                    position[4] = position[4] - space
                    dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6], position[7])
                '''position[0]=position[0]-space
                dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                self.xPoint_lineEdit.setText(str(float('%.4f' % position[0])))
                QApplication.processEvents()  # 刷新界面
                if (position[0]-space) >= 200:
                    position[0]=position[0]-space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                    self.xPoint_lineEdit.setText(str(float('%.2f' % position[0])))
                    QApplication.processEvents()  # 刷新界面
                else:
                    q_message = QMessageBox.information(self, "Tips", "X轴左超限！", QMessageBox.Ok)'''
            else:
                pass

    def robot_yAdd(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            if self.get_lineEdit():
                if (self.coordinateSystem_comboBox.currentIndex() == 0):
                    position[1]=position[1]+space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                else:
                    position[5] = position[5] + space
                    dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6], position[7])
                '''position[1]=position[1]+space
                dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                self.yPoint_lineEdit.setText(str(float('%.4f' % position[1])))
                QApplication.processEvents()  # 刷新界面
                if (position[1]+space)<=160:
                    position[1]=position[1]+space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                    self.yPoint_lineEdit.setText(str(float('%.2f' % position[1])))
                    QApplication.processEvents()  # 刷新界面
                else:
                    q_message = QMessageBox.information(self, "Tips", "Y轴右超限！", QMessageBox.Ok)'''
            else:
                pass

    def robot_yReduce(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            if self.get_lineEdit():
                if (self.coordinateSystem_comboBox.currentIndex() == 0):
                    position[1]=position[1]-space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                else:
                    position[5] = position[5] - space
                    dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6], position[7])
                '''position[1]=position[1]-space
                dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                self.yPoint_lineEdit.setText(str(float('%.4f' % position[1])))
                QApplication.processEvents()  # 刷新界面
                if (position[1]-space)>=-150:
                    position[1]=position[1]-space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                    self.yPoint_lineEdit.setText(str(float('%.2f' % position[1])))
                    QApplication.processEvents()  # 刷新界面
                else:
                    q_message = QMessageBox.information(self, "Tips", "Y轴左超限！", QMessageBox.Ok)'''
            else:
                pass

    def robot_zAdd(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            if self.get_lineEdit():
                if (self.coordinateSystem_comboBox.currentIndex() == 0):
                    position[2]=position[2]+space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                else:
                    position[6] = position[6] + space
                    dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6], position[7])
                '''if (position[2]+space)<=235:
                    position[2] = position[2] + space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                    self.zPoint_lineEdit.setText(str(float('%.4f' % position[2])))
                    QApplication.processEvents()  # 刷新界面
                else:
                    q_message = QMessageBox.information(self, "Tips", "Z轴上超限！", QMessageBox.Ok)'''
            else:
                pass

    def robot_zReduce(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            if self.get_lineEdit():
                if (self.coordinateSystem_comboBox.currentIndex() == 0):
                    position[2]=position[2]-space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                else:
                    position[6] = position[6] - space
                    dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6], position[7])
                '''if (position[2]-space)>=80:
                    position[2] = position[2] - space
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                    self.zPoint_lineEdit.setText(str(float('%.4f' % position[2])))
                    QApplication.processEvents()  # 刷新界面
                else:
                    q_message = QMessageBox.information(self, "Tips", "Z轴下超限！", QMessageBox.Ok)'''
            else:
                pass

    def robot_rAdd(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.Ok)
        else:
            if self.get_lineEdit():
                print(position[3])
                if (self.coordinateSystem_comboBox.currentIndex() == 0):
                    position[3]=position[3] + angle
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                else:
                    position[7] = position[7] + angle
                    dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6], position[7])
                '''if (position[3]+angle)<=300:
                    position[3] = position[3] + angle
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                    self.rAngle_lineEdit.setText(str(float('%.4f' % position[3])))
                    QApplication.processEvents()  # 刷新界面
                else:
                    q_message = QMessageBox.information(self, "Tips", "R右超限！", QMessageBox.Ok)'''
            else:
                pass

    def robot_rReduce(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.Ok)
        else:
            if self.get_lineEdit():
                if (self.coordinateSystem_comboBox.currentIndex() == 0):
                    position[3] = position[3] - angle
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                else:
                    position[7] = position[7] - angle
                    dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6], position[7])
                '''if (position[3]-angle) >= -300:
                    position[3] = position[3] - angle
                    dobot_m1.MoveToPoint(position[0], position[1], position[2], position[3])
                    self.rAngle_lineEdit.setText(str(float('%.4f' % position[3])))
                    QApplication.processEvents()  # 刷新界面
                else:
                    q_message = QMessageBox.information(self, "Tips", "R左超限！", QMessageBox.Ok)'''
            else:
                pass

    def grab_radio(self):
        if self.grab_radioButton.isChecked():
            self.release_radioButton.setChecked(0)
        else:
            self.release_radioButton.setChecked(1)

    def release_radio(self):
        if self.release_radioButton.isChecked():
            self.grab_radioButton.setChecked(0)
        else:
            self.grab_radioButton.setChecked(1)

    def pressure_setPressure(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            airpressure = self.airpressure_lineEdit.text()
            if float(airpressure)>-10 and float(airpressure)<15:
                print(float(airpressure))
                precigenome_chip.setPressure(1,float(airpressure))
            else:
                q_message = QMessageBox.information(self, "Tips", "pressure请在-10-15psi之间！", QMessageBox.OK)


    def pressure_readPressure(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            if self.bool_pressure:
                print("readPressure")
                airpressure = precigenome_chip.readPressure(1)
                self.airpressure_lineEdit.setText(str((float('%.4f' % airpressure))))
            else:
                q_message = QMessageBox.information(self, "Tips", "请先purgeOn！", QMessageBox.Ok)


    def pressure_purgeOn(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            if self.bool_pressure == 0:
                precigenome_chip.purgeOn(1)
                self.bool_pressure = 1
                self.purgeOn_pushButton.setText(u'purgeOff')
            else:
                precigenome_chip.purgeOff(1)
                self.bool_pressure = 0
                self.purgeOn_pushButton.setText(u'purgeOn')

    def valve_pulsetime(self):
        now = datetime.datetime.now()
        print(str(now))
        elec_valve.ValveState(2, 0)
        self.bool_valve = 0
        self.valveStart_pushButton.setEnabled(1)
        self.valveStop_pushButton.setEnabled(0)
        self.time_lineEdit.setText(str(5000))
        QApplication.processEvents()  # 刷新界面


    def valve_valveStart(self):
        global timer_vlave
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.Ok)
        else:
            pulsetime = self.time_lineEdit.text()
            if float(pulsetime) > 0:
                timer_vlave = Timer(float(pulsetime) / 1000, self.valve_pulsetime)
                timer_vlave.start()
                now = datetime.datetime.now()
                print(str(now))
                elec_valve.ValveState(2, 1)

                self.bool_valve = 1
                self.valveStart_pushButton.setEnabled(0)
                self.valveStop_pushButton.setEnabled(1)
            else:
                q_message = QMessageBox.information(self, "Tips", "pulsetime请大于0！", QMessageBox.Ok)

    def valve_valveStop(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            elec_valve.ValveState(2, 0)
            self.bool_valve = 0
            self.valveStart_pushButton.setEnabled(1)
            self.valveStop_pushButton.setEnabled(0)

    def thread_emergencyStop(self):
        thread_emergencyStop= threading.Thread(target=self.emergencyStop)
        thread_emergencyStop.setDaemon(True)
        thread_emergencyStop.start()
        thread_emergencyStop.join()

    # 紧急停止按钮的实现
    def emergencyStop(self):
        if self.bool_init == 0:
            q_message = QMessageBox.information(self, "Tips", "请先Init！", QMessageBox.OK)
        else:
            if self.bool_run == 1:
                dobot_m1.stop()
                dobot_m1.reset()
                time.sleep(1)
                dobot_m1.stop()
                global state
                state = "stop"
            else:
                dobot_m1.stop()
                #precigenome_claw.purgeOff(1)
                precigenome_chip.purgeOff(1)
                self.bool_pressure = 0
                elec_valve.ValveState(2, 0)
                self.bool_valve = 0


    ####################### 分割线下半部分的实现 #############################
    # run、stop设置按钮enable状态
    def button_enable(self, value):
        self.Init_pushButton.setEnabled(value)
        self.grab_pushButton.setEnabled(value)
        self.setVelocity_pushButton.setEnabled(value)
        self.xAdd_pushButton.setEnabled(value)
        self.xReduce_pushButton.setEnabled(value)
        self.yAdd_pushButton.setEnabled(value)
        self.yReduce_pushButton.setEnabled(value)
        self.zAdd_pushButton.setEnabled(value)
        self.zReduce_pushButton.setEnabled(value)
        self.rAdd_pushButton.setEnabled(value)
        self.rReduce_pushButton.setEnabled(value)
        self.setPressure_pushButton.setEnabled(value)
        self.readPressure_pushButton.setEnabled(value)
        self.purgeOn_pushButton.setEnabled(value)
        self.valveStart_pushButton.setEnabled(value)
        self.add_pushButton.setEnabled(value)
        self.insert_pushButton.setEnabled(value)
        self.delete_pushButton.setEnabled(value)
        self.save_pushButton.setEnabled(value)
        self.load_pushButton.setEnabled(value)
        self.emergencyStop_pushButton.setEnabled(value)
        self.run_pushButton.setEnabled(value)
        self.pause_pushButton.setEnabled(value)
        self.stop_pushButton.setEnabled(value)

    #table paramter_judge(x和y的限制待补充）
    def table_paramter_judge(self)->bool:
        judge_pressure = 0
        judge_pulsetime = 0
        judge_xPosition=0
        judge_yPosition=0
        judge_zPosition=0
        judge_rAngle=0
        pressure = self.pressure_lineEdit.text()
        if float(pressure) > -10 and float(pressure) < 15:
            judge_pressure = 1
        else:
            q_message = QMessageBox.information(self, "Tips", "pressure请在-10-15psi之间！", QMessageBox.Ok)

        pulsetime = self.pulseTime_lineEdit.text()
        if float(pulsetime) >= 0:
            judge_pulsetime = 1
        else:
            q_message = QMessageBox.information(self, "Tips", "pulsetime请大于等于0！", QMessageBox.Ok)


        xPosition = self.xPoint_lineEdit_2.text()
        if float(xPosition)>=200 and float(xPosition)<=380:
            judge_xPosition=1
        else:
            q_message = QMessageBox.information(self, "Tips", "xPosition请在200-380之间！", QMessageBox.Ok)

        yPosition = self.yPoint_lineEdit_2.text()
        if float(yPosition) >= -120 and float(yPosition) <= 140:
            judge_yPosition = 1
        else:
            q_message = QMessageBox.information(self, "Tips", "yPosition请在-150-160之间！", QMessageBox.Ok)

        zPosition = self.zPoint_lineEdit_2.text()
        if float(zPosition) >= 80 and float(zPosition) <= 235:
            judge_zPosition = 1
        else:
            q_message = QMessageBox.information(self, "Tips", "zPosition请在80-235之间！", QMessageBox.Ok)

        rAngle = self.rAngle_lineEdit_2.text()
        if float(rAngle)>=-300 and float(rAngle)<=300:
            judge_rAngle=1
        else:
            q_message = QMessageBox.information(self, "Tips", "rAngle请在-300°-300°之间！", QMessageBox.Ok)

        if judge_pressure and judge_pulsetime and judge_xPosition and judge_yPosition and judge_zPosition and judge_rAngle:
            return 1
        else:
            return 0

    # add,增加数据
    def table_add(self):
        if self.table_paramter_judge():
            row = self.table.rowCount()
            self.table.insertRow(row)

            xPosition = self.xPoint_lineEdit_2.text()
            item_X = QTableWidgetItem(xPosition)

            yPosition = self.yPoint_lineEdit_2.text()
            item_Y = QTableWidgetItem(yPosition)

            zPosition = self.zPoint_lineEdit_2.text()
            item_Z = QTableWidgetItem(zPosition)

            rAngle = self.rAngle_lineEdit_2.text()
            item_R = QTableWidgetItem(rAngle)

            pressure = self.pressure_lineEdit.text()
            item_pressure = QTableWidgetItem(pressure)

            pulsetime = self.pulseTime_lineEdit.text()
            item_time = QTableWidgetItem(pulsetime)

            if self.grab_radioButton.isChecked():
                item_claw = QTableWidgetItem("grab")
            else:
                item_claw = QTableWidgetItem("release")
            item_claw.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

            # 以下可以加入保存数据到数据的操作
            self.table.setItem(row, 0, item_X)
            self.table.setItem(row, 1, item_Y)
            self.table.setItem(row, 2, item_Z)
            self.table.setItem(row, 3, item_R)
            self.table.setItem(row, 4, item_pressure)
            self.table.setItem(row, 5, item_time)
            self.table.setItem(row, 6, item_claw)
        else:
            pass


    # delete
    def table_delete(self):
        q_message = QMessageBox.information(self, "Tips", "Do you want to delete this row？",
                                            QMessageBox.Yes | QMessageBox.No)
        if QMessageBox.Yes == q_message:
            row_select = self.table.selectedItems()
            if len(row_select) == 0:
                message = QMessageBox.information(self, "Tips", "You have not selected the row you want to delete!",
                                                 QMessageBox.Ok)
            else:
                id = row_select[0].text()
                print("id: {}".format(id))
                row = row_select[0].row()
                self.table.removeRow(row)
        else:
            pass

    def table_insert(self):
        if self.table_paramter_judge():
            row = self.table.currentRow()
            self.table.insertRow(row)

            xPosition = self.xPoint_lineEdit_2.text()
            item_X = QTableWidgetItem(xPosition)

            yPosition = self.yPoint_lineEdit_2.text()
            item_Y = QTableWidgetItem(yPosition)

            zPosition = self.zPoint_lineEdit_2.text()
            item_Z = QTableWidgetItem(zPosition)

            rAngle = self.rAngle_lineEdit_2.text()
            item_R = QTableWidgetItem(rAngle)

            pressure = self.pressure_lineEdit.text()
            item_pressure = QTableWidgetItem(pressure)

            pulsetime = self.pulseTime_lineEdit.text()
            item_time = QTableWidgetItem(pulsetime)

            if self.grab_radioButton.isChecked():
                item_claw = QTableWidgetItem("grab")
            else:
                item_claw = QTableWidgetItem("release")
            item_claw.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

            # 以下可以加入保存数据到数据的操作
            self.table.setItem(row, 0, item_X)
            self.table.setItem(row, 1, item_Y)
            self.table.setItem(row, 2, item_Z)
            self.table.setItem(row, 3, item_R)
            self.table.setItem(row, 4, item_pressure)
            self.table.setItem(row, 5, item_time)
            self.table.setItem(row, 6, item_claw)
        else:
            pass


    def data_save(self):
        judge_item0 = False
        judge_item1 = False
        judge_item2 = False
        judge_item3 = False
        judge_item4 = False
        judge_out=True

        for i in range(0, self.table.rowCount()):
            if float(self.table.item(i, 0).text()) >= 200 and float(self.table.item(i, 0).text()) <= 380:
                judge_item0 = True
            else:
                judge_out = False
                q_message = QMessageBox.information(self, "Tips", "X请在200-380之间！", QMessageBox.Ok)

            if float(self.table.item(i, 1).text()) >= -120 and float(self.table.item(i, 1).text()) <= 140:
                judge_item1 = True
            else:
                judge_out = False
                q_message = QMessageBox.information(self, "Tips", "Y请在-120-140之间！", QMessageBox.Ok)

            if float(self.table.item(i, 2).text()) >= 80 and float(self.table.item(i, 2).text()) <= 235:
                judge_item2 = True
            else:
                judge_out = False
                q_message = QMessageBox.information(self, "Tips", "Z请在80-235之间！", QMessageBox.Ok)

            if float(self.table.item(i, 3).text()) >= -300 and float(self.table.item(i, 3).text()) <= 300:
                judge_item3 = True
            else:
                judge_out = False
                q_message = QMessageBox.information(self, "Tips", "R请在-300-300之间！", QMessageBox.Ok)

            if float(self.table.item(i, 4).text()) >= -10 and float(self.table.item(i, 3).text()) <= 15:
                judge_item4 = True
            else:
                judge_out = False
                q_message = QMessageBox.information(self, "Tips", "Pressure请在-10-15psi之间！", QMessageBox.Ok)

        if judge_item0 and judge_item1 and judge_item2 and judge_item3 and judge_item4 and judge_out:
            book = xlwt.Workbook()
            sheet = book.add_sheet('process data')
            for i in range(0, self.table.rowCount()):
                sheet.write(i + 1, 0, i + 1)  # 加行头
            for j in range(0, self.table.columnCount()):
                sheet.write(0, j + 1, self.table.horizontalHeaderItem(j).text())  # 加列头

            print(self.table.rowCount())
            print(self.table.columnCount())  # 列数9 0-8

            for j in range(0, self.table.columnCount()):
                try:
                    sheet.write(i + 1, j + 1, self.table.item(i, j).text())
                    data_list[j] = self.table.item(i, j).text()
                except:
                    continue
            data.append(data_list.copy())

            # get_filename_path, ok = QFileDialog.getSaveFileName(self,"选取单个文件","C:/","Text Files (*.xls)")
            get_filename_path, ok = QFileDialog.getSaveFileName(self, "请输入文件名", "../data/", "Text Files (*.xls)")
            if ok:
                self.projectName_lineEdit.setText(str(get_filename_path))
                if len(self.projectName_lineEdit.text()) < 1:
                    QMessageBox.information(self.save_pushButton, 'Tips ', '文件名不可为空', QMessageBox.Ok)
                else:
                    ##file_name = Path('../data/' + self.projectName_lineEdit.text() + '.xls')
                    if not get_filename_path:
                        q_message = QMessageBox.information(self.save_pushButton, 'Tips ', '已有该文件，是否覆盖内容',
                                                            QMessageBox.Yes | QMessageBox.No)
                        if QMessageBox.Yes == q_message:
                            book.save(get_filename_path)
                            q_message = QMessageBox.information(self, 'Tips ', '保存成功！')
                        else:
                            pass
                    else:
                        book.save(get_filename_path)
                        q_message = QMessageBox.information(self, 'Tips ', '保存成功！')
        else:
            q_message = QMessageBox.information(self, 'Tips ', '数据超限，保存失败！')
            # print((data_list))
        # print(data)
        # print(data[0])



    def data_load(self):
        # get_filename_path, ok = QFileDialog.getOpenFileName(self,"选取单个文件","C:/","Text Files (*.xls)")
        get_filename_path, ok = QFileDialog.getOpenFileName(self, "请选取单个文件", "../data/","Text Files (*.xls)")
        if ok:
            self.projectName_lineEdit.setText(str(get_filename_path))
            if len(self.projectName_lineEdit.text()) < 1:
                QMessageBox.information(self, 'Tips ', '文件名不可为空', QMessageBox.Ok)
            else:
                if  get_filename_path:
                    xls = xlrd.open_workbook(get_filename_path, "r")
                    sheet = xls.sheet_by_index(0)
                    self.table.setRowCount(sheet.nrows - 1)
                    self.table.setColumnCount(sheet.ncols - 1)
                    for i in range(1, sheet.nrows):
                        for j in range(1, sheet.ncols):
                            item_text = sheet.cell(i, j).value
                            item = QTableWidgetItem(item_text)
                            self.table.setItem(i - 1, j - 1, item)
                else:
                    QMessageBox.information(self, 'Tips ', '要打开的文件不存在!', QMessageBox.Ok)

        # 存储数据到列表字典
        for i in range(0, self.table.rowCount()):
            for j in range(0, self.table.columnCount()):
                try:
                    data_list[j] = self.table.item(i, j).text()
                except:
                    continue
            data.append(data_list.copy())

    def process_valve_off(self):
        now = datetime.datetime.now()
        print("process_valve_off:"+str(now))
        elec_valve.ValveState(2, 0)
    def process_valve_on(self):
        now = datetime.datetime.now()
        print("process_valve_on:"+str(now))
        elec_valve.ValveState(2, 1)


    def process_run(self):
        if len(data) == 0:
            QMessageBox.information(self, 'Tips ', '请先保存后在run！', QMessageBox.Ok)
        else:
            if self.bool_init == 0:
                self.deviceInit()
            else:
                pass
             # 移动至初始位置
            self.button_enable(0)  # run的时候设置一些按钮不能点击

            dobot_m1.MoveToPoint_Joint(-38.5066, 78.1401, 207.002, -81.0742)  # 移动至初始位置
            #dobot_m1.start()
            #QMessageBox.about(self, 'Tips ', '正在初始化，请等待初始化结束！')
            time.sleep(10)
            #if QMessageBox.open():
            #    QMessageBox.close()
            #QMessageBox.information(self, 'Tips ', '初始化结束！')
            self.run_pushButton.setEnabled(1)
            self.pause_pushButton.setEnabled(1)
            self.stop_pushButton.setEnabled(1)
            self.emergencyStop_pushButton.setEnabled(1)
            global state
            state = "run"
            self.bool_run = 1
            #global i
            i = 0
            while i<len(data):
                while state == "pause":
                    QApplication.processEvents()  # 刷新界面
                if state == "stop":
                    dobot_m1.stop()
                    dobot_m1.reset()
                    break

                # data[i][0]为xPosition
                self.table.item(i, 0).setForeground(QBrush(QColor(255, 0, 0)))
                self.table.item(i, 1).setForeground(QBrush(QColor(255, 0, 0)))
                self.table.item(i, 2).setForeground(QBrush(QColor(255, 0, 0)))
                self.table.item(i, 3).setForeground(QBrush(QColor(255, 0, 0)))
                QApplication.processEvents()  # 刷新界面
                dobot_m1.MoveToPoint(float(data[i][0]), float(data[i][1]), float(data[i][2]), float(data[i][3]))
                #time.sleep(5)  # 保证机械臂移动至指定位置后再进行相关操作

                #while(position[0]==float(data[i][0]) and position[1]==float(data[i][1]) and
                #        position[2]==float(data[i][2]) and position[3]==float(data[i][3])):

                print(float(self.xPoint_lineEdit.text()))
                print(float(data[i][0]))
                while (float(self.xPoint_lineEdit.text()) == float(data[i][0]) and
                       float(self.yPoint_lineEdit.text()) == float(data[i][1]) and
                       float(self.zPoint_lineEdit.text()) == float(data[i][2]) and
                       float(self.rAngle_lineEdit.text()) == float(data[i][3])):

                    self.table.item(i, 6).setForeground(QBrush(QColor(255, 0, 0)))
                    QApplication.processEvents()  # 刷新界面
                    if self.bool_robotGrab == 0:
                        if data[i][6] == "grab":
                            self.Grab()
                            self.bool_robotGrab = 1
                            print("grab")
                        else:
                            pass  # 此时爪为张开状态，并且指令为release，无需操作
                    else:
                        if data[i][6] == "release":
                            self.Release()
                            self.bool_robotGrab = 0
                            print("release")
                        else:
                            pass
                    time.sleep(1)

                    self.table.item(i, 4).setForeground(QBrush(QColor(255, 0, 0)))
                    QApplication.processEvents()  # 刷新界面
                    if self.bool_pressure == 0:
                        precigenome_chip.setPressure(1, float(data[i][4]))
                        print("setPressure")
                        time.sleep(1)
                        precigenome_chip.purgeOn(1)
                        print("purgeOn")
                        self.bool_pressure = 1
                    else:
                         pass
                    time.sleep(1)

                    # data[i][5]为pulseTime
                    self.table.item(i, 5).setForeground(QBrush(QColor(255, 0, 0)))
                    QApplication.processEvents()  # 刷新界面
                    if data[i][5] == "0":
                        pass
                    else:
                        temp = float(data[i][5]) / 1000  # temp暂时记录当前pulsetime
                        waiting = temp*5
                        print("开关阀门")
                        '''elec_valve.ValveState(2, 1)'''
                        elec_valve.setPrinting(5, temp, 40, 5, 0)
                        elec_valve.switchState(1)
                        now = datetime.datetime.now()
                        print(str(now))
                        # print(float(data[i][5]) / 1000)
                        # timer_vlave = Timer(float(data[i][5]) / 1000, self.process_valve_off)
                        timer_vlave = Timer(temp, self.process_valve_off)
                        timer_vlave.start()
                        time.sleep(waiting + 1)  # 给多1s的延时足够吸取液体再移动机械逼
                        elec_valve.switchState(0)
                    precigenome_chip.purgeOff(1)
                    self.bool_pressure=0
                    time.sleep(1)
                    i = i + 1
                    if i==4:
                        break
                        print(i)


            time.sleep(1)
            for i in range(0, len(data)):
                for j in range(0, len(data_list)):
                    self.table.item(i, j).setForeground(QBrush(QColor(0, 0, 0)))
                    QApplication.processEvents()  # 刷新界面

            if state=="stop":
                pass
            else:
                self.Release()  # 爪张开
                self.bool_robotGrab = 0
                precigenome_claw.purgeOff(1)
            precigenome_chip.purgeOff(1)
            self.bool_pressure=0
            elec_valve.ValveState(2, 0)
            self.bool_valve=0

            self.bool_run = 0
            self.button_enable(1)  # stop的时候恢复按钮，使能点击

    def process_pause(self):
        global state
        print(self.pause_pushButton.text())
        if self.bool_run == 0:
            q_message = QMessageBox.information(self, "Tips", "你需要先运行！", QMessageBox.Ok)
        else:
            if self.pause_pushButton.text() == "||":
                q_message = QMessageBox.information(self, "Tips", "你确定要暂停吗？", QMessageBox.Yes | QMessageBox.No)
                if QMessageBox.Yes == q_message:
                    print("pausepause")
                    state = "pause"
                    self.pause_pushButton.setText("▷")
                    QApplication.processEvents()  # 刷新界面
                else:
                    pass
            else:
                q_message = QMessageBox.information(self, "Tips", "你确定要恢复吗？", QMessageBox.Yes | QMessageBox.No)
                if QMessageBox.Yes == q_message:
                    state = "run"
                    self.pause_pushButton.setText("||")
                else:
                    pass
        print("ssss")

    # 下面stop按钮的实现
    def process_stop(self):
        if self.bool_run == 0:
            q_message = QMessageBox.information(self, "Tips", "你需要先运行！", QMessageBox.Ok)
        else:
            q_message = QMessageBox.information(self, "Tips", "你确定停止整个流程吗？", QMessageBox.Yes | QMessageBox.No)
            if QMessageBox.Yes == q_message:
                for i in range(0, len(data)):
                    for j in range(0, len(data_list)):
                        self.table.item(i, j).setForeground(QBrush(QColor(0, 0, 0)))
                        QApplication.processEvents()  # 刷新界面
                if self.pause_pushButton.text() == "▷":
                    self.pause_pushButton.setText("||")
                global state
                state = "stop"
                dobot_m1.stop()
                dobot_m1.reset()
                #precigenome_claw.purgeOff(1)
                precigenome_chip.purgeOff(1)
                self.bool_pressure = 0
                elec_valve.ValveState(2, 0)
                self.bool_valve = 0
                self.bool_run = 0
                self.button_enable(1)  # stop的时候恢复按钮，使能点击
            else:
                pass

    global bool_getPosition
    bool_getPosition = True
    # get position
    def get_position(self):
        global position
        #judge_joint1 = True
        #judge_joint2 = True
        #judge_joint3 = True
        #judge_joint4 = True
        position = []
        position = dobot_m1.getPosition()
        print("Getting position")
        print(datetime.datetime.now())
        # print(position)

        if position[4]<-85:
            dobot_m1.stop()
            #judge_joint1=False
            q_message = QMessageBox.information(self, "Tips", "关节一左超限！", QMessageBox.Ok)
            dobot_m1.MoveToPoint_Joint(position[4] + 5,position[5],position[6],position[7])
        elif position[4]<85:
            pass
        else:
            dobot_m1.stop()
            #judge_joint1 = False
            q_message = QMessageBox.information(self, "Tips", "关节一右超限!", QMessageBox.Ok)
            dobot_m1.MoveToPoint_Joint(position[4] - 5 , position[5]-5, position[6], position[7])

        if position[5] < -135:
            dobot_m1.stop()
            #judge_joint2 = False
            q_message = QMessageBox.information(self, "Tips", "关节二左超限！", QMessageBox.Ok)
            dobot_m1.MoveToPoint_Joint(position[4] , position[5]+5, position[6], position[7])
        elif position[5] < 135:
            pass
        else:
            dobot_m1.stop()
            #judge_joint2 = False
            q_message = QMessageBox.information(self, "Tips", "关节二右超限！", QMessageBox.Ok)
            dobot_m1.MoveToPoint_Joint(position[4], position[5]-5, position[6], position[7])

        if position[6] < 10:
            dobot_m1.stop()
            #judge_joint3 = False
            q_message = QMessageBox.information(self, "Tips", "关节三下超限！", QMessageBox.Ok)
            dobot_m1.MoveToPoint_Joint(position[4] , position[5], position[6]+5, position[7])
        elif position[6] < 235:
            pass
        else:
            dobot_m1.stop()
            #judge_joint3 = False
            q_message = QMessageBox.information(self, "Tips", "关节三上超限！", QMessageBox.Ok)
            dobot_m1.MoveToPoint_Joint(position[4], position[5], position[6]-5, position[7])

        if position[7] < -360:
            dobot_m1.stop()
            #judge_joint4 = False
            q_message = QMessageBox.information(self, "Tips", "关节四左超限！", QMessageBox.Ok)
            dobot_m1.MoveToPoint_Joint(position[4] , position[5], position[6], position[7]+5)
        elif position[4] < 360:
            pass
        else:
            dobot_m1.stop()
            #judge_joint4 = False
            q_message = QMessageBox.information(self, "Tips", "关节四右超限！", QMessageBox.Ok)
            dobot_m1.MoveToPoint_Joint(position[4], position[5]-1, position[6], position[7]-5)

        self.xPoint_lineEdit.setText(str(float('%.4f' % position[0])))
        self.yPoint_lineEdit.setText(str(float('%.4f' % position[1])))
        self.zPoint_lineEdit.setText(str(float('%.4f' % position[2])))
        self.rAngle_lineEdit.setText(str(float('%.4f' % position[3])))
        self.joint1_lineEdit.setText(str(float('%.4f' % position[4])))
        self.joint2_lineEdit.setText(str(float('%.4f' % position[5])))
        self.joint3_lineEdit.setText(str(float('%.4f' % position[6])))
        self.joint4_lineEdit.setText(str(float('%.4f' % position[7])))
        QApplication.processEvents()  # 刷新界面
        if bool_getPosition:
            timer_getPosition = Timer(1, self.get_position)
        timer_getPosition.start()



''' # get warning
    global bool_getWarning
    bool_getWarning = True
    def get_warning(self):
        warnMsg = dobot_m1.get_alarm()
        print("Getting alarm")
        print(datetime.datetime.now())
        global timer
        # 重复构造定时器
        if bool_getWarning:
            timer_getWarning = Timer(1, self.get_warning)
        timer_getWarning.start()
        if warnMsg != None:
            print("warnMsg=" + warnMsg)
            # warning.instance().warning_log("warnMsg!")  # 输出到warning日志中'''



if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.setWindowState(Qt.WindowMaximized)
    myWin.show()
    # myWin.showFullScreen()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())


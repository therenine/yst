# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(618, 550)
        MainWindow.setMaximumSize(QtCore.QSize(618, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 601, 600))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 550))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 54, 12))
        self.label.setObjectName("label")
        self.dept_id_text = QtWidgets.QLineEdit(self.groupBox)
        self.dept_id_text.setGeometry(QtCore.QRect(100, 30, 471, 31))
        self.dept_id_text.setObjectName("dept_id_text")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(33, 90, 61, 20))
        self.label_3.setObjectName("label_3")
        self.name_text = QtWidgets.QLineEdit(self.groupBox)
        self.name_text.setGeometry(QtCore.QRect(100, 80, 471, 31))
        self.name_text.setObjectName("name_text")
        self.card_id_text = QtWidgets.QLineEdit(self.groupBox)
        self.card_id_text.setGeometry(QtCore.QRect(100, 130, 471, 31))
        self.card_id_text.setObjectName("card_id_text")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(33, 137, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(33, 185, 61, 20))
        self.label_8.setObjectName("label_8")
        self.mobile_text = QtWidgets.QLineEdit(self.groupBox)
        self.mobile_text.setGeometry(QtCore.QRect(100, 180, 471, 31))
        self.mobile_text.setObjectName("mobile_text")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(33, 235, 61, 20))
        self.label_9.setObjectName("label_9")
        self.address_text = QtWidgets.QLineEdit(self.groupBox)
        self.address_text.setGeometry(QtCore.QRect(100, 230, 471, 31))
        self.address_text.setObjectName("address_text")

        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(33, 285, 61, 20))
        self.label_15.setObjectName("label_15")
        self.doctor_name_text = QtWidgets.QLineEdit(self.groupBox)
        self.doctor_name_text.setGeometry(QtCore.QRect(100, 280, 471, 31))
        self.doctor_name_text.setObjectName("doctor_name_text")

        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(33, 335, 61, 20))
        self.label_16.setObjectName("label_16")

        self.date_time =QtWidgets.QDateEdit(self.groupBox)
        self.date_time.setGeometry(QtCore.QRect(100, 330, 211, 31))
        self.date_time.setObjectName("date_time")

        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(33, 385, 61, 20))
        self.label_18.setObjectName("label_18")
        self.pay_type = QtWidgets.QComboBox(self.groupBox)
        self.pay_type.setGeometry(QtCore.QRect(100, 380, 211, 31))
        self.pay_type.setObjectName("pay_type")
        self.pay_type.addItem("医院现场支付")
        self.pay_type.addItem("微信支付")
        self.pay_type.addItem("支付宝支付")


        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(33, 435, 61, 20))
        self.label_17.setObjectName("label_17")
        self.excute_date_time = QtWidgets.QDateTimeEdit(self.groupBox)
        self.excute_date_time.setGeometry(QtCore.QRect(100, 430, 211, 31))
        self.excute_date_time.setObjectName("date_time")


        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(250, 480, 81, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "约号"))
        self.groupBox.setTitle(_translate("MainWindow", "预约信息"))
        self.label.setText(_translate("MainWindow", "dept_id"))
        self.label_3.setText(_translate("MainWindow", "患者姓名"))
        self.label_4.setText(_translate("MainWindow", "身份证号"))
        self.label_8.setText(_translate("MainWindow", "手机号码"))
        self.label_9.setText(_translate("MainWindow", "家庭地址"))
        self.label_15.setText(_translate("MainWindow", "预约医生"))
        self.label_16.setText(_translate("MainWindow", "预约时间"))
        self.label_18.setText(_translate("MainWindow", "支付方式"))
        self.label_17.setText(_translate("MainWindow", "执行时间"))
        self.date_time.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.excute_date_time.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.pushButton.setText(_translate("MainWindow", "预  约"))


        self.dept_id_text.setText('20072949')
        self.doctor_name_text.setText('郑卫琴')
        #self.card_id_text.setText('420100197810301952')
        #self.name_text.setText('顾纲 ')
        self.address_text.setText('重庆')


        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.excute_date_time.setDateTime(QDateTime.fromString(now_time, 'yyyy-MM-dd hh:mm:ss'))
    def commit_appointment(self):
        pass




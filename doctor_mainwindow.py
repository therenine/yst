import sys
import traceback
import webbrowser
import time
import datetime
from io import StringIO
from threading import Timer
import threading
from urllib import parse
import json


from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic.properties import QtGui, QtCore
from doctor_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread
from PyQt5.QtCore import *


from app_logger import app_logger
from doctor_appointment_schedule import excute, get_duty_week, get_dep_duty_info, is_begin_appointment


logging = app_logger("doctor_mainwindow")


class ShowUiThread(QThread):
    _signal = pyqtSignal(str)
    def __init__(self, parent=None):
        self.excute = excute
        super(ShowUiThread, self).__init__()
    def run(self):
        self._signal.emit('1')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.pushButton.setDisabled(True)

        dept_id_value = self.dept_id_text.text()
        name_value = self.name_text.text()
        card_id_value = self.card_id_text.text()
        mobile_value = self.mobile_text.text()
        address_value = self.address_text.text()
        doctor_name_value = self.doctor_name_text.text()
        date_time_value = self.date_time.text()
        excute_date_time_value = self.excute_date_time.text()

        if dept_id_value and name_value and card_id_value and mobile_value and address_value and\
                doctor_name_value and date_time_value and excute_date_time_value:

            now = datetime.datetime.now()
            temp = datetime.datetime.strptime(excute_date_time_value, '%Y-%m-%d %H:%M:%S')
            beyond_time = temp - now
            QTimer.singleShot(beyond_time.seconds * 1000, self.excute)
        else:
            QMessageBox.warning(self, "信息不完整", self.tr("HI，要完整的填写信息，^_^"))
            self.pushButton.setDisabled(False)



    def excute(self):
        logging.info("开始执行预约任务")
        dept_id_value = self.dept_id_text.text()
        name_value = self.name_text.text()
        card_id_value = self.card_id_text.text()
        mobile_value = self.mobile_text.text()
        address_value = self.address_text.text()
        doctor_name_value = self.doctor_name_text.text()
        date_time_value = self.date_time.text()
        pay_way_text = self.pay_type.currentText()
        pay_way_dict = {'医院现场支付': 'free', '微信支付':'wxsmzf', "支付宝支付":'zfb'}
        pay_way = pay_way_dict.get(pay_way_text)
        try:
            j = 1
            is_ok = False
            for i in range(1, 80):
                if not is_begin_appointment(date_time_value, dept_id_value):
                    logging.debug('等待-----')
                    if i % 10 == 0:
                        j += 1
                    time.sleep(0.5 * j)
                else:
                    is_ok = True
                    break

            if is_ok:
                appointment_result = excute(date_time_value, dept_id_value, doctor_name_value,
                                            name_value, card_id_value, int(mobile_value), address_value, pay_way)

                logging.info("预约结果: %s" % json.dumps(appointment_result))
                if 'success' == appointment_result['type']:
                    if 'free' == pay_way:
                        QMessageBox.information(self, "预约成功", self.tr("预约成功，注意查收短信消息，^_^"))
                        return
                    elif 'wxsmzf' == pay_way:  # 微信扫码支付
                        self.open_webbrowser(('http://www.jkwin.com.cn/ams/pages/jkwin4/reg/wxScan.jsp?code=%s&regId=%s' \
                                            % (parse.quote(appointment_result['payUrl']), appointment_result['regId']))
                                             )
                    else:  #支付宝支付
                        self.open_webbrowser(appointment_result['payUrl'])
                else:
                    QMessageBox.information(self, "预约失败", self.tr("预约失败"))
            else:
                QMessageBox.information(self, "预约失败", self.tr("没有找到号源"))


            #self.open_webbrowser("http://www.jkwin.com.cn/ams/jkwin4Dep.do?method=dep&depId=20072949")
        except Exception:
            fp = StringIO()
            traceback.print_stack(file=fp)
            message = fp.getvalue()
            logging.error("预约异常: %s" % message)

            QMessageBox.warning(self, "出错了", self.tr("出错了，请联系作者吧， Ծ‸Ծ"))

        finally:
            self.pushButton.setDisabled(False)


    def open_webbrowser(self, url):
        webbrowser.open(url, new=0, autoraise=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
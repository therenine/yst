#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import re
import logging
import json


import requests
from pyquery import PyQuery as pq


from app_logger import app_logger



logging = app_logger("doctor_appointment_schedule")



def is_begin_appointment(appointment_date_str, dept_id):
    n_week = get_duty_week(appointment_date_str)
    duty_info = get_dep_duty_info(n_week, dept_id)
    if len(duty_info['staffVOList']) < 1:
        return False
    else:
        return  True



def commit_appointment(duty_id, period_unique_id, nameCn, idCard, callPhone, address, payWay):
    '''
        发送预约请求
    '''
    recoupWay = '2'
    if payWay == 'free':
        recoupWay = ''
    patient_info = {'dutyId': duty_id, 'nameCn': nameCn, 'idCard': idCard, 'callPhone': callPhone,
                    'address': address, 'otherCardNum': '', 'periodUniqueId': period_unique_id,
                    'payWay': payWay,  'syx': False,
                    'recoupWay': recoupWay}

    logging.info("执行预约请求参数为: %s" % json.dumps(patient_info))
    request_url = "http://www.jkwin.com.cn/ams/jkwin4RegPay.do?method=toPay"
    appointment_result = requests.post(request_url, data=patient_info)
    logging.info("执行预约返回结果: %s" % appointment_result.text)
    return appointment_result.json()


def get_period_unique_id(duty_id):
    '''
        根据duty_id获取时间段信息
    '''
    request_url = "http://www.jkwin.com.cn/ams/jkwin4Reg.do"
    duty_time = requests.get(request_url, {'method': 'toFsd', 'dutyId': duty_id})
    d = pq(duty_time.text)
    usable = d(".usable")

    period_unique_id_list = []

    id_re = r"comitTimeForm\('(.*)'\)"
    #id_re = r"(PEcyfey[0-9]*)"
    pattern = re.compile(id_re)
    for i in usable.items():
        att = i.attr("href")
        period_unique_id_list.append(re.search(pattern, att).group(1))
    return period_unique_id_list


def get_duty_week(appointment_date_str):
    '''
    根据日期计算出，n_week，预约信息在第几个页面，从0开始
    '''
    now = datetime.datetime.now()
    now_date = datetime.datetime(now.year, now.month, now.day)
    temp = time.strptime(appointment_date_str,'%Y-%m-%d')
    appointment_date = datetime.datetime(temp.tm_year, temp.tm_mon, temp.tm_mday)

    day = (appointment_date - now_date).days
    n_week = (day // 7 + 1 if day % 7 > 0  else day // 7) - 1
    return n_week



def get_dep_duty_info(n_week, dep_id):
    '''
    nWeek，第几周，以当前时间为第一周，
    查询某个科室的排班
    '''
    schedule_html = requests.post('http://www.jkwin.com.cn/ams/jkwin4Dep.do?method=depDutyList', {"nWeek":n_week,"depId":dep_id})
    return schedule_html.json()


def get_duty_id_by_appointment(appointment_doctor_name, appointment_date_str, duty_info):
    '''
        不在预约时间，返回-1
        本时间段没有排班，返回-9
        时间应该超过30天了，返回-2
        或者没有专家或者没号, 返回-3
    '''

    appointment_date_long = int(time.mktime(time.strptime(appointment_date_str,'%Y-%m-%d')));

    week_list = duty_info['weekStr']
    has_week = False
    for week in week_list:
        if week.find(appointment_date_str) != -1:
            has_week = True
            break
    if not has_week:
        return [-1]

    if not duty_info.get('hasDutyStaffList'):
        return [-2]
    duty_staff_list = duty_info['hasDutyStaffList']
    if not duty_staff_list:
        return [-9]

    duty_remain = []
    for staff_duty in duty_info['staffVOList']:
        if staff_duty['staff']['STAFF_NAME'] == appointment_doctor_name:
            for duty in staff_duty['staffDutyList']:
                duty_date_long = duty['DUTY_DATE_LONGVAR']
                if duty_date_long == int("%d000" % appointment_date_long):
                    if duty['REG_NUM_REMAIN'] > 0:
                        duty_remain.append(duty['DUTY_ID'])

    if duty_remain:
        return duty_remain

    return [-3]



def excute(appointment_date, dep_id, doctor_name, nameCn, idCard, callPhone, address, payWay):
    start_time = int(time.time())

    n_week = get_duty_week(appointment_date)

    appointment_success = False
    duty_info = get_dep_duty_info(n_week, dep_id)
    #logging.info("值班信息: %s" % json.dumps(duty_info))
    get_duty_ids = get_duty_id_by_appointment(doctor_name, appointment_date, duty_info)
    # get_duty_ids = get_duty_id(doctor_name, duty_info)

    if get_duty_ids[0] in [-1. - 2, -3, -9]:
        return {'type': 'error'}

    #特殊情况特殊处理
    if duty_info['org']['HAS_FSD'] == '0':
        appointment_result = commit_appointment(get_duty_ids[0], "", nameCn,
                                                idCard, callPhone, address, payWay)
        end_time = int(time.time())
        logging.info('本次预约花费时间为, %d' % (end_time - start_time))
        return appointment_result

    period_unique_id_list = get_period_unique_id(get_duty_ids[0])
    if period_unique_id_list:
        for period_unique_id in period_unique_id_list:
            appointment_result = commit_appointment(get_duty_ids[0], period_unique_id, nameCn,
                                                    idCard, callPhone, address, payWay)
            if 'success' == appointment_result['type']:
                logging.info('预约时间段为, %s' % period_unique_id)
                end_time = int(time.time())
                logging.info('本次预约花费时间为, %d' % (end_time - start_time))
                return appointment_result


    return {'type': 'error'}




if __name__ == '__main__':

    start_time = int(time.time())
    appointment_date = '2017-11-28'

    is_begin_appointment(appointment_date, 20072949)

    n_week = get_duty_week(appointment_date)
    duty_info = get_dep_duty_info(n_week, 20072949)
    get_duty_ids = get_duty_id_by_appointment('简嘉', appointment_date, duty_info)

    appointment_success = False
    if get_duty_ids[0] not in [-1. -2, -3, -9]:
        period_unique_id_list = get_period_unique_id(get_duty_ids[0])
        if period_unique_id_list:
            for period_unique_id in period_unique_id_list:
                appointment_result = '' #commit_appointment(get_duty_ids[0], period_unique_id)
                if 'success' == appointment_result:
                    appointment_success = True
                    print('预约时间段为, %s' % period_unique_id)
                    break


    if appointment_success:
        print('预约成功')

    end_time = int(time.time())
    print('本次预约花费时间为, %d' % (end_time - start_time))

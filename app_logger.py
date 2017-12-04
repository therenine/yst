#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

def app_logger(log_name):
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(os.path.join(os.getcwd(), 'app.log'))
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:11:02 2020

@author: qtckp
"""


import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')



import logzero
from logzero import logger
 
# 3 rotations, each with a maximum filesize of 1MB:
logzero.logfile("logfile.log", disableStderrLogger=0, encoding = 'utf-8')
 
logger.info('سلام')



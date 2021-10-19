# -*- coding:utf-8 -*-

import logging.config
from conf.global_var import PROJECT_PATH

# read logger config file
logging.config.fileConfig(PROJECT_PATH + '/conf/logger.ini')

# select logger object
logger = logging.getLogger("loggerObj")

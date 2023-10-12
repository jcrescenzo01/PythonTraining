import logging


"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

import helper
"""
"""
# setting different log handlers
logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('../file.log')

# level and format
stream_h.setLevel((logging.WARNING))
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')

# RECCOMENDATION: Rewatch 2:20:00 - 2:42:41 in https://www.youtube.com/watch?v=HGOBQPFzWKo&t=4058s
# because logging is somewhat in comprehensible to me
"""

import logging.config #logging.conf file I made

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')

# all not functional, rewatch video
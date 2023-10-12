# python has a prebuilt logging module
"""
import logging
logging.debug('This is a debug message')        # level 1
logging.info('This is an info message')         # level 2
logging.warning('This is a warning message')    # level 3 prints
logging.error('This is an error message')       # level 4 prints
logging.critical('This is a critical message')  # level 5 prints
"""
# only warning, error, and critical are printed b/c
# by default, only messages with level warning or above are printed
# we can change this by setting the basic configuration
"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
    # level is set to logging.debug, meaning debug and above levels print
    # log record attributes (format):
        # %(asctime)s - logs time of occurence
        # %(name)s - logs name of the logger
        # %(levelname)s - logs name of the level (debug, info, warning, etc)
        # %(message)s - logs message being sent, for palcement's sake
    # datefmt effects the time logging of %(asctime)s
        # %m/%d/%Y %H:%M:%S = month/day/year hour:minute:second
    # all this is found in official python documentation
logging.debug('This is a debug message')        # level 1
logging.info('This is an info message')         # level 2
logging.warning('This is a warning message')    # level 3 prints
logging.error('This is an error message')       # level 4 prints
logging.critical('This is a critical message')  # level 5 prints
"""
# if we want to make our own log in different modules, its best to not use the root logger above
import logging
logger = logging.getLogger(__name__) #__name__ global variable is good practice, taking the name of the module, which is logger
logger.info('hello from helper')

import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s | [%(levelname)s] | (%(filename)s) | %(funcName)s(%(lineno)d) | %(message)s'
            ,'datefmt':'%Y-%m-%d %H:%M:%S'
            },
        
    },
    
    
    
    
    "json": {  # The formatter name
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",  # The class to instantiate!
            # Json is more complex, but easier to read, display all attributes!
            "format": """
                    asctime: %(asctime)s
                    created: %(created)f
                    filename: %(filename)s
                    funcName: %(funcName)s
                    levelname: %(levelname)s
                    levelno: %(levelno)s
                    lineno: %(lineno)d
                    message: %(message)s
                    module: %(module)s
                    msec: %(msecs)d
                    name: %(name)s
                    pathname: %(pathname)s
                    process: %(process)d
                    processName: %(processName)s
                    relativeCreated: %(relativeCreated)d
                    thread: %(thread)d
                    threadName: %(threadName)s
                    exc_info: %(exc_info)s
                """,
            "datefmt": "%Y-%m-%d %H:%M:%S",  # How to display dates
        },

    'handlers': {
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default_formatter',
            'filename': '/home/administrator/Global/log/ws_log.log',
            'mode': 'a',
            "level": "DEBUG", 
            'maxBytes': 1048576,
            'backupCount': 10

        },
        
    },
     "json": {  # The handler name
            "formatter": "json",  # Refer to the formatter defined above
            "class": "logging.StreamHandler",  # OUTPUT: Same as above, stream to console
            "stream": "ext://sys.stdout",
        },

    'loggers': {
        'my_logger': {
            'handlers': ['file_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
    '__main__': {  # if __name__ == '__main__'
            'handlers': ['file_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
}


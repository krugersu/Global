import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s | [%(levelname)s] | (%(filename)s).|%(funcName)s(%(lineno)d) | %(message)s'
            ,'datefmt':'%Y-%m-%d %H:%M:%S'
            },
    },

    'handlers': {
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default_formatter',
            'filename': '/home/administrator/Global/log/ws_log.log',
            'mode': 'a',
            'maxBytes': 1048576,
            'backupCount': 10

        },
        
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


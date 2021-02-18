import os
import logging.config
dir_path = os.path.dirname(os.path.realpath(__file__))

logging_config_file = '''
[loggers]
keys=root

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=consoleFormatter,fileFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler,fileHandler

[handler_consoleHandler]
class=StreamHandler
level=ERROR
formatter=consoleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=INFO
formatter=fileFormatter
args=('log.txt',)

[formatter_consoleFormatter]
format=%(asctime)-8s.%(msecs)03d %(levelname)-8s %(name)s:%(lineno)-3s %(message)s
datefmt=%H:%M:%S

[formatter_fileFormatter]
format=%(asctime)-16s %(levelname)-8s %(filename)-s:%(lineno)-3s %(message)s
datefmt=%Y-%m-%d %H:%M
'''

with open('./logging_config.cnf', 'w') as config_file:
    config_file.write(logging_config_file)

basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
logging.config.fileConfig('./logging_config.cnf')
logger = logging.getLogger(__name__)

import configparser

config = configparser.ConfigParser()
print(config.sections())
print(config.read("config.ini"))
print(config.sections())
logging_config = config['LOGGING']
print(logging_config)
print(logging_config.get("LOG_LEVEL"))

# []
# ['config.ini']
# ['LOGGING']
# <Section: LOGGING>
# DEBUG
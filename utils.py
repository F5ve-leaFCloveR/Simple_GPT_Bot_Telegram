import configparser
import sys

def config_reader(head, key):
    config = configparser.ConfigParser()
    try: # попытка чтения cfg файла
        config.read('conf.cfg')
    except FileNotFoundError:
        print('Error: conf.cfg file not found')
        sys.exit(1)
    except configparser.Error as e:
        print(f'Error parsing conf.cfg file: {e}')
        sys.exit(1)


    try: # получение самого key из cfg файла
        key = config[head][key]
        return key
    except KeyError:
        print('Error: key not found in conf.cfg file')
        sys.exit(1)
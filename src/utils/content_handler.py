from abc import ABC, abstractmethod
from typing import Set

class ContentHandler(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def assert_exist(self, vocab:str) -> bool:
        pass

    @abstractmethod
    def add_new_vocab(self, vocab:str) -> bool:
        pass

    @abstractmethod
    def get_content(self, vocab:str) -> str:
        pass
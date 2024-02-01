from .config import EXPLAINATION_FLOLDER
import os

class ExplainationIOHandler:
    def __init__(self):
        pass

    def save(self, word:str, explaination:str):
        assert os.path.exists(EXPLAINATION_FLOLDER)
        with open(f"{EXPLAINATION_FLOLDER}/{word}.md", "w") as file:
            file.write(explaination)
    
    def fetch(self, word:str):
        assert os.path.exists(f"{EXPLAINATION_FLOLDER}/{word}.md")
        with open(f"{EXPLAINATION_FLOLDER}/{word}.md", "r") as file:
            return file.read()
from .config import AUDIO_FOLDER, EXPLAINATION_FLOLDER

class CacheManager:
    def __init__(self):
        self.cache = set()

    def fetch(self):
        # fetch from the cache folder
        # traverse the folder and add the word to the cache
        # for example, if the word is "hello", then AUDIO_FOLDER will have hello.mp3 and EXPLAINATION_FLOLDER will have hello.md
        # so we will add "hello" to the cache
        import os 
        for file in os.listdir(EXPLAINATION_FLOLDER):
            word = file.split(".")[0]
            self.add(word)
        for file in os.listdir(AUDIO_FOLDER):
            word = file.split(".")[0]
            assert self.is_cached(word) # if the word is not cached, then it is a bug

    def add(self, word:str):
        self.cache.add((word))
    
    def is_cached(self, word:str):
        return word in self.cache
        
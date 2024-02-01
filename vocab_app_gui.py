from src.vocab_explainer import VocabExplainer
from src.cache_manager import CacheManager
from src.explaination_io_handler import ExplainationIOHandler
from src.audio_handler import AudioHandler

class VocabAppGUI:
    def __init__(self):
        self.cache_manager = CacheManager()
        self.cache_manager.fetch()
        self.vocab_explainer = VocabExplainer()
        self.explaination_io_handler = ExplainationIOHandler()
        self.audio_handler = AudioHandler()

    def run(self, word:str):
        if self.cache_manager.is_cached(word):
            result = self.explaination_io_handler.fetch(word)
        else:
            result = self.vocab_explainer.explain(word)
            self.audio_handler.save(word)
            self.explaination_io_handler.save(word, result)
            self.cache_manager.add(word)
        return result, self.audio_handler.get_path(word)
from src.vocab_explainer import VocabExplainer
from src.md_viewer import MarkdownViewer
from src.cache_manager import CacheManager
from src.explaination_io_handler import ExplainationIOHandler
from src.audio_handler import AudioHandler

class VocabApp:
    def __init__(self):
        self.cache_manager = CacheManager()
        self.cache_manager.fetch()
        self.vocab_explainer = VocabExplainer()
        self.explaination_io_handler = ExplainationIOHandler()
        self.audio_handler = AudioHandler()

    def run(self):
        run = True
        while run:
            action = input("Choose Action\n 1. Explain a word \n 2. Exit \n")
            if action == "1":
                word = input("Enter the word: ")
                if self.cache_manager.is_cached(word):
                    result = self.explaination_io_handler.fetch(word)
                else:
                    result = self.vocab_explainer.explain(word)
                    self.audio_handler.save(word)
                    self.explaination_io_handler.save(word, result)
                    self.cache_manager.add(word)
                MarkdownViewer.view(result)
                play = input("Play the word audio? (y/n): ")
                if play == "y":
                    self.audio_handler.play(word)
            elif action == "2":
                run = False
from ..utils.cache_manager import CacheManager
from ..utils.explaination_handler import ExplainationHandler
from ..utils.audio_handler import AudioHandler
from ..utils.llm_handler import GeminiProHandler
from ..utils.prompt_formator import DefaultPromptFormator
from .md_viewer import MarkdownViewer
from .audio_player import AudioPlayer

class CliController:
    def __init__(self):
        self.cache_manager = CacheManager()
        explaination_handler = ExplainationHandler()
        explaination_handler.set_llm_handler(GeminiProHandler())
        explaination_handler.set_prompt_formator(DefaultPromptFormator())
        self.cache_manager.add_content_handler(explaination_handler)
        self.cache_manager.add_content_handler(AudioHandler())
        
    def run(self):
        run = True
        while run:
            action = input("Choose Action\n 1. Explain a word \n 2. Exit \n")
            if action == "1":
                word = input("Enter the word: ")
                result_list = self.cache_manager.get_content(word)
                MarkdownViewer.view(result_list[0])
                play = input("Play the word audio? (y/n): ")
                if play == "y":
                    AudioPlayer.play(result_list[1])
            elif action == "2":
                run = False
from ..utils.cache_manager import CacheManager
from ..utils.explaination_handler import ExplainationHandler
from ..utils.audio_handler import AudioHandler
from ..utils.llm_handler import GeminiProHandler
from ..utils.prompt_formator import DefaultPromptFormator

class GuiController:
    def __init__(self):
        self.cache_manager = CacheManager()
        explaination_handler = ExplainationHandler()
        explaination_handler.set_llm_handler(GeminiProHandler())
        explaination_handler.set_prompt_formator(DefaultPromptFormator())
        self.cache_manager.add_content_handler(explaination_handler)
        self.cache_manager.add_content_handler(AudioHandler())
        
    def run(self, vocab:str) -> list[str]:
        return self.cache_manager.get_content(vocab)
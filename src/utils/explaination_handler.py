from .prompt_formator import PromptFormator, DefaultPromptFormator
from .content_handler import ContentHandler
from .llm_handler import LLMHandler
from ..config import EXPLAINATION_FLOLDER
import os

class ExplainationHandler(ContentHandler):
    def __init__(self):
        super().__init__()
        self.llm_handler: LLMHandler = None 
        self.prompt_formator: PromptFormator = None 

    def set_llm_handler(self, llm_handler: LLMHandler) -> None:
        self.llm_handler = llm_handler

    def set_prompt_formator(self, prompt_formator: PromptFormator) -> None:
        self.prompt_formator = prompt_formator

    def save_content(self, vocab:str, explaination:str) -> None:
        with open(f"{EXPLAINATION_FLOLDER}/{vocab}.md", "w") as file:
            file.write(explaination)

    def assert_init(self) -> bool:
        return self.llm_handler is not None and self.prompt_formator is not None

    def add_new_vocab(self, vocab:str) -> bool:
        assert self.assert_init()
        assert not self.assert_exist(vocab)
        try:
            prompt = self.prompt_formator.format(vocab)
            explaination = self.llm_handler.invoke(prompt)
            self.save_content(vocab, explaination)
            return True
        except:
            return False

    def assert_exist(self, vocab:str) -> None:
        assert self.assert_init()
        return os.path.exists(f"{EXPLAINATION_FLOLDER}/{vocab}.md")

    def get_content(self, vocab:str) -> str:
        assert self.assert_init()
        assert self.assert_exist(vocab)
        with open(f"{EXPLAINATION_FLOLDER}/{vocab}.md", "r") as file:
            return file.read()

from .content_handler import ContentHandler
from .explaination_handler import ExplainationHandler

class CacheManager:
    def __init__(self) -> None:
        self.content_handlers: list[ContentHandler] = []
    
    def add_content_handler(self, content_handler: ContentHandler) -> None:
        self.content_handlers.append(content_handler)

    def add_new_vocab(self, vocab:str) -> bool:
        for content_handler in self.content_handlers:
            if content_handler.assert_exist(vocab):
                continue            
            if not content_handler.add_new_vocab(vocab):
                return False
        return True
            
    def get_content(self, vocab:str) -> list[str]:
        return_list = []
        for content_handler in self.content_handlers:
            if content_handler.assert_exist(vocab):
                return_list.append(content_handler.get_content(vocab))
            else:
                assert self.add_new_vocab(vocab)
                return_list.append(content_handler.get_content(vocab))
        assert len(return_list) == len(self.content_handlers)
        return return_list
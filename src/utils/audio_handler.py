from ..config import AUDIO_FOLDER
from gtts import gTTS
import os
from .content_handler import ContentHandler

class AudioHandler(ContentHandler):
    def __init__(self):
        assert os.path.exists(AUDIO_FOLDER)

    def assert_exist(self, vocab:str) -> bool:
        return os.path.exists(f"{AUDIO_FOLDER}/{vocab}.mp3")

    def add_new_vocab(self, vocab:str) -> bool:
        assert not self.assert_exist(vocab)
        try:
            tts = gTTS(vocab)
            tts.save(f'{AUDIO_FOLDER}/{vocab}.mp3')
            return True
        except:
            return False

    def get_content(self, vocab:str) -> str:
        assert self.assert_exist(vocab)
        return f"{AUDIO_FOLDER}/{vocab}.mp3"
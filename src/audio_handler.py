from .config import AUDIO_FOLDER
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

class AudioHandler:
    def __init__(self):
        pass

    def save(self, word:str):        
        tts = gTTS(word)
        assert os.path.exists(AUDIO_FOLDER)
        tts.save(f'{AUDIO_FOLDER}/{word}.mp3')

    def play(self, word:str):
        assert os.path.exists(f"{AUDIO_FOLDER}/{word}.mp3")
        song = AudioSegment.from_mp3(f"{AUDIO_FOLDER}/{word}.mp3")
        play(song)
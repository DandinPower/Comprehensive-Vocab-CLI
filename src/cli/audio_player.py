from pydub import AudioSegment
from pydub.playback import play
import os 
from ..config import AUDIO_FOLDER

class AudioPlayer:
    @staticmethod
    def play(path:str):
        assert os.path.exists(path)
        song = AudioSegment.from_mp3(path)
        play(song)
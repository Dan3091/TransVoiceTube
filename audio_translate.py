from pytube import YouTube
import os
from speech_recognition import *
from pydub import AudioSegment
from gtts import gTTS
from deep_translator import GoogleTranslator


txt = ""

def download_video(url_video):
    """
    This function take the url as an argument download the audio
    from the specified url video link and return True if it succeeds
    or False otherwise.
    """

    try:
        yt = YouTube(url_video)
        stream = yt.streams.get_audio_only()
        stream.download(filename="AudioTrack.mp4")
        return True
    except:
        return False

def convert_mp4_to_wav():
    """
    The function take the recently downloaded file that is in *.mp4
    format and converts it in a *.wav format.
    """

    try:
        audio = AudioSegment.from_file("AudioTrack.mp4", format="mp4")
        audio.export("audio.wav", format="wav")
        os.remove("AudioTrack.mp4")
        return True
    except:
        return False
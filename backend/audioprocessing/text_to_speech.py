# backend/audio_processing/text_to_speech.py
# pip install TTS
from TTS.api import TTS
import os

class TextToSpeech:
    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

    def synthesize(self, text, output_path="output.wav"):
        self.tts.tts_to_file(text=text, file_path=output_path)
        return output_path


if __name__ == "__main__":
    tts = TextToSpeech()
    path = tts.synthesize("Welcome to the annual tech fest. I’m your AI virtual host!")
    print("Audio saved at:", path)

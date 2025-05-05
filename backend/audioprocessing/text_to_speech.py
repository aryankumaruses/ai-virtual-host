# backend/audio_processing/text_to_speech.py

from TTS.api import TTS
from backend.audio_processing.audio_utils import get_audio_duration

class TextToSpeech:
    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

    def synthesize(self, text, output_path="output.wav"):
        self.tts.tts_to_file(text=text, file_path=output_path)
        duration = get_audio_duration(output_path)
        print(f"Audio generated at {output_path} with duration: {duration:.2f} seconds")
        return output_path


if __name__ == "__main__":
    tts = TextToSpeech()
    path = tts.synthesize("Welcome! I’m your AI virtual emcee.")

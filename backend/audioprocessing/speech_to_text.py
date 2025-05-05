# backend/audio_processing/speech_to_text.py

import whisper
from backend.audio_processing.audio_utils import convert_to_wav, is_valid_audio

class SpeechToText:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        if not is_valid_audio(audio_path):
            raise ValueError("Invalid or corrupted audio file.")

        wav_path = convert_to_wav(audio_path)
        result = self.model.transcribe(wav_path)
        return result['text']


if __name__ == "__main__":
    stt = SpeechToText()
    text = stt.transcribe("sample_audio.mp3")  # Any format supported by pydub
    print("Transcribed Text:", text)


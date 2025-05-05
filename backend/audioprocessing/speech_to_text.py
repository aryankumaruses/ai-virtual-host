# backend/audio_processing/speech_to_text.py

import whisper

class SpeechToText:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result['text']


if __name__ == "__main__":
    stt = SpeechToText()
    text = stt.transcribe("sample_audio.wav")
    print("Transcribed Text:", text)


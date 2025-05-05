# backend/audio_processing/audio_utils.py

import wave
import contextlib
import os
from pydub import AudioSegment

def get_audio_duration(audio_path):
    with contextlib.closing(wave.open(audio_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

def convert_to_wav(input_path, output_path="converted.wav"):
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    return output_path

def is_valid_audio(file_path):
    try:
        AudioSegment.from_file(file_path)
        return True
    except Exception:
        return False

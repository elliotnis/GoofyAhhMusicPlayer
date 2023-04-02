import os
import librosa
import numpy as np
import sounddevice as sd
class Audio:
    def __init__(self):
        self.y, self.sr = librosa.load(os.getcwd() + r"\testsounds\nokia-ringtone-arabic.mp3")

    def play_audio(self,start, amplitude = 0, pitch=0, speed = 1):
        y_pitch = librosa.effects.pitch_shift(self.y, sr=self.sr, n_steps=float(pitch))
        self.y_mod = librosa.util.normalize(y_pitch)
        rate = speed
        self.y_mod = librosa.effects.time_stretch(self.y_mod, rate = rate)
        self.y_mod = self.y_mod[int(start/speed):]
        sd.play(self.y_mod*amplitude, self.sr)


    def getLength(self):
        return len(self.y)
    def stop_audio(self):
        sd.stop()
    def getSamplingRate(self):
        return self.sr

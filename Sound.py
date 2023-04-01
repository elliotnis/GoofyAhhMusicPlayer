import librosa
import numpy as np
import sounddevice as sd
class Audio:
    def __init__(self):
        self.y, self.sr = librosa.load(r'C:\Users\ellio\Documents\GoofyAhhMusicPlayer\testsounds\piano-C4.wav')
    def modify_amplitude(self, value):
            y_amp = self.y * float(value)
            self.y_mod = librosa.util.normalize(y_amp)

    def modify_pitch(self, value):
            y_pitch = librosa.effects.pitch_shift(self.y, self.sr, n_steps=float(value))
            self.y_mod = librosa.util.normalize(y_pitch)

    def play_audio(self):
        sd.play(self.y, self.sr, blocking=True)
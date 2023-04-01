import librosa
import numpy as np
import sounddevice as sd
class Audio:
    def __init__(self):
        self.y, self.sr = librosa.load(r'C:\Users\ellio\Documents\GoofyAhhMusicPlayer\testsounds\piano-C4.wav')

    def play_audio(self,start, amplitude = 0, pitch=0):
        y_pitch = librosa.effects.pitch_shift(self.y, sr=self.sr, n_steps=float(pitch))
        self.y_mod = librosa.util.normalize(y_pitch)
        self.y_mod = self.y_mod[start:]
        sd.play(self.y_mod*amplitude, self.sr)

    def getLength(self):
        return len(self.y)
    def stop_audio(self):
        sd.stop()


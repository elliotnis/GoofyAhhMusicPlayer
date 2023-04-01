import tkinter as tk
import librosa
import numpy as np
import IPython.display as ipd

class AudioGUI:
    def __init__(self, audio_file):
        self.y, self.sr = librosa.load(audio_file)


        # Create amplitude scale
        self.amp_label = tk.Label(self.root, text="Amplitude:")
        self.amp_label.pack()
        self.amp_scale = tk.Scale(self.root, from_=0, to=4, orient=tk.HORIZONTAL, resolution=0.1, command=self.modify_amplitude)
        self.amp_scale.pack()

        # Create pitch shift scale
        self.pitch_label = tk.Label(self.root, text="Pitch shift:")
        self.pitch_label.pack()
        self.pitch_scale = tk.Scale(self.root, from_=-12, to=12, orient=tk.HORIZONTAL, command=self.modify_pitch)
        self.pitch_scale.pack()

        # Create play button
        self.play_button = tk.Button(self.root, text="Play", command=self.play_audio)
        self.play_button.pack()

#     def modify_amplitude(self, value):
#         y_amp = self.y * float(value)
#         self.y_mod = librosa.util.normalize(y_amp)

#     def modify_pitch(self, value):
#         y_pitch = librosa.effects.pitch_shift(self.y, self.sr, n_steps=float(value))
#         self.y_mod = librosa.util.normalize(y_pitch)

#     def play_audio(self):
#         ipd.display(ipd.Audio(self.y_mod, rate=self.sr))

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    audio_gui = AudioGUI('test.wav')
    audio_gui.run()
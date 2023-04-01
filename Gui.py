from tkinter import *
from Sound import Audio
import threading
audio = Audio()
root = Tk()
root.title("GUITest")
class GUI:
    def __init__(self, root):

        # Placeholder commands
        def modify_amplitude(self):
            print("test")
        def modify_pitch(self):
            print("Pitch modified")
        def play_audio():
            thread = threading.Thread(target=audio.play_audio)
            thread.start()
            
        # Create amplitude scale
        self.amp_label = Label(root, text="Amplitude:")
        self.amp_label.pack()
        self.amp_scale = Scale(root, from_=0, to=4, orient=HORIZONTAL, resolution=0.1, command=modify_amplitude)
        self.amp_scale.pack()

        # Create pitch shift scale
        self.pitch_label = Label(root, text="Pitch shift:")
        self.pitch_label.pack()
        self.pitch_scale = Scale(root, from_=-12, to=12, orient=HORIZONTAL, command=modify_pitch)
        self.pitch_scale.pack()
        # Create Play Button
        self.play_button = Button(root, text="Play", command=play_audio)
        self.play_button.pack()

        # Duration slider
        self.slider = Scale(root, from_=0, to=100, orient='horizontal', length=300)
        self.slider.pack()

        def modify_time(value):
            print(value)

        self.slider.config(command = lambda value: modify_time(self.slider.get()))




g = GUI(root)

root.mainloop()

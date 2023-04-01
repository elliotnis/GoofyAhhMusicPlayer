from tkinter import *

root = Tk()
root.title("GUITest")
class GUI:
    def __init__(self, root):

        # Placeholder commands
        def modify_amplitude(self):
            print("Amplitude modified")
        def modify_pitch(self):
            print("Pitch modified")
        def play_audio(self):
            print("Play")
        
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

        # Create play button
        self.play_button = Button(root, text="Play", command=play_audio)
        self.play_button.pack()



g = GUI(root)

root.mainloop()

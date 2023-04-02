from tkinter import *
from Sound import Audio
import threading
import time
audio = Audio()
root = Tk()
root.title("Audio")
class GUI:
    def __init__(self, root):
        self.isPlaying = False
        self.slider_value = IntVar(value = 0)
        self.amp_value = DoubleVar(value = 0.0)
        self.pitch_value = DoubleVar(value = 0.0)
        self.speed_value = DoubleVar(value = 0.0)
        self.current_speed = DoubleVar(value = 0.0)
        # Play_audio command
        def play_audio():
            if self.isPlaying == False:
                self.isPlaying = True
                self.audio = Audio()
                thread = threading.Thread(target=self.audio.play_audio, args=[self.slider_value.get(),self.amp_value.get(),self.pitch_value.get(),self.speed_value.get()])
                thread.start()
                self.current_speed = self.speed_value.get()
                print(self.current_speed.get())

            else:
                self.isPlaying = False
                self.audio.stop_audio()

            
        # Create Volume scale
        self.amp_label = Label(root, text="Volume:")
        self.amp_label.pack()
        self.amp_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, resolution=0.1, variable = self.amp_value)
        self.amp_scale.set(1)
        self.amp_scale.pack()

        # Create pitch shift scale
        self.pitch_label = Label(root, text="Pitch shift:")
        self.pitch_label.pack()
        self.pitch_scale = Scale(root, from_=-10, to=10, orient=HORIZONTAL, resolution=0.05, variable = self.pitch_value)
        self.pitch_scale.set(0)
        self.pitch_scale.pack()


        # Create Speed Scale
        self.speed_label = Label(root, text="Speed control:")
        self.speed_label.pack()
        self.speed_scale = Scale(root, from_=0, to=10, orient=HORIZONTAL, resolution=0.05, variable = self.speed_value)
        self.speed_scale.set(1)
        self.speed_scale.pack()

        # Create Play Button
        self.play_button = Button(root, text="Play", command=play_audio)
        self.play_button.pack()

        # Duration slider
        self.slider = Scale(root, from_=0, to= audio.getLength(), orient='horizontal', length=300, variable=self.slider_value, showvalue = True)
        self.slider.pack()
        self.slider.config(showvalue = False)
        # Time label
        self.time_label = Label(root, text=0)
        self.time_label.place(x=0,y=195)
        def modify_time(value):
                self.time_label.destroy()
                samplesperpixel = audio.getLength()/300
                self.time_label = Label(root, text=str(int(value/audio.getSamplingRate())))
                self.time_label.place(x=self.slider_value.get()/(samplesperpixel/0.94),y=195)
        
        def incrementtime(self):
            while(True):
                if self.isPlaying == True:
                    self.slider.set(self.slider_value.get()+audio.getSamplingRate())
                    time.sleep(1/self.current_speed)                

                elif self.isPlaying == False and self.slider_value.get() == audio.getLength():
                    self.slider.set(0)
        thread2 = threading.Thread(target = incrementtime, args=[self])
        thread2.start()
        self.slider.config(command = lambda value: modify_time(self.slider.get()))




g = GUI(root)

root.mainloop()
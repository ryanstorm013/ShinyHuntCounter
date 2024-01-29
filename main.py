from playsound import playsound
import tkinter as tk
import customtkinter as ctk
from PIL import Image
from myFrame import *
from segButton import *
from tab import *


# import ttkbootstrap as ttk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
ctk.set_window_scaling(1)

        
class App(ctk.CTk, tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("700x400")
        self.grid_rowconfigure((0, 3), weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1) 
        

        self.my_frame = TabViewTime(self)
        self.my_frame.grid(row=1, column=0, padx=20, pady=0, sticky="w")
        #button
        
        
        self.other_frame = MyFrame(self)
        self.other_frame.grid(row=1, column=1, padx=0, pady=0)
        
        
        
        segmented_button()
        # reset()
        
        



app = App()
app.title('Shny Counter')
playsound('sound effects\GUI save game.wav')
app.resizable(0, 0)
app.mainloop()


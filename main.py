import tkinter as tk
from tkinter import colorchooser
import customtkinter as ctk
from PIL import Image
from myFrame import *
from segButton import *
from datetime import datetime

# import ttkbootstrap as ttk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
ctk.set_window_scaling(1)
        
class TimerTime(ctk.CTkTabview):
        def __init__(self, taby): 
            super().__init__(taby)

            custom_font =("Times",30,'bold')
            custom_font2 =("Times",20,'bold')

            self.running = False    #Defailt Running
            self.start_time = None  #Default Start Time
            

            self.button4 = ctk.CTkButton(taby, text="Start", font=custom_font2, width=40, height=35, command=self.stopngo)
        
            self.button4.place(relx=0.5, rely=1.0, anchor=tk.S)

            self.string_var = ctk.StringVar(value="black")

            self.label2 = ctk.CTkLabel(taby,
                                    font=custom_font,
                                    text="0:00:00.000",
                                    width=250,
                                    height=150,
                                    fg_color=("black", "white"),
                                    text_color=("white", "black")
                                    )
            self.label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            self.text_var = ctk.IntVar()

            # button5 = ctk.CTkButton(master=None, text="Reset", height=35)
            # button5.grid(row=3, column=0, padx=20, pady=20)

        

        def stopngo(self):
            if not self.running:
                self.start_time = datetime.now()
                self.running = True
                self.button4.configure(text="Stop")
                self.update_time()
            else:
                self.running = False
                self.button4.configure(text="Start")

        def update_time(self):
            if self.running:
                elapsed = datetime.now() - self.start_time
                formatted_time = self.format_time(elapsed)
                self.label2.configure(text=formatted_time)
                self.after(50, self.update_time)
        
        def update_display(self):
            self.label2.configure(text="0:00:00.000")

        def format_time(self, elapsed):
            total_seconds = elapsed.total_seconds()
            minutes, seconds = divmod(total_seconds, 60)
            hours, minutes = divmod(minutes, 60)
            milliseconds = int((total_seconds - int(total_seconds)) * 1000)
            formatted_time = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{milliseconds:03d}"
            return formatted_time
        

        




        
# class PowerCounter(ctk.CTkTabview):
#     pass








class TabViewTime(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        custom_font =("Times",50,'bold')
        custom_font2 =("Times",20,'bold')
        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=(20, 20), pady=0, sticky="sn")
        
        self.add("Counter")
        self.add("Timer")
        
        def color():
            my_color = colorchooser.askcolor("black")
            valueStore = my_color[1]

            try: 
                self.label.configure(fg_color=valueStore)
                # self.label2.configure(fg_color=valueStore)
            except ValueError:
                pass

        def plus():
            current_value = self.text_var.get()
            self.text_var.set(current_value + 1)
            self.label.configure(text=str(self.text_var.get()))
            
            
        def minus():
            current_value = self.text_var.get()
            self.text_var.set(current_value - 1)
            self.label.configure(text=str(self.text_var.get()))

        

        self.text_var = ctk.IntVar()

        self.label = ctk.CTkLabel(master=self.tab("Counter"),                       
                               font=custom_font,
                               text=str(self.text_var.get()),
                               width=250,
                               height=150,
                               fg_color=("black", "white"),
                               text_color=("white", "black")
                                )
        self.label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
                
        self.button = ctk.CTkButton(self.tab("Counter"), text="+", font=custom_font2, width=40, height=35,
                               command=plus)

        self.button2 = ctk.CTkButton(self.tab("Counter"), text="-", font=custom_font2, width=40, height=35,
                                command=minus)
        self.button.place(relx=0.8, rely=1.0, anchor=tk.SW)
        self.button2.place(relx=0.2, rely=1.0, anchor=tk.SE)

        #Color 
        button3 = ctk.CTkButton(None, text="Color", font=custom_font2, width=40, height=35, command=color)

        
        button3.place(relx=0.5, rely=1.0, anchor=tk.S)


        self.my_timer = TimerTime(self.tab("Timer"))

        button5 = ctk.CTkButton(master=None, text="Reset", height=35)
        button5.grid(row=2, column=0, padx=20, pady=20)



    
        
        

        




        
class App(ctk.CTk, tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("650x400")
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
app.resizable(0, 0)

app.mainloop()


import tkinter as tk
import customtkinter as ctk
from tkinter import colorchooser
from datetime import datetime

class TabViewTime(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        custom_font =("Times",50,'bold')
        custom_font2 =("Times",20,'bold')
        # add widgets onto the frame, for example:

        
        my_tabs = ["Counter", "Timer"]

        counterTab = self.add(my_tabs[0])
        timeTab = self.add(my_tabs[1])
        
        
        def color():
            my_color = colorchooser.askcolor("black")
            valueStore = my_color[1]
            # print(my_color)
            try:
                if valueStore == '#000000' or valueStore == '#ffffff':
                    default()
                else:
                    self.tabCounter.configure(fg_color=valueStore)
                    self.tabTime.configure(fg_color=valueStore)
            except ValueError:
                pass
        
        def default():
            self.tabCounter.configure(fg_color=("black", "white"), text_color=("white", "black"))
            self.tabTime.configure(fg_color=("black", "white"), text_color=("white", "black"))

        def transparent():
            self.tabCounter.configure(fg_color=("transparent"), text_color=("black", "white"))
            self.tabTime.configure(fg_color=("transparent"), text_color=("black", "white"))

        def plus():
            current_value = self.text_var.get()
            self.text_var.set(current_value + 1)
            self.tabCounter.configure(text=str(self.text_var.get()))
            
            
        def minus():
            current_value = self.text_var.get()
            if current_value == 0:
                self.text_var.set(0)
            else:
                self.text_var.set(current_value - 1)
                self.tabCounter.configure(text=str(self.text_var.get()))

            
        self.text_var = ctk.IntVar()

        self.tabCounter = ctk.CTkLabel(master=counterTab,
                                                  
                               font=custom_font,
                               text=str(self.text_var.get()),
                               width=250,
                               height=150,
                               fg_color=("black", "white"),
                               text_color=("white", "black")
                                )


        self.tabCounter.grid(row=0, column=0, padx=30, pady=20)
                
        self.buttonPlus = ctk.CTkButton(self.tab("Counter"), text="+", font=("Times",30,'bold'), width=40, height=25,
                               command=plus, fg_color="#5cb85c", text_color="black" )

        self.buttonMinus = ctk.CTkButton(self.tab("Counter"), text="-", font=("Times",30,'bold'), width=40, height=25,
                                command=minus, fg_color="#d9534f", text_color="black" )
        

        self.buttonPlus.grid(row=1, column=0, padx=30, pady=0)
        self.buttonPlus.place(relx=0.9, rely=0.75, anchor=tk.SE)

        self.buttonMinus.grid(row=1, column=0, padx=0, pady=0)
        self.buttonMinus.place(relx=0.1, rely=0.75, anchor=tk.SW)

        counterReset = ctk.CTkButton(counterTab, text="Reset", height=35, command= self.reset)
        counterReset.grid(row=2, column=0, padx=0, pady=35)








        self.running = False    #Defailt Running
        self.start_time = None  #Default Start Time
        self.pause_time = None

        self.stopStart = ctk.CTkButton(timeTab, text="Start", font=custom_font2, width=40, height=25, command=self.stopngo, fg_color="#5cb85c")
        self.stopStart.grid(row=1, column=0, padx=30, pady=0)
        self.stopStart.place(relx=0.5, rely=0.71, anchor=tk.S)


        self.button6 = ctk.CTkButton(timeTab, text="Reset", height=35, command= self.timeReset)
        self.button6.grid(row=2, column=0, padx=0, pady=35)

        self.string_var = ctk.StringVar(value="black")

        self.tabTime = ctk.CTkLabel(timeTab,
                                font=("Times",40,'bold'),
                                
                                text="0:00:00.000",
                                width=250,
                                height=150,
                                fg_color=("black", "white"),
                                text_color=("white", "black")
                                )
        self.tabTime.grid(row=0, column=0, padx=30, pady=20)
        
        self.text_var2 = ctk.IntVar()

        #Color 
        colorMode = ctk.CTkButton(None, text="Color", width=20, height=25,corner_radius=30 , command=color, fg_color="#5bc0de", text_color="black")
        colorMode.place(relx=0.15, rely=0.95, anchor=tk.S)

        defaultMode = ctk.CTkButton(None, text="Default", width=20, height=25,corner_radius=30, command=default)
        defaultMode.place(relx=0.26, rely=0.95, anchor=tk.S)

        clearMode = ctk.CTkButton(None, text="Clear", width=20, height=25,corner_radius=30, command=transparent, fg_color="transparent", text_color=("black", "white"))
        clearMode.place(relx=0.37, rely=0.95, anchor=tk.S)
        
    def reset(self):
        self.text_var.set(0)
        self.tabCounter.configure(text=str(self.text_var.get()))



    #StopWatch Sequence

    def stopngo(self):
            if not self.running:
                if self.start_time is None:
                    self.start_time = datetime.now()
                else:
                    paused_time = datetime.now() - self.pause_time
                    self.start_time += paused_time

                self.running = True
                self.stopStart.configure(text="Stop", fg_color="#d9534f")
                self.update_time()
            else:
                self.pause_time = datetime.now()
                self.running = False
                self.stopStart.configure(text="Start", fg_color="#5cb85c")
            

    def timeReset(self):
        self.running = False
        self.stopStart.configure(text="Start", fg_color="#5cb85c")
        self.start_time = None
        self.update_display()


    def update_time(self):
        if self.running:
            elapsed = datetime.now() - self.start_time
            formatted_time = self.format_time(elapsed)
            self.tabTime.configure(text=formatted_time)
            self.after(50, self.update_time)
        
    def update_display(self):
        self.tabTime.configure(text="0:00:00.000")

    def format_time(self, elapsed):
        total_seconds = elapsed.total_seconds()
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((total_seconds - int(total_seconds)) * 1000)
        formatted_time = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{milliseconds:03d}"
        return formatted_time


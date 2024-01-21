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
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=(20, 20), pady=0, sticky="sn")
        
        my_tabs = ["Counter", "Timer"]

        counterTab = self.add(my_tabs[0])
        timeTab = self.add(my_tabs[1])
        
        
        
        
        
        def color():
            my_color = colorchooser.askcolor("black")
            valueStore = my_color[1]

            try: 
                self.label.configure(fg_color=valueStore)
                self.label2.configure(fg_color=valueStore)
            except ValueError:
                pass

        def plus():
            current_value = self.text_var.get()
            self.text_var.set(current_value + 1)
            self.label.configure(text=str(self.text_var.get()))
            
            
        def minus():
            current_value = self.text_var.get()
            if current_value == 0:
                self.text_var.set(0)
            else:
                self.text_var.set(current_value - 1)
                self.label.configure(text=str(self.text_var.get()))

            
        self.text_var = ctk.IntVar()

        self.label = ctk.CTkLabel(master=counterTab,
                                                  
                               font=custom_font,
                               text=str(self.text_var.get()),
                               width=250,
                               height=150,
                               fg_color=("black", "white"),
                               text_color=("white", "black")
                                )


        self.label.grid(row=0, column=0, padx=30, pady=0)
                
        self.button = ctk.CTkButton(self.tab("Counter"), text="+", font=custom_font2, width=30, height=25,
                               command=plus)

        self.button2 = ctk.CTkButton(self.tab("Counter"), text="-", font=custom_font2, width=30, height=25,
                                command=minus)
        

        self.button.grid(row=1, column=0, padx=30, pady=0)
        self.button.place(relx=0.9, rely=0.7, anchor=tk.SE)

        self.button2.grid(row=1, column=0, padx=0, pady=0)
        self.button2.place(relx=0.1, rely=0.7, anchor=tk.SW)

        button5 = ctk.CTkButton(counterTab, text="Reset", height=35, command= self.reset)
        button5.grid(row=2, column=0, padx=0, pady=35)








        self.running = False    #Defailt Running
        self.start_time = None  #Default Start Time
        self.pause_time = None

        self.button4 = ctk.CTkButton(timeTab, text="Start", font=custom_font2, width=40, height=25, command=self.stopngo)
        self.button4.grid(row=1, column=0, padx=30, pady=0)
        self.button4.place(relx=0.5, rely=0.71, anchor=tk.S)


        self.button6 = ctk.CTkButton(timeTab, text="Reset", height=35, command= self.timeReset)
        self.button6.grid(row=2, column=0, padx=0, pady=35)

        self.string_var = ctk.StringVar(value="black")

        self.label2 = ctk.CTkLabel(timeTab,
                                font=("Times",40,'bold'),
                                
                                text="0:00:00.000",
                                width=250,
                                height=150,
                                fg_color=("black", "white"),
                                text_color=("white", "black")
                                )
        self.label2.grid(row=0, column=0, padx=30, pady=0)
        
        self.text_var2 = ctk.IntVar()

        #Color 
        button3 = ctk.CTkButton(None, text="Color", width=20, height=25,corner_radius=30 , command=color)
        
        
        button3.place(relx=0.19, rely=0.9, anchor=tk.S)
        


    def stopngo(self):
            if not self.running:
                if self.start_time is None:
                    self.start_time = datetime.now()
                else:
                    paused_time = datetime.now() - self.pause_time
                    self.start_time += paused_time

                self.running = True
                self.button4.configure(text="Stop")
                self.update_time()
            else:
                self.pause_time = datetime.now()
                self.running = False
                self.button4.configure(text="Start")

    def reset(self):
            self.text_var.set(0)
            self.label.configure(text=str(self.text_var.get()))

            

    def timeReset(self):
        self.running = False
        self.button4.configure(text="Start")
        self.start_time = None
        self.update_display()


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


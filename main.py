import tkinter as tk
import customtkinter as ctk
from PIL import Image
# import ttkbootstrap as ttk


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
ctk.set_window_scaling(1)

class TextBox():
    pass

class MyLabel(ctk.CTkLabel):
    def __init__(self, master):
        pass
    pass


class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=1, column=0, padx=0, pady= (0, 20), sticky="snew")

        entry = ctk.CTkEntry(self, placeholder_text="1", width=70)
        entry.grid(row=0, column=0, padx=20, pady=25)
        entry.configure(state="disabled")

        entry2 = ctk.CTkEntry(self, placeholder_text="1", width=70)
        entry2.grid(row=0, column=1, padx=20, pady=25)
        entry2.configure(state="disabled")

        button = ctk.CTkButton(self, text="Flip", width=45, height=25)
        button.grid(row=1, column=0, padx=30, pady=0)

        button2 = ctk.CTkButton(self, text="Roll", width=45, height=25)
        button2.grid(row=1, column=1, padx=30, pady=0)





class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        custom_font =("Times",50,'bold')
        custom_font2 =("Times",30,'bold')
        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=(20, 20), pady=0, sticky="sn")
        
        self.add("Counter")
        self.add("Timer")

        text_var = ctk.StringVar(value="0")

        label = ctk.CTkLabel(master=self.tab("Counter"),
                               textvariable=text_var,
                               font=custom_font,
                               width=250,
                               height=150,
                               fg_color=("white", "black")
                                )
        label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        label2 = ctk.CTkLabel(master=self.tab("Timer"),
                               textvariable=text_var,
                               font=custom_font,
                               width=250,
                               height=150,
                               fg_color=("white", "black")
                                )
        
        label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
                
        button = ctk.CTkButton(self.tab("Counter"), text="+", font=custom_font2, width=40, height=35)
        button2 = ctk.CTkButton(self.tab("Counter"), text="-", font=custom_font2, width=40, height=35)
        button3 = ctk.CTkButton(self.tab("Counter"), text="Color", font=custom_font2, width=40, height=35)
        button4 = ctk.CTkButton(self.tab("Timer"), text="Start", font=custom_font2, width=40, height=35)
        # button.grid(row=0, column=0, padx=0, pady=0, sticky="n")
        button.place(relx=0.8, rely=1.0, anchor=tk.SW)
        button2.place(relx=0.2, rely=1.0, anchor=tk.SE)
        button3.place(relx=0.5, rely=1.0, anchor=tk.S)
        button4.place(relx=0.5, rely=1.0, anchor=tk.S)

       
        

        

        
        


class App(ctk.CTk, tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("650x400")
        self.grid_rowconfigure((0, 3), weight=2)  # configure grid system
        self.grid_columnconfigure(1, weight=1) 
        

        self.my_frame = TabView(self)
        self.my_frame.grid(row=1, column=0, padx=20, pady=0, sticky="w")
        #button
        
        

        # button2 = ctk.CTkButton(self, text="Flip", command= self.button_function, width=40, height=35)
        # button2.grid(row=0, column=1, padx=80, pady=0)

        # button3 = ctk.CTkButton(self, text="Roll", command= self.button_function, width=40, height=35)
        self.other_frame = MyFrame(self)
        self.other_frame.grid(row=1, column=1, padx=0, pady=0)
        
        button5 = ctk.CTkButton(self, text="CTkButton", command= self.button_function, height=35)
        button5.grid(row=2, column=0, padx=0, pady=0)
        
        segemented_button = ctk.CTkSegmentedButton(self, values=["Value 1", "Value 2", "Value 3"],
                                                     command=self.segmented_button_callback, height=10)
        segemented_button.set("Value 1")
        segemented_button.grid(row=0, column=0, padx=0, pady=0, sticky="snew")

    def segmented_button_callback(self, taco):
        print("segmented button clicked:", taco)

    

    def button_function(self):
        print("button pressed")
        
        


    



app = App()
app.title('Taco Bell')
app.resizable(0, 0)

app.mainloop()


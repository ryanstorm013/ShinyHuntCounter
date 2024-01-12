import tkinter as tk
import customtkinter as ctk


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class TextBox():
    pass

class MyFrame(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        custom_font =("Times",50,'bold')
        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=0, pady=0, sticky="esn")
        
        self.add("tab 1")
        self.add("tab 2")

        text_var = tk.StringVar(value="0")

        label = ctk.CTkLabel(master=self.tab("tab 1"),
                               textvariable=text_var,
                               font=custom_font,
                               width=250,
                               height=150,
                               fg_color=("white", "black")
                                )
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

                
        button = ctk.CTkButton(self.tab("tab 1"), text="+", width=30, height=25)
        
        # button.grid(row=0, column=0, padx=0, pady=0, sticky="n")
        button.place(relx=0.5, rely=1.0, anchor=tk.S)
        

        

        
        


class App(ctk.CTk, tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("500x300")
        self.pack
        self.grid_rowconfigure((0, 1), weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1) 
        

        self.my_frame = MyFrame(self)
        self.my_frame.grid(row=0, column=0, padx=0, pady=0, sticky="w")
        #button
        
        button = ctk.CTkButton(self, text="CTkButton", command= self.button_function)
        # button.grid_rowconfigure(0, weight=1)
        button.grid(row=1, column=0, padx=80, pady=0, sticky="wn")
        


    def button_function(self):
        print("button pressed")



app = App()
# app.master.title("taco time")

app.mainloop()


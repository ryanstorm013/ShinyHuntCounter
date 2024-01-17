import tkinter as tk
import customtkinter as ctk
from PIL import Image
import random
# import ttkbootstrap as ttk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
ctk.set_window_scaling(1)



class MyFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        def flip_Function():
            roll = random.randint(0, 1)
            if(roll == 0):
                text_var.set("Heads")
            else:
                text_var.set("Tails")
            
        
        def dice_function():
            text_var2.set(random.randint(1, 6))
        

        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=1, column=0, padx=0, pady= (0, 20), sticky="snew")

        

        button = ctk.CTkButton(self, text="Flip", width=45, height=25, command= flip_Function)
        button.grid(row=1, column=0, padx=30, pady=0)

        button2 = ctk.CTkButton(self, text="Roll", width=45, height=25, command= dice_function)
        button2.grid(row=1, column=1, padx=30, pady=0)

        text_var = ctk.StringVar()
        text_var2 = ctk.IntVar()

        entry = ctk.CTkEntry(self, textvariable= text_var, width=70)
        entry.grid(row=0, column=0, padx=20, pady=25)
        entry.configure(state="disabled")

        entry2 = ctk.CTkEntry(self, textvariable= text_var2, width=70)
        entry2.grid(row=0, column=1, padx=20, pady=25)
        entry2.configure(state="disabled")

        
    
        
        # return num

        
        







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
        
        

        self.text_var = ctk.IntVar(value=0)

        self.label = ctk.CTkLabel(master=self.tab("Counter"),
                               textvariable=self.text_var.get(),
                               font=custom_font,
                               width=250,
                               height=150,
                               fg_color=("white", "black")
                                )
        self.label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        label2 = ctk.CTkLabel(master=self.tab("Timer"),
                               textvariable=self.text_var,
                               font=custom_font,
                               width=250,
                               height=150,
                               fg_color=("white", "black")
                                )
        
        label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
                
        self.button = ctk.CTkButton(self.tab("Counter"), text="+", font=custom_font2, width=40, height=35,
                               command=self.counter)

        self.button2 = ctk.CTkButton(self.tab("Counter"), text="-", font=custom_font2, width=40, height=35,
                                command=self.counter)
        button3 = ctk.CTkButton(self.tab("Counter"), text="Color", font=custom_font2, width=40, height=35)
        button4 = ctk.CTkButton(self.tab("Timer"), text="Start", font=custom_font2, width=40, height=35)
        # button.grid(row=0, column=0, padx=0, pady=0, sticky="n")
        self.button.place(relx=0.8, rely=1.0, anchor=tk.SW)
        self.button2.place(relx=0.2, rely=1.0, anchor=tk.SE)
        button3.place(relx=0.5, rely=1.0, anchor=tk.S)
        button4.place(relx=0.5, rely=1.0, anchor=tk.S)


    def clickedPlus(self):
        plus = self.button.cget("text")
        # text = self.text_var.get("value")
        self.text_var.set(3)
        # print(text)
        return plus
    
    def clickedMinus(self):
        minus = self.button.cget("text")
        print("-")
        return minus
    
    def counter(self):
        num = 0
        if self.button.cget("text") == "+":
            num += 1
            
        elif self.button2.cget("text") == "-":
            num -= 1

        return self.text_var.set(num)

            
    
   

    


        

        
        

        

        
        


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
        
        button5 = ctk.CTkButton(self, text="Reset", command= self.button_function, height=35)
        button5.grid(row=2, column=0, padx=20, pady=20)
        
        segemented_button = ctk.CTkSegmentedButton(self, values=["Dark", "Light"],
                                                     command=self.segmented_button_callback, corner_radius=20, selected_color=("#E7F6F2", "#395B64"), text_color=("black", "white"))
        segemented_button.set("Value 1")
        segemented_button.grid(row=0, column=0, padx=0, pady=10, sticky="snew")
    
    # Modes: system (default), light, dark
    def segmented_button_callback(self, taco):
        if taco == "Dark":
            ctk.set_appearance_mode("dark")

        elif taco == "Light":
            ctk.set_appearance_mode("light") 
        else:
            ctk.set_appearance_mode("system")

    

    def button_function(self):
        print("button pressed")
        
        



app = App()
app.title('Taco Bell')
app.resizable(0, 0)

app.mainloop()


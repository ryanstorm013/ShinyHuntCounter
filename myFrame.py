import customtkinter as ctk
import random



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
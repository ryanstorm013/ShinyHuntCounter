import customtkinter as ctk

def segmented_button():
    def segmented_button_callback(setting): 

        if setting == "Dark":
            ctk.set_appearance_mode("dark")

        elif setting == "Light":
            ctk.set_appearance_mode("light") 

        else:
            ctk.set_appearance_mode("system")
            
    my_button = ctk.CTkSegmentedButton(master=None, values=["Dark", "Light"],
                                                     command=segmented_button_callback, corner_radius=20, selected_color=("#E7F6F2", "#395B64"), text_color=("black", "white"))

    my_button.set("Value 1")
    my_button.grid(row=0, column=0, padx=0, pady=10, sticky="snew")
            # Modes: system (default), light, dark
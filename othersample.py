import tkinter as tk
import random
from tkinter import colorchooser

def flip_coin():
    result_int_var.set(random.randint(0, 1))
    update_label_color()

def update_label_color():
    bg_color = colorchooser.askcolor()[1]
    fg_color = default_fg_color.get()
    result_label.config(bg=bg_color, fg=fg_color)

# Create the main window
root = tk.Tk()
root.title("Coin Flip GUI")

# Set a default foreground color
default_fg_color = tk.StringVar(value="black")

# Create and configure widgets
flip_button = tk.Button(root, text="Flip Coin", command=flip_coin)
flip_button.pack(pady=10)

result_int_var = tk.IntVar()
result_label = tk.Label(root, textvariable=result_int_var, width=20, height=2, relief="solid")
result_label.pack(pady=10)

color_button = tk.Button(root, text="Choose Color", command=update_label_color)
color_button.pack(pady=10)

# Entry to set a default foreground color
fg_color_entry = tk.Entry(root, textvariable=default_fg_color, width=10)
fg_color_entry.pack(pady=5)

# Start the main loop
root.mainloop()

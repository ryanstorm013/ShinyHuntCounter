import tkinter as tk
import random

def flip_coin():
    result_int_var.set(random.randint(0, 1))

# Create the main window
root = tk.Tk()
root.title("Coin Flip GUI")

# Create and configure widgets
flip_button = tk.Button(root, text="Flip Coin", command=flip_coin)
flip_button.pack(pady=20)

result_int_var = tk.IntVar()
result_entry = tk.Entry(root, textvariable=result_int_var, width=20, state='readonly')
result_entry.pack()

# Start the main loop
root.mainloop()

""" 
A clock application using Tkinter with localtime and 24hour format
"""
from time import strftime, localtime
import tkinter as tk

# Create a window
def Window():
    root = tk.Tk()
    root.title('Digital Clock')
    digital_clock = tk.Label(root, 
                         font=('calibri', 20, 'bold'), 
                         bg='black', 
                         fg='white')
    digital_clock.pack(fill='both', expand=1, ipadx=50, ipady=10)
    return root,digital_clock

root, digital_clock = Window()

# Function to update the time every second
def update_time():
    # Set initial time
    current_time = strftime('%H:%M:%S', localtime())
    display_text = tk.StringVar()
    display_text.set(current_time)
    digital_clock.config(textvariable=display_text, text=current_time)
    digital_clock.after(1000, update_time)

# Function to run the clock
def clock():
    update_time()
    # Run the window
    root.mainloop()

clock()

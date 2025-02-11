from time import strftime, localtime
import tkinter as tk

# Function to update the time every second
def update_time():
    # Get the current time
    string_time = strftime('%H:%M:%S', localtime())
    # Update the time on the label
    digital_clock.config(text=string_time)
    # Call the function again after 1 second
    digital_clock.after(1000, update_time)

# Create a window
root = tk.Tk()
root.title('Digital Clock')

# Set the background color to black and foreground color to white
digital_clock = tk.Label(root, font=('calibri', 20, 'bold'), bg='black', fg='white')
# Fill the entire window with ipadx and ipady for borders
digital_clock.pack(fill='both', expand=1, ipadx=50, ipady=10)

# Call the function to update the time
update_time()

# Run the window
root.mainloop()


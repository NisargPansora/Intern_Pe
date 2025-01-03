import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.configure(bg="black")

# Create and configure the clock label
clock_label = tk.Label(root, font=("Helvetica", 48, "bold"), background="black", foreground="white")
clock_label.pack(anchor="center", expand=True, pady=10)

#Create and configure date label
date_label = tk.Label(root, font=("Helvetica", 36), background="black", foreground="white")
date_label.pack(anchor="center")

# Function to update the time
def update_time():
    current_time = strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    current_date = strftime('%A, %d %B %Y')
    date_label.config(text=current_date)
    root.after(1000, update_time)


# Initialize the clock update
update_time()

# Start the GUI loop
root.mainloop()

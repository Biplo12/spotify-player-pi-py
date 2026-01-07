import tkinter as tk
from datetime import datetime
from config import SCREEN_WIDTH, SCREEN_HEIGHT, UPDATE_INTERVAL


# -----------------------------
# Tkinter UI Setup
# -----------------------------
root = tk.Tk()
root.title("Clock")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.resizable(False, False)

container = tk.Frame(root, bg="#111111")
container.pack(fill="both", expand=True)

time_label = tk.Label(
    container,
    text="",
    fg="#ffffff",
    bg="#111111",
    font=("Arial", 48, "bold"),
    justify="center"
)
time_label.pack(expand=True)

date_label = tk.Label(
    container,
    text="",
    fg="#bbbbbb",
    bg="#111111",
    font=("Arial", 20),
    justify="center"
)
date_label.pack(pady=(0, 20))


# -----------------------------
# Clock Update Function
# -----------------------------
def update_clock():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%A, %B %d, %Y")

    time_label.config(text=time_str)
    date_label.config(text=date_str)

    root.after(UPDATE_INTERVAL * 1000, update_clock)


# Kick off clock update
update_clock()

# Start UI
root.mainloop()

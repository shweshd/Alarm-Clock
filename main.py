import tkinter as tk
from tkinter import messagebox
import time
import threading
from playsound import playsound


# -----------------------------
# Alarm sound
# -----------------------------

alarm_running = False


def play_alarm():
    global alarm_running

    while alarm_running:
        playsound("alarm.mp3")


# -----------------------------
# Countdown
# -----------------------------

def start_alarm():
    global alarm_running

    try:
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())

        if minutes < 0 or seconds < 0:
            raise ValueError

        total_seconds = minutes * 60 + seconds

        if total_seconds == 0:
            messagebox.showerror(
                "Invalid Time",
                "Please enter a time greater than 0."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers."
        )
        return

    start_button.config(state="disabled")
    minutes_entry.config(state="disabled")
    seconds_entry.config(state="disabled")

    countdown(total_seconds)


def countdown(total_seconds):
    if total_seconds > 0:
        minutes_left = total_seconds // 60
        seconds_left = total_seconds % 60

        timer_label.config(
            text=f"{minutes_left:02d}:{seconds_left:02d}"
        )

        root.after(
            1000,
            countdown,
            total_seconds - 1
        )

    else:
        timer_label.config(text="00:00")
        alarm()


# -----------------------------
# Start alarm sound
# -----------------------------

def alarm():
    global alarm_running

    alarm_running = True

    stop_button.config(state="normal")

    threading.Thread(
        target=play_alarm,
        daemon=True
    ).start()


# -----------------------------
# Stop alarm
# -----------------------------

def stop_alarm():
    global alarm_running

    alarm_running = False

    stop_button.config(state="disabled")
    start_button.config(state="normal")

    minutes_entry.config(state="normal")
    seconds_entry.config(state="normal")

    timer_label.config(text="00:00")


# -----------------------------
# GUI
# -----------------------------

root = tk.Tk()

root.title("Alarm Clock")
root.geometry("400x400")
root.resizable(False, False)


# Title

title_label = tk.Label(
    root,
    text="ALARM CLOCK",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=30)


# Minutes

minutes_label = tk.Label(
    root,
    text="Minutes",
    font=("Arial", 12)
)

minutes_label.pack()

minutes_entry = tk.Entry(
    root,
    width=10,
    font=("Arial", 16),
    justify="center"
)

minutes_entry.pack(pady=5)


# Seconds

seconds_label = tk.Label(
    root,
    text="Seconds",
    font=("Arial", 12)
)

seconds_label.pack()

seconds_entry = tk.Entry(
    root,
    width=10,
    font=("Arial", 16),
    justify="center"
)

seconds_entry.pack(pady=5)


# Timer

timer_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 40, "bold")
)

timer_label.pack(pady=20)


# Start button

start_button = tk.Button(
    root,
    text="SET ALARM",
    font=("Arial", 12, "bold"),
    command=start_alarm,
    width=15
)

start_button.pack(pady=5)


# Stop button

stop_button = tk.Button(
    root,
    text="STOP ALARM",
    font=("Arial", 12, "bold"),
    command=stop_alarm,
    width=15,
    state="disabled"
)

stop_button.pack(pady=5)


# Start GUI

root.mainloop()

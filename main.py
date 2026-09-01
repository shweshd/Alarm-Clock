import customtkinter as ctk
import threading
from playsound import playsound


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

alarm_running = False


def play_alarm():
    global alarm_running

    while alarm_running:
        playsound("alarm.mp3")


def start_alarm():
    global alarm_running

    try:
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())

        if minutes < 0 or seconds < 0:
            raise ValueError

        total_seconds = minutes * 60 + seconds

        if total_seconds <= 0:
            status_label.configure(
                text="Please enter a time greater than 0."
            )
            return

    except ValueError:
        status_label.configure(
            text="Please enter valid numbers."
        )
        return

    start_button.configure(state="disabled")
    minutes_entry.configure(state="disabled")
    seconds_entry.configure(state="disabled")

    status_label.configure(text="Alarm is running...")

    countdown(total_seconds)


def countdown(total_seconds):

    if total_seconds > 0:

        minutes_left = total_seconds // 60
        seconds_left = total_seconds % 60

        timer_label.configure(
            text=f"{minutes_left:02d}:{seconds_left:02d}"
        )

        root.after(
            1000,
            countdown,
            total_seconds - 1
        )

    else:
        timer_label.configure(text="00:00")
        alarm()


def alarm():
    global alarm_running

    alarm_running = True

    status_label.configure(
        text="ALARM! Press STOP to silence."
    )

    stop_button.configure(state="normal")

    threading.Thread(
        target=play_alarm,
        daemon=True
    ).start()


def stop_alarm():
    global alarm_running

    alarm_running = False

    stop_button.configure(state="disabled")
    start_button.configure(state="normal")

    minutes_entry.configure(state="normal")
    seconds_entry.configure(state="normal")

    timer_label.configure(text="00:00")

    status_label.configure(
        text="Alarm stopped."
    )


root = ctk.CTk()

root.title("Alarm Clock")
root.geometry("500x600")
root.resizable(False, False)

root.configure(
    fg_color="#0B0B0F"
)


main_frame = ctk.CTkFrame(
    root,
    width=420,
    height=520,
    corner_radius=30,
    fg_color="#15151C"
)

main_frame.pack(
    padx=40,
    pady=40,
    fill="both",
    expand=True
)


title_label = ctk.CTkLabel(
    main_frame,
    text="ALARM CLOCK",
    font=("Arial", 30, "bold"),
    text_color="#FFFFFF"
)

title_label.pack(pady=(35, 5))


subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Set a countdown and relax",
    font=("Arial", 14),
    text_color="#8F8F9D"
)

subtitle_label.pack(pady=(0, 30))


input_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

input_frame.pack()


# Minutes

minutes_container = ctk.CTkFrame(
    input_frame,
    fg_color="#202029",
    corner_radius=18
)

minutes_container.grid(
    row=0,
    column=0,
    padx=8
)

minutes_label = ctk.CTkLabel(
    minutes_container,
    text="MINUTES",
    font=("Arial", 11, "bold"),
    text_color="#888894"
)

minutes_label.pack(
    padx=25,
    pady=(12, 2)
)

minutes_entry = ctk.CTkEntry(
    minutes_container,
    width=90,
    height=45,
    corner_radius=15,
    border_width=0,
    fg_color="#2A2A35",
    text_color="#FFFFFF",
    font=("Arial", 20),
    justify="center",
    placeholder_text="00"
)

minutes_entry.pack(
    padx=15,
    pady=(2, 15)
)


# Seconds

seconds_container = ctk.CTkFrame(
    input_frame,
    fg_color="#202029",
    corner_radius=18
)

seconds_container.grid(
    row=0,
    column=1,
    padx=8
)

seconds_label = ctk.CTkLabel(
    seconds_container,
    text="SECONDS",
    font=("Arial", 11, "bold"),
    text_color="#888894"
)

seconds_label.pack(
    padx=25,
    pady=(12, 2)
)

seconds_entry = ctk.CTkEntry(
    seconds_container,
    width=90,
    height=45,
    corner_radius=15,
    border_width=0,
    fg_color="#2A2A35",
    text_color="#FFFFFF",
    font=("Arial", 20),
    justify="center",
    placeholder_text="00"
)

seconds_entry.pack(
    padx=15,
    pady=(2, 15)
)


timer_label = ctk.CTkLabel(
    main_frame,
    text="00:00",
    font=("Arial", 64, "bold"),
    text_color="#FFFFFF"
)

timer_label.pack(
    pady=(35, 5)
)


status_label = ctk.CTkLabel(
    main_frame,
    text="Ready to set your alarm",
    font=("Arial", 13),
    text_color="#8F8F9D"
)

status_label.pack(
    pady=(0, 25)
)


start_button = ctk.CTkButton(
    main_frame,
    text="SET ALARM",
    width=260,
    height=55,
    corner_radius=28,
    font=("Arial", 15, "bold"),
    fg_color="#FFFFFF",
    hover_color="#DCDCE2",
    text_color="#111111",
    command=start_alarm
)

start_button.pack(
    pady=8
)


stop_button = ctk.CTkButton(
    main_frame,
    text="STOP ALARM",
    width=260,
    height=55,
    corner_radius=28,
    font=("Arial", 15, "bold"),
    fg_color="#2A2A35",
    hover_color="#3A3A48",
    text_color="#FFFFFF",
    command=stop_alarm,
    state="disabled"
)

stop_button.pack(
    pady=8
)

root.mainloop()
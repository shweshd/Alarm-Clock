from playsound import playsound
import time
import threading
import msvcrt

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def play_alarm():
    while True:
        playsound("alarm.mp3")


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(
            f"{CLEAR_AND_RETURN}"
            f"Alarm will sound in: "
            f"{minutes_left:02d}:{seconds_left:02d}"
        )

    print("\nALARM! Press SPACE to stop.")

    # Start alarm sound in background
    alarm_thread = threading.Thread(target=play_alarm, daemon=True)
    alarm_thread.start()

    # Wait for Space
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()

            if key == b" ":
                print("Alarm stopped.")
                break

        time.sleep(0.1)


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))

total_seconds = minutes * 60 + seconds

alarm(total_seconds)
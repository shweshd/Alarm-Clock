# Alarm Clock

A modern **Python Alarm Clock** application built with **CustomTkinter**. It provides a graphical interface for setting a countdown alarm and playing an alarm sound when the countdown reaches zero.

## Features

* Modern dark-themed graphical user interface
* Set an alarm using minutes and seconds
* Live countdown timer
* Plays an MP3 alarm sound
* Repeats the alarm sound continuously
* Start and stop alarm controls
* Capsule-shaped modern buttons
* Input validation for invalid values
* Background thread for alarm sound playback

## Preview

The application provides a clean desktop interface with:

* Alarm Clock title
* Countdown input fields
* Live countdown display
* Alarm status
* Set Alarm button
* Stop Alarm button

## Requirements

* Python 3.x
* CustomTkinter
* playsound

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shweshd/Alarm-Clock.git
```

### 2. Open the project folder

```bash
cd Alarm-Clock
```

### 3. Install the required packages

```bash
pip install customtkinter
```

```bash
pip install playsound==1.2.2
```

Or install both at once:

```bash
pip install customtkinter playsound==1.2.2
```

## Project Structure

```text
Alarm-Clock/
│
├── alarm_clock.py
├── alarm.mp3
└── README.md
```

## How to Run

Run the application using:

```bash
python alarm_clock.py
```

A graphical alarm clock window will open.

## How to Use

### 1. Enter the alarm duration

Enter the desired time in the **Minutes** and **Seconds** fields.

For example:

```text
Minutes: 0
Seconds: 10
```

### 2. Set the alarm

Click:

```text
SET ALARM
```

The countdown will begin.

Example:

```text
00:10
00:09
00:08
...
00:01
00:00
```

### 3. Stop the alarm

When the countdown reaches `00:00`, the alarm sound will start playing continuously.

Click:

```text
STOP ALARM
```

to stop the alarm.

## Alarm Sound

The application uses an MP3 file named:

```text
alarm.mp3
```

Make sure `alarm.mp3` is located in the same directory as `alarm_clock.py`.

```text
Alarm-Clock/
├── alarm_clock.py
├── alarm.mp3
└── README.md
```

## Technologies Used

* **Python** — Application logic
* **CustomTkinter** — Modern graphical user interface
* **Threading** — Background alarm sound playback
* **playsound** — MP3 audio playback

## Concepts Practiced

* Functions
* Variables
* Conditional statements
* Loops
* Exception handling
* User input
* GUI development
* Event-driven programming
* Countdown timers
* `threading`
* Audio playback
* Widget configuration
* GUI layout management

## Future Improvements

Possible improvements for future versions:

* Set an alarm for a specific time, such as `10:00 AM` or `11:00 PM`
* Multiple alarms
* Snooze functionality
* Custom alarm sounds
* Delete and edit alarms
* Date-based alarms
* System tray support
* Start automatically with Windows
* Package the application as a Windows `.exe`
* Improved animations and UI
* Cross-platform support

## License

This project is created for **learning and practice purposes**.

```

One thing to check before pushing: your current file is named `alarm_clock.py`, so the README correctly uses that name instead of the old `main.py`.
```

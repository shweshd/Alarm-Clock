# Alarm Clock

A simple **Python alarm clock** mini project that lets the user set a countdown timer and plays an alarm sound continuously when the timer reaches zero.

## Features

* Set alarm time using minutes and seconds
* Live countdown timer
* Plays an MP3 alarm sound
* Repeats the alarm sound continuously
* Press **Space** to stop the alarm
* Built using basic Python concepts

## Requirements

* Python 3.x
* `playsound` package

Install `playsound`:

```bash
pip install playsound
```

## Project Structure

```text
Alarm-Clock/
│
├── main.py
├── alarm.mp3
└── README.md
```

## How to Run

1. Clone or download the repository.
2. Make sure `alarm.mp3` is in the same folder as `main.py`.
3. Open the project in VS Code.
4. Run:

```bash
python main.py
```

5. Enter the number of minutes and seconds.
6. When the countdown reaches `00:00`, the alarm will start.
7. Press **Space** to stop the alarm.

## Example

```text
How many minutes to wait: 0
How many seconds to wait: 10

Alarm will sound in: 00:10
Alarm will sound in: 00:09
...
Alarm will sound in: 00:01

ALARM! Press SPACE to stop.
```

## Concepts Practiced

* Functions
* Loops
* User input
* `time` module
* `threading`
* Keyboard input with `msvcrt`
* Audio playback
* Basic terminal control

## License

This project is created for **learning and practice purposes**.

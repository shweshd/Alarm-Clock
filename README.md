# Alarm Clock

A simple **Python alarm clock** mini project that lets the user set a countdown timer and plays an alarm sound continuously when the timer reaches zero.

<img src="https://github.com/user-attachments/assets/9a6979e1-6bef-4fd3-b9a0-624349e29098" width="400">

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

### 1. Clone the repository

```bash
git clone https://github.com/shweshd/Alarm-Clock.git
```

### 2. Open the project folder

```bash
cd Alarm-Clock
```

### 3. Install the required package

```bash
pip install playsound
```

### 4. Run the program

```bash
python main.py
```

### 5. Set the alarm

Enter the number of minutes and seconds when prompted:

```text
How many minutes to wait: 0
How many seconds to wait: 10
```

The countdown will begin.

### 6. Stop the alarm

When the countdown reaches `00:00`, the alarm sound will play continuously.

Press **Space** to stop the alarm.

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

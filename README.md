# HackerAI Keylogger

## Overview
This project is a Python-based keylogger with both console and GUI versions. It uses the `pynput` library to capture keyboard events and logs them in both JSON and plain text formats. The GUI version is built with `tkinter` and provides controls to start, stop, and clear logs, as well as a live display of captured keystrokes.

## Features
- **Keyboard Event Logging:** Captures key presses, holds, and releases.
- **Multiple Output Formats:** Logs are saved in both `logs.json` (structured JSON) and `logs.txt` (plain text).
- **GUI Control Panel:** Start, stop, and clear logs with a user-friendly interface (see `update.V.02.py`).
- **Live Log Display:** View keystrokes in real-time in the GUI.
- **Thread-Safe Logging:** Ensures GUI updates are safe and responsive.

## Files
- `keylogger.py`: Basic keylogger that logs keystrokes to `logs.json`.
- `update.V.01.py`: Enhanced version that logs to both JSON and TXT files, with improved formatting.
- `update.V.02.py`: Advanced version with a Tkinter GUI for interactive control and live log viewing.
- `logs.json`: Output file for structured key logs (created at runtime).
- `logs.txt`: Output file for plain text key logs (created at runtime).

## Requirements
- Python 3.x
- `pynput` library
- `tkinter` (usually included with Python)

Install dependencies with:
```bash
pip install pynput
```

## Usage
### Console Version
Run the basic or enhanced keylogger from the terminal:
```bash
python keylogger.py
# or
python update.V.01.py
```

### GUI Version
Run the GUI keylogger:
```bash
python update.V.02.py
```

- **START:** Begins logging keystrokes.
- **STOP:** Stops logging.
- **CLEAR LOGS:** Clears the log files and GUI display.

## Security & Ethics
This tool is for educational and authorized testing purposes only. Do **not** use it to monitor devices without explicit permission. Unauthorized use may be illegal and unethical.

## Disclaimer
The author is not responsible for any misuse of this software. Use responsibly and only in compliance with local laws and regulations.

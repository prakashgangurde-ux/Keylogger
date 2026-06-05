# Python Keyboard Event Logger

A Python application that demonstrates keyboard event monitoring, JSON data logging, multithreading, and GUI development using Tkinter.

> Educational project for learning event-driven programming, file handling, and desktop application development in Python.

---

## Features

### Keyboard Event Monitoring

* Captures keyboard press and release events.
* Records user input activity in real time.
* Demonstrates event listeners using the `pynput` library.

### Multiple Log Formats

* Structured JSON output (`logs.json`)
* Plain text output (`logs.txt`)

### Graphical User Interface

* Built with Tkinter.
* Start and stop logging with a simple control panel.
* Clear log files directly from the application.
* View captured events in real time.

### Thread-Safe Architecture

* Uses threading to keep the GUI responsive.
* Safe communication between background logging processes and the user interface.

---

## Technologies Used

* Python 3
* Tkinter
* pynput
* JSON
* Threading

---

## Project Structure

```text
Keylogger/
│
├── keylogger.py          # Basic keyboard event logger
├── update.V.01.py        # Enhanced logger with JSON and TXT output
├── update.V.02.py        # GUI version with live monitoring
│
├── logs.json             # Generated at runtime
├── logs.txt              # Generated at runtime
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/prakashgangurde-ux/Keylogger.git
cd Keylogger
```

### Install Dependencies

```bash
pip install pynput
```

---

## Usage

### Console Version

Run the basic logger:

```bash
python keylogger.py
```

Or the enhanced version:

```bash
python update.V.01.py
```

### GUI Version

Launch the graphical interface:

```bash
python update.V.02.py
```

### Available Controls

| Button     | Function                            |
| ---------- | ----------------------------------- |
| START      | Begin monitoring keyboard events    |
| STOP       | Stop monitoring                     |
| CLEAR LOGS | Remove saved logs and clear display |

---

## Learning Objectives

This project demonstrates:

* Event-driven programming
* Keyboard input handling
* File I/O operations
* JSON serialization
* GUI development with Tkinter
* Multithreading concepts
* Thread-safe UI updates

---

## Screenshots

Add screenshots of the GUI here.

Example:

```text
screenshots/
├── main-window.png
├── logging-active.png
└── logs-view.png
```

---

## Future Improvements

* Export logs as CSV
* Search and filter functionality
* Dark mode interface
* Configurable log storage location
* Improved event statistics dashboard
* Cross-platform packaging

---

## Ethical Use Notice

This project is intended solely for educational purposes and authorized testing environments.

Users should only run this software on systems they own or have explicit permission to test. Unauthorized monitoring of devices or user activity may violate privacy laws and organizational policies.

---

## License

This project is open source and available under the MIT License.

---

## Author

Prakash Gangurde

GitHub:
https://github.com/prakashgangurde-ux

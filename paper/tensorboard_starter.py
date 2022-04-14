import os
import sys
import webbrowser
import ws_specific_settings as wss

def start_and_open():
    print("Starting tensorboard...")
    current_script_path = wss.storage + r":\models"
    webbrowser.open_new("http://localhost:6006/#scalars")
    os.system('python -m tensorboard.main --logdir='+ current_script_path)

if __name__ == "__main__":
    start_and_open()
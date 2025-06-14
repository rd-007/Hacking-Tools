"""
Clipboard Activity Monitor - Educational Tool
- This Python script monitors clipboard changes and logs clipboard content with timestamps.
- It demonstrates how clipboard data can be intercepted and highlights privacy concerns.

Usage:
    python clipboard_monitor.py
    
Notes:
- This tool is intended for ethical security research and education.
- Use it only on systems where you have permission.
- It logs clipboard text data; be mindful of sensitive data handling.
"""

import time
import threading
import logging
import sys

try:
    import tkinter as tk
except ImportError:
    print("tkinter is required but not installed. Please install it to proceed.")
    sys.exit(1)

class ClipboardMonitor:
    def __init__(self, poll_interval=1.0, log_file="clipboard.log"):
        self.poll_interval = poll_interval
        self.log_file = log_file
        self._root = tk.Tk()
        self._root.withdraw()  # Hide the main window
        self.last_clipboard = None
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def get_clipboard_data(self):
        try:
            data = self._root.clipboard_get()
            return data
        except tk.TclError:
            # Clipboard empty or non-text data
            return None

    def monitor_clipboard(self):
        print(f"Monitoring clipboard... Logging to '{self.log_file}'. Press Ctrl+C to stop.")
        try:
            while True:
                clipboard_data = self.get_clipboard_data()
                if clipboard_data and clipboard_data != self.last_clipboard:
                    self.last_clipboard = clipboard_data
                    print(f"Clipboard changed: {clipboard_data!r}")
                    logging.info(f"Clipboard content: {clipboard_data}")
                time.sleep(self.poll_interval)
        except KeyboardInterrupt:
            print("\nClipboard monitoring stopped by user.")

def main():
    monitor = ClipboardMonitor()
    monitor.monitor_clipboard()

if __name__ == "__main__":
    main()

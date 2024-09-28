# MAIN THREAD => It is the first thread that is created when the program is executed. 
# This thread executes the main code of the program and manages its central logic, in
# addition, it allows the creation of normal secondary threads and daemon threads. The 
# main thread is always a normal or non-daemon thread.

# SECONDARY THREADS => These are threads created by the main thread or another 
# secondary thread that run in the background to perform tasks or functions concurrently
# or in parallel.

# TYPES OF SECONDARY THREADS:

# * NORMAL OR NON-DAEMON THREADS => Threads that, upon completing the task for which 
# they were created, terminate their execution.
# * DAEMON THREADS => Threads that run in the background continuously, this with the aim 
# of listening to events (for example mouse clicks, network messages, etc) and perform 
# an action when these events happen. These threads start automatically when the program
# is open, and end their execution when the program is closed.

import threading
from pynput import keyboard # Allows you control and monitor input devices.
from time import sleep

def show_key_pressed(key):
    try:
        print(f"Key \"{key.char}\" pressed.")
    except AttributeError:
        special_key_name = str(key).split(".")[1]
        print(f"Key \"{special_key_name}\" pressed.")
    
def listen_keys():
    with keyboard.Listener(on_press=show_key_pressed) as listener:
        listener.join()
#                                           Set a thread as daemon thread.
#                                                         ↓
daemon_thread = threading.Thread(target=listen_keys, daemon=True) # Create a daemon 
# thread that listens for and displays key pressed of the keyboard in the background. 
daemon_thread.start()

print("Running \"Daemon Thread\" in the background.")
print("Running \"Main Thread\".")
sleep(10)
    
print("\"Daemon Thread\" and \"Main Thread\" have ended.")
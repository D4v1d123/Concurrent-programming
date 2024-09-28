# is_alive => Method that determines whether a thread is running (True) or not (false).
# It is used to analyze and debug the behavior of a program's threads , as well as 
# synchronize their execution. 

# active_count => Function that counts the amount of active (running) threads within a
# process. It is used to identify thread leaks, manage the creation of new threads 
# without exceeding an established limit, debug concurrent programs, etc. 

# THREAD LEAKS => These are unfinished or unnecessary threads that continue existing, 
# thus causing excessive consumption of system resources, making it unstable.

# enumerate => Function that generates a list of the threads (objects of the Thread 
# class) that are active with the objective of analyzing and debugging a program.

# main_thread => Function that obtains the object that identifies the main thread in a
# process or program. It is used to differentiate the main thread from secondary or 
# child threads.

import threading
from time import sleep

def task1():
    sleep(3)
    print("Task 1 completed.")
    
def task2():
    sleep(4)
    print("Task 2 completed.")
    
def task3():
    sleep(1)
    print("Task 3 completed.")
    
def show_thread_status():
    print("\nTHREAD STATUS:")
    #               Determine whether a thread is alive (True) or not (False).
    #                                         ↓
    print(f"* Main thread => {main_thread.is_alive()}. \
        \n* Thread 1 => {thread_1.is_alive()}. \
        \n* Thread 2 => {thread_2.is_alive()}. \
        \n* Thread 3 => {thread_3.is_alive()}.")
    print(f"ACTIVE THREADS => {threading.active_count()}. \n")
    #                                          ↑
    #                        Determine how many threads are active.
    
thread_1 = threading.Thread(target=task1)
thread_2 = threading.Thread(target=task2)
thread_3 = threading.Thread(target=task3)
main_thread = threading.main_thread() # Get an object that represents the main thread. 

show_thread_status()

thread_1.start()
thread_2.start()

show_thread_status()

thread_list = threading.enumerate() # Generate a list of all active threads.
for thread in thread_list:
    if thread.is_alive() and thread != main_thread:
        thread.join()
        
print("\nThe program has ended.")
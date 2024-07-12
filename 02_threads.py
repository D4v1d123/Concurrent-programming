# THREADS => They allow tasks or functions to be executed concurrently (in the
# background) with the aim of listening to events and performing an action or task in
# response to them. Reduce program execution time when there are multiple data input 
# and output operations because other tasks can be executed while waiting for those 
# operations to complete.

# On the other hand, threads can only be executed once (they cannot execute the same 
# task twice), and they share resources within the same process. Finally, a thread can
# create other threads within the same process.

# THREAD STATES:

# * READY => Thread created and ready to run.
# * RUNNING => Thread that is carrying out a task.
# * SUSPENDED OR BLOCKED => Thread waiting for a response or event, after which it 
# resumes to continue executing the task.
# * TERMINATED => Thread terminated, eliminating its execution context.

# START => Method that allows you to start the execution of a thread or task in the
# background.

# join => Method that suspends a thread until the execution of another specific thread 
# finishes to continue the execution of the program. It is used to synchronize the 
# execution of threads in a predefined order to avoid unexpected results.

from time import sleep
import threading

def update_inventory(product_id, amount):
    global products
    
    products[product_id] -= amount
    sleep(3)
    print("Updated inventory.")
    
def generate_invoice():
    sleep(2)
    print("Invoice generated and saved in the database.")
    
def send_mail(user_mail):
    sleep(2)
    print(f"Mail send to {user_mail}.")

products = {
    "rice": 32,
    "pasta": 88,
    "egg": 25,
    "mayonnaise": 58,
    "milk": 2
    }   
product_id = "rice"
amount = 20

# Create threads
thread_1 = threading.Thread(target=update_inventory, args=(product_id, amount), name="update_inventory_user_368")
thread_2 = threading.Thread(target=generate_invoice, name="generate_invoice_user_368")
thread_3 = threading.Thread(target=send_mail, args=("solor26@outlook.com",), name="send_mail_user_368")
#   ↑                                    ↑                      ↑                             ↑
# Object or                      Function or task            Function                     Thread name 
# thread                         to execute                  arguments                    (optional)    

# Start thread execution.
thread_1.start()
thread_2.start()
thread_3.start()

# Wait for each thread to finish its task or function to continue with the program 
# execution.
thread_1.join()
thread_2.join()
thread_3.join()

print("\nPurchase made successfully!!!")


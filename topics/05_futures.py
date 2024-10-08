# FUTURES => It is an object that is responsible for obtaining the return value of a 
# task or thread that executes concurrently (it can also be used with thread that do 
# not return any result). This tool creates and manages the execution of threads of 
# automatically, resulting in more readable, concise and scalable code, due to these
# advantages, its use is recommended in programs that manage a large number of threads.

# set_result => Method that manually sets the result of a task or function to the 
# future object.

# add_done_callback => Method that adds a callback to perform an action with the result
# of the future.

# done => Method that checks if a future has finished its execution, either because it
# completed successfully, an error occurred or its execution was canceled. 

import threading
from time import sleep
from concurrent.futures import Future

def query_db(query):
    future = Future() # Create the future object.

    thread = threading.Thread(target=generate_response_db, args=(future, )) # Create a 
    # thread that queries the database.
    thread.start()

    return future
    
def generate_response_db(future): # Simulates the response generated by the database.
    sleep(2)
    # Save the database response in the future.
    future.set_result([
            ("david guerrero", 23, "davidemail@gmail.com", "male", "3985210233")
    ])
    
def show_info_user(response): # Callback function that processes the response given by 
# the database.
    print("\nUSER INFORMATION:")
    print(f"* Name: {response[0][0].title()}. \
          \n* Age: {response[0][1]}. \
          \n* Mail: {response[0][2]}. \
          \n* Sex: {response[0][3].title()}. \
          \n* Phone number: {response[0][4]}.")
    
future = query_db("SELECT * FROM users WHERE id = 1040648811")
future.add_done_callback(lambda future: show_info_user(future.result()))

while not future.done():
    print("Query in process.")
    sleep(0.25)
else:
    print("\nQuery completed successfully.")
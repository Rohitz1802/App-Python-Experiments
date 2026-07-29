import time

# Decorator function
def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", end - start, "seconds")
    return wrapper

# Function to be decorated
@calculate_time
def display_numbers():
    for i in range(1, 1000001):
        pass
    print("Loop Executed Successfully")

# Function call
display_numbers()

from time import time

def track_time(initial_time, message = "elapsed time: "):
    """ space-efficient way to print timings """
    current_time = time()
    print(message, current_time - initial_time)
    return current_time
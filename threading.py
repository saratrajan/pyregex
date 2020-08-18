import time
import os
import random

def get_current_time():
    return time.perf_counter()

def lets_sleep(seconds):
    print(f"Sleeping {seconds} second(s) here...")
    time.sleep(seconds)
    print("Waking up now...")

def calculate_elapsed_time(start_time, end_time):
    return round(end_time - start_time, 2)


def main():
    start_time = get_current_time()
    if(os.environ.get('TRAVIS') == True):
        seconds = random.randrange(25)
    else:    
        seconds = input("Please input desired seconds to sleep:  ")
        seconds = int(seconds)
    lets_sleep(seconds)
    end_time = get_current_time()
    time_elapsed = calculate_elapsed_time(start_time, end_time)
    print(f'Finished in {time_elapsed} second(s)...')

if __name__ == "__main__":
    main()

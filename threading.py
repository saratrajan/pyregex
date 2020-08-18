""" Trying out threading mechanisms """

import time
import random


def get_current_time():
    """ Getting current time """
    return time.perf_counter()

def lets_sleep(seconds):
    """ Sleeping in thread """
    print(f"Sleeping {seconds} second(s) here...")
    time.sleep(seconds)
    print("Waking up now...")


def calculate_elapsed_time(start_time, end_time):
    """ Calculating time elapsed """
    print("Getting elapsed time")
    return round(end_time - start_time, 2)

def do_the_thing():
    """ Action is happening here """
    _start_time = get_current_time()
    _seconds = random.randrange(10)
    print("zzzz.....")
    lets_sleep(_seconds)
    _end_time = get_current_time()
    _time_elapsed = calculate_elapsed_time(_start_time, _end_time)
    print(f'Finished in {_time_elapsed} second(s)...')


def main():
    """ I am the main dude """
    i = 1
    while i < 4:
        print(f'Attempt no: {i}')
        do_the_thing()
        i += 1

if __name__ == "__main__":
    main()

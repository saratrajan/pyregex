#!/usr/bin/python

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


def do_the_thing():
    start_time = get_current_time()
    _seconds = random.randrange(5) 
    lets_sleep(_seconds)
    end_time = get_current_time()
    time_elapsed = calculate_elapsed_time(start_time, end_time)
    print(f'Finished in {time_elapsed} second(s)...')

def main():
    i = 1
    while i < 4:
        print(f'Attempt no: {i}')
        do_the_thing()
        i += 1

if __name__ == "__main__":
    main()

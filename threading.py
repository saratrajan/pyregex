""" Trying out threading mechanisms """

import time
import random
import threading


def get_current_time():
    """ Getting current time """
    return time.perf_counter()

def lets_sleep(seconds):
    """ Sleeping in thread """
    print(f'Sleeping {seconds} second(s) here...')
    time.sleep(seconds)
    print("Waking up now...")


def calculate_elapsed_time(start_time, end_time):
    """ Calculating time elapsed """
    print("Getting elapsed time")
    return round(end_time - start_time, 2)

def do_the_thing():
    """ Action is happening here """
    _seconds = random.randrange(20)
    print("zzzz.....")
    lets_sleep(_seconds)


def main():
    """ I am the main dude """
    i = 1
    start_time = get_current_time()
    threads = []
    while i < 4:
        print(f'Attempt no: {i}')
        t = threading.Thread(target=do_the_thing)
        t.start()
#        t.join()
        threads.append(t)
        i += 1
    for thread in threads:
        thread.join()    
    end_time = get_current_time()
    _time_elapsed = calculate_elapsed_time(start_time, end_time)
    print(f'Finished in {_time_elapsed} second(s)...')

if __name__ == "__main__":
    main()

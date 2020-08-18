import time

def getCurrentTime():
    return time.perf_counter()

def lets_sleep(seconds):
    print(f"Sleeping {seconds} second(s) here...")
    time.sleep(seconds)
    print("Waking up now...")

def calculateElapsedTime(startTime, EndTime):
    return round(EndTime - startTime , 2)


def main():
    startTime = getCurrentTime()
    seconds = input("Please input desired seconds to sleep:  ")
    seconds = int(seconds)
    lets_sleep(seconds)
    endTime = getCurrentTime()
    timeElapsed = calculateElapsedTime(startTime, endTime)
    print(f'Finished in {timeElapsed} second(s)...')

if __name__ == "__main__":
    main()
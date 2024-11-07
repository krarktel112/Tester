import time

def countdown(t):
    """
    This function counts down from a given time in seconds.
    """

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time is up!')

if __name__ == '__main__':
    # Set the time in seconds (24 hours = 86400 seconds)
    t = 86400 

    countdown(t)
import time
import datetime

write_timer = '0:10:00'


def timer(write_timer, n):

    while n > 0:
        time.sleep(1)
        n = n - 1
        write_timer = str(datetime.timedelta(seconds=n))
        return write_timer, n
        if n == 0:
            print("Time's up. Press Continue to edit")

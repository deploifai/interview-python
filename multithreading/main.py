from timer import Timer
from init import init
import requests

# Task
# 1. send a request to each url in the list l
# each url is of the form: https://via.placeholder.com/{size}
# where size is the size of the image in pixels
# 2. print out the response data size
# 3. check the amount of time required to run that code


def single_thread(l):
    pass


def multi_thread(l):
    pass


def run(fn, l):
    timer = Timer()
    timer.start()
    print('timer started:', timer.start_time)

    fn(l)

    timer.stop()
    print('duration:', timer.duration)


def main():
    l = init(10)

    run(single_thread, l)
    # replace single_thread with multi_thread to run the multi_thread function


if __name__ == "__main__":
    main()

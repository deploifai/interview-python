from timer import Timer
from init import init
import requests


# Tasks
# 1. in the single_thread function, send a request to each url in the list l
# each url is of the form: https://via.placeholder.com/{size}
# where size is the size of the image in pixels

# 2. check the amount of time required to run that single_thread function

# 3. in the multi_thread function, write some multithreaded code
# to speed up the url fetching process


def single_thread(l):
    pass


def multi_thread(l):
    pass


def run(fn, l):
    timer = Timer()
    timer.start()
    print('timer started:', timer.start_time)
    print('running function:', fn.__name__)

    fn(l)

    timer.stop()
    print('duration:', timer.duration)


def main():
    l = init(10)

    run(single_thread, l)
    # run(multi_thread, l)
    # comment out code to choose which function to run


if __name__ == "__main__":
    main()

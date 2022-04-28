import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.duration = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        stop_time = time.time()
        self.duration = stop_time - self.start_time
        return self.duration

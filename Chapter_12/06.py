import threading
import requests
import time
from typing import List


class CustThread(threading.Thread):
    """Wrapper for threading.Thread, to run our HTML requests"""
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.result = f'{self.url}: Timeout'

    def run(self):
        res = requests.get(self.url)
        self.result = f'{self.url}: {res.text}'


class RequestHandler:
    """Handler for our list of threads, with built in timeout"""
    def __init__(self, threads: List[CustThread], timeout=None):
        """

        Args:
            threads: List of CustThread threads, to send our http get requests
            timeout: timeout interval for primary function .handle()
        """
        self.threads = threads
        self.timeout = timeout if timeout else 5
        self.update_interval = 0.01

    @property
    def _threads_running(self):
        return sum([1 if thread.isAlive() else 0 for thread in self.threads])

    def _start_threads(self):
        for t in self.threads:
            t.setDaemon(True)
            t.start()

    def handle(self):
        self._start_threads()
        while self._threads_running and self.timeout > 0:
            self.timeout -= self.update_interval
            time.sleep(self.update_interval)
        for thread in self.threads:
            print(thread.result)


def main():
    urls = [
        'http://httpstat.us/200',
        'http://httpstat.us/200?sleep=4000',
        'http://httpstat.us/200?sleep=20000',
        'http://httpstat.us/400',
        'http://httpstat.us/404',
        'http://httpstat.us/408',
        'http://httpstat.us/500',
        'http://httpstat.us/524'
    ]

    thrstart = time.time()
    handler = RequestHandler([CustThread(url) for url in urls])
    handler.handle()
    thrstart = format(time.time() - thrstart, 'f')
    print('✔️ Custom Thread class run time   :', thrstart)


if __name__ == '__main__':
    main()

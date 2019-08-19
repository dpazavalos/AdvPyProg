import threading
import requests
import time


class CustThread(threading.Thread):
    """Wrapper for Thread, to handle our HTML requests"""
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.result = None

    def run(self):
        res = requests.get(self.url)
        self.result = f'{self.url}: {res.text}'


urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524'
]

thrstart = time.time()
threads = [CustThread(url) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    pass
    thread.join()
for thread in threads:
    print(thread.result)

thrstart = format(time.time() - thrstart, 'f')
print('✔️ Custom Thread class run time   :', thrstart)

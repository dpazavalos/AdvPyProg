import threading
import requests
import time


def ping(url):
    res = requests.get(url)
    print(f'{url} : {res.text}')


urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524'
]


if __name__ == '__main__':
    # Sequential run
    seqstart = time.time()
    [ping(url) for url in urls]
    seqstart = format(time.time() - seqstart, 'f')
    print('✔️ Sequential run time :', seqstart, end='\n\n')

    # multi threaded run
    thrstart = time.time()
    threads = []
    for url in urls:
        ping_thread = threading.Thread(target=ping, args=(url,))
        threads.append(ping_thread)
        ping_thread.start()
    for thread in threads:
        thread.join()
    thrstart = format(time.time() - thrstart, 'f')
    print('✔️ Threaded run time   :', thrstart, end='\n\n')

    print(f'Squental -vs- Threaded')
    print(f'{seqstart} -::- {thrstart}')

import threading
import time
import string


class LockNamed:
    """Custom wrapper for threading.Lock, contains name (cannot subclass .Lock)"""
    def __init__(self, name: str):
        self.name = name
        self._locked = False
        self._lock = threading.Lock()

    def acquire(self):
        self._lock.acquire()
        self._locked = True

    def release(self):
        self._lock.release()
        self._locked = False

    def locked(self):
        self._lock.locked()

    @property
    def is_locked(self):
        return self._locked


class Locked:
    def __init__(self):
        self.lock_1 = LockNamed('Lock 1')
        self.lock_2 = LockNamed('Lock 2')

    def work_locks(self, thread_name, lock_1=None, lock_2=None):
        """Avoid deadlock by calling locks in same order"""
        if not lock_1:
            lock_1 = self.lock_1
        if not lock_2:
            lock_2 = self.lock_2
        self.acquire_lock(thread_name, lock_1)
        self.acquire_lock(thread_name, lock_2)
        self.release_locks(thread_name, lock_1, lock_2)

    def locks_opposite_a(self, thread_name):
        """Explicitly call work_locks in opposition to sibling function, in order to cause deadlock"""
        self.work_locks(thread_name, self.lock_1, self.lock_2)

    def locks_opposite_b(self, thread_name):
        """Explicitly call work_locks in opposition to sibling function, in order to cause deadlock"""
        self.work_locks(thread_name, self.lock_2, self.lock_1)

    @staticmethod
    def acquire_lock(thread: str, lock: LockNamed):
        while lock.is_locked:
            print(f'⚠️ Thread {thread} awaiting {lock.name} ')
            time.sleep(5)
        lock.acquire()
        print(f'✔️ Thread {thread} Acquired {lock.name}!')
        time.sleep(2)

    @staticmethod
    def release_locks(thread: str, *locks: LockNamed):
        for lock in locks:
            lock.release()
        print(f'🔵 Thread {thread} releasing locks')

    def main(self):
        letters = string.ascii_uppercase
        threads = []

        work = True
        if work:
            # Works, by calling locks in parallel
            for i in range(10):
                threads.append(
                    threading.Thread(target=self.work_locks, args=(letters[i],))
                )
        else:
            # Deadlocks, by calling locks in opposite order (philosopher's table)
            threads.append(threading.Thread(target=self.locks_opposite_a, args=('A',)))
            threads.append(threading.Thread(target=self.locks_opposite_b, args=('B',)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()


if __name__ == '__main__':
    locked = Locked()
    locked.main()

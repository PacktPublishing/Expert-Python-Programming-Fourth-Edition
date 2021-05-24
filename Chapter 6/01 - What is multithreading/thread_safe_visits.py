from threading import Thread, Lock

thread_visits = 0
thread_visits_lock = Lock()


def visit_counter():
    global thread_visits
    for i in range(100_000):
        with thread_visits_lock:
            thread_visits += 1


if __name__ == "__main__":
    thread_count = 100
    threads = [Thread(target=visit_counter) for _ in range(thread_count)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"{thread_count=}, {thread_visits=}")

from threading import Thread

thread_visits = 0


def visit_counter():
    global thread_visits
    for i in range(100_000):
        # value = thread_visits
        # thread_visits = value + 1
        thread_visits += 1


if __name__ == "__main__":
    thread_count = 100
    threads = [Thread(target=visit_counter) for _ in range(thread_count)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"{thread_count=}, {thread_visits=}")

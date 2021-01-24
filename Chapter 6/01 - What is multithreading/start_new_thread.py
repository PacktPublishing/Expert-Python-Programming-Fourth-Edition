from threading import Thread


def my_function():
    print("printing from thread")


if __name__ == "__main__":
    thread = Thread(target=my_function)
    thread.start()
    thread.join()

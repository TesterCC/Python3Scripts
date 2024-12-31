import threading


# target function
def threat_count(count):
    print(f"I am the thread number {count}.")
    # print(f"Current threading name is : {threading.current_thread().getName()}")  # before python 3.10
    print(f"Current threading name is : {threading.current_thread().name}")  # after python 3.10


for i in range(1, 7):
    t = threading.Thread(target=threat_count, args=(i,))
    # launch threading
    t.start()
    # 阻塞当前线程，直至其调用对象阻塞为止，join()从主线程中调用，一旦调用，join()方法将防止主线程比其调用线程先退出
    t.join()
print("Main thread exiting now...")
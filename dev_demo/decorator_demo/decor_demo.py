import time

def count_runtime(func):
    # support python2 and python3
    def wrapper(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        print('[+] Function name <%s> , run time: %s seconds' % (func.__name__, time.time() - s))
        return result
    return wrapper

@count_runtime
def print_info():
    print("This is print_info test.")

# test count_runtime decorator
if __name__ == '__main__':
    print_info()
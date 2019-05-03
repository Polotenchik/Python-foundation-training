import datetime as dt
import functools

def log(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        #print("{}: Starting {}.".format(dt.datetime.now(), func.__name__))
        print("Arguments were: {} and {}.".format(args, kwargs))
        #start = dt.datetime.now()
        #res = func(*args, **kwargs)
        #end = dt.datetime.now()
        #running_time = (end - start).seconds
        #print("{}: I'm done. Took {} seconds to finish.".format(dt.datetime.now(), running_time))
        #return res

    return wrap


@log
def foo(a, b, c):
    return a + b + c

foo(1, 2, c=3)

input()
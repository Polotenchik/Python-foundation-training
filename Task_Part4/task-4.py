import datetime as dt
import functools 
import inspect

def log(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        startTime =  dt.datetime.now()

        inp_args = inspect.getfullargspec(func)
        params = inp_args[0]
        params_dict = dict(enumerate(params))
        list = []
        for p_key in params_dict:
            list.append(params_dict[p_key])
        lenList = list[:len(args)]


        # heavy operation
        BIG_NUMBER = str(2**1000000)

        output = ''
        output += func.__name__ + ';'
        if args:
            output += ' args: '+ ', '.join('%s=%r' % (lenList[i], args[i]) for i in range(0, len(lenList))) + ';'
        if kwargs:
            output += ' kwargs: ' + ', '.join('%s=%r' % (key, value) for key, value in kwargs.items()) + ';'

        endTime = dt.datetime.now()
        execTime = (endTime - startTime).seconds
        output += ' execution time: ' + str(float(execTime)) + ' sec.'

        print(output)

    return wrap


@log
def foo(a, b, c):
    return a + b + c

@log
def bar(a, b, c, d):
    return a + b + c - d

@log
def spam(a):
    return a

foo(1, 2, c=3)
foo(1, 2)
bar(1, 2, c = 3, d = 4)
spam(a = 42)

input()
# pytest_sampler




Function Decorators
-------------------

In Python, a function decorator is a function that takes a function as
input, and returns another function.  They are typically used to expand
the functionality of other functions.  For instance:

```
import time

def timer(func):
    def timed_func(*args, **kwargs):
        t = time.time()
        ret = func(*args, **kwargs)
        print('Function {} took {:.2e}s.'.format(func.__name__,
                                                 time.time() - t))
        return ret
    return timed_func

@timer
def count_to_n(n):
    for j in range(n):
        pass
```

The *decorated* `count_to_n` is equivalent to writing:

```
def count_to_n(n):
    for j in range(n):
        pass

count_to_n = timer(count_to_n)
```

Either way, we can now run things like:

```
>>> count_to_n(1000)
Function count_to_n took 5.51e-05s.
>>> count_to_n(1000000)
Function count_to_n took 3.30e-02s.
```

Decorators are used in many place by py.test, to alter the behavior of
test functions in several ways.



Test Fixtures
-------------

A fixture is a resource that is needed to

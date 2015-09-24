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


Skipping Tests
--------------
`pytest.mark.skipif` is a function decorator that can be used to mark
tests to be skipped:

```
import pytest

@pytest.mark.skipif
def test_i_am_unconditionally_skipped_without_reason():
    print('Nothing to see here, we are being skipped')
```

Aside from a function to decorate, decorators can take extra parameters,
in the case of `skipif`, a boolean expression indicating whether the
test should be skipped or not, as well as a an optional `reason` keyword
argument taking a string that explains, well the reason for skipping the
test.  Both arguments are optional, with the default behavior being to
skip the test:

```
@pytest.mark.skipif(True, reason='testing skip works')
def test_i_am_being_skipped():
    print('Nothing to see here, I am being skipped')

@pytest.mark.skipif(False, reason='testing not skipping works')
def test_i_am_not_being_skipped():
    print('Look at me, I am not being skipped')

@pytest.mark.skipif(reason='testing skip by default')
def test_yet_another_skipped_test():
    print('Nothing to see here, I am being skipped')
```

There is a chance you will not know if a test has to be skipped until
you have started running the tests, e.g. perhaps you need to check the
FW version of a device you only connect to during the test.  You can
also skip tests from within, a.k.a. imperative skipping, by calling the
function `pytest.skip`:

```
def test_skipping_halfway_through():
    print('This code will be run...')
    pytest.skip('trying imperative skipping out')
    print('...but we will never make it to here.')
```

All of these examples are in the `test_skipif` folder, inside file
'test_1.py'.  Running `py.test` on that folder:

```
py.test -v test_skipif
============================= test session starts ==============================
platform darwin -- Python 2.7.10, pytest-2.8.0, py-1.4.30, pluggy-0.3.1 -- /Users/jaimefrio/miniconda/envs/numpydev/bin/python
cachedir: test_skipif/.cache
rootdir: /Users/jaimefrio/open_source/pytest_sampler/test_skipif, inifile:
collected 5 items

test_skipif/test_1.py::test_i_am_unconditionally_skipped_without_reason SKIPPED
test_skipif/test_1.py::test_i_am_being_skipped SKIPPED
test_skipif/test_1.py::test_i_am_not_being_skipped PASSED
test_skipif/test_1.py::test_yet_another_skipped_test SKIPPED
test_skipif/test_1.py::test_skipping_halfway_through SKIPPED

===================== 1 passed, 4 skipped in 0.01 seconds ======================
```

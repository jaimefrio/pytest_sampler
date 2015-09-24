import pytest

@pytest.mark.xfail
def test_i_will_fail():
    assert False, 'I told you I was going to fail'

@pytest.mark.xfail(run=False)
def test_i_will_break_things_big_time():
    print('Use this to not run e.g. tests that segfault')

@pytest.mark.xfail(raises=IndexError)
def test_moronic_list_access():
    a = []
    assert a[1] == 5

@pytest.mark.xfail(raises=IndexError)
def test_moronic_dict_access():
    a = {}
    # dict access raises KeyError, not IndexError
    assert a[1] == 5

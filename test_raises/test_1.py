import pytest

def test_verbose_raises():
    try:
        raise ValueError('I am a graceful failure')
    except ValueError:
        assert True, 'what a graceful failure!'
    except:
        assert False, 'this is not the graceful failure you were looking for'
    else:
        assert False, 'success is just another form of failure'

def test_succint_raises():
    with pytest.raises(ValueError):
        raise ValueError('I am a graceful failure')

def test_succint_raises_graceful():
    with pytest.raises(ValueError) as exception_info:
        raise ValueError('I am a graceful failure')
    assert 'graceful' in str(exception_info.value), 'the failure was graceful'

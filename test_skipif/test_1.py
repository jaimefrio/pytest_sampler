import pytest

@pytest.mark.skipif
def test_i_am_unconditionally_skipped_without_reason():
    print('Nothing to see here, I am being skipped.')

@pytest.mark.skipif(True, reason='testing skip works')
def test_i_am_being_skipped():
    print('Nothing to see here, I am being skipped.')

@pytest.mark.skipif(False, reason='testing not skipping works')
def test_i_am_not_being_skipped():
    print('Look at me, I am not being skipped.')

@pytest.mark.skipif(reason='testing skip by default')
def test_yet_another_skipped_test():
    print('Nothing to see here, I am being skipped.')

def test_skipping_halfway_through():
    print('This code will be run...')
    pytest.skip('trying imperative skipping out')
    print('...but we will never make it to here.')

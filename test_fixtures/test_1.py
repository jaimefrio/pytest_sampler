import pytest

@pytest.fixture
def i_set_things_up():
    projector = {'status': 'doing fine',
                 'flashing': "dicts can't flash!"}
    return projector

def test_fixture_contents(i_set_things_up):
    assert i_set_things_up['status'] == 'doing fine'

def test_try_to_break_the_fixture_1(i_set_things_up):
    del i_set_things_up['flashing']

def test_try_to_break_the_fixture_2(i_set_things_up):
    assert i_set_things_up['flashing'] == "dicts can't flash!"

@pytest.fixture(scope='module')
def i_also_set_things_up():
    projector = {'status': 'doing fine',
                 'flashing': "dicts can't flash!"}
    return projector

def test_try_to_break_the_module_fixture_1(i_also_set_things_up):
    del i_also_set_things_up['flashing']

def test_try_to_break_the_module_fixture_2(i_also_set_things_up):
    assert i_also_set_things_up['flashing'] == "dicts can't flash!"

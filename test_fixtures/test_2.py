import pytest

@pytest.fixture
def i_set_things_up(request):
    projector = {'status': 'doing fine',
                 'flashing': "dicts can't flash!"}
    def fin():
        projector['status'] = 'torn down by finalizer!'
    request.addfinalizer(fin)
    return projector

def test_nothing(i_set_things_up):
    assert i_set_things_up['status'] == 'doing fine'

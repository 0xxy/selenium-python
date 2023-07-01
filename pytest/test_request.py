import pytest
 
@pytest.fixture
def setup(request):
    print (request.fixturename)
    print (request.scope)
    print (request.function.__name__)
    print (request.cls)
    print (request.module.__name__)
    print (request.fspath)
    
def test_1(setup):
    assert True
 
class TestClass():
    def test_2(self, setup):
        assert True
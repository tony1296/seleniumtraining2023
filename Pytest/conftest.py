import pytest

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level teardown")

@pytest.fixture(scope="class")

def oneTimeSetUp(request, browser):
    print("Running one time setup")
    if browser == 'Chrome':
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on Chrome")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print("Running one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
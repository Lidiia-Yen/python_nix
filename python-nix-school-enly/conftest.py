import pytest


def pytest_addoption(parser):
    parser.addoption("--rounding_index", default=4)


@pytest.fixture()
def get_rounding_index(request):
    rounding_index = request.config.getoption("--rounding_index")
    return rounding_index


def pytest_configure(config):
    config.addinivalue_line("markers", "add: mark test to run tests only for Add operation")
    config.addinivalue_line("markers", "subtract: mark test to run tests only for Subtract operation")
    config.addinivalue_line("markers", "multiply: mark test to run only for Multiply operation")
    config.addinivalue_line("markers", "divide: mark test to run only for Divide operation")
    config.addinivalue_line("markers", "square_root: mark test to run only for Square_root operation")

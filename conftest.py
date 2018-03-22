import pytest
import json
import os.path
from fixture.application import MyApplication

fixture = None
target = None


def load_config(c_file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), c_file)
        with open(config_file) as f:
            target = json.load(f)
    return target


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")


@pytest.fixture()
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))
    if fixture is None:
        fixture = MyApplication(web_config["path_to_app"], web_config["main_window_header"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

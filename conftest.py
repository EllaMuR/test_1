import pytest
import requests
from fixture.application import Application
import json
import os.path



fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid() :
        fixture = Application(browser=browser, config=config) #, username=web_config["username"], password=web_config["password"]
        fixture.session.login(username=config["login_info"]["username"], password=config["login_info"]["password"])

    return fixture

@pytest.fixture
def api_client():
    return requests.Session()

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption('--target', action='store', default='target.json')



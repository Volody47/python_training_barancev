import pytest
import jsonpickle
import json
import os.path
from fixture.application import Application
from fixture.db import Dbfixture


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config_file:
            target = json.load(config_file)
    return target


@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))["web"]
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture

@pytest.fixture
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = Dbfixture(host=db_config["host"], name=db_config["database"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="remote")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            test_group_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_group_data, ids=[str(x) for x in test_group_data])



def load_from_json(file):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "resourses/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

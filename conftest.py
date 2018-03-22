import pytest
import json
import os.path
from fixture.application import MyApplication
import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel


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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
           testdata = load_from_xlsx(fixture[5:])
           metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_xlsx(x_file):
    data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.xlsx" % x_file)
    excel = Excel.ApplicationClass()
    workbook = excel.Workbooks.Open(data_file)
    sheet = workbook.ActiveSheet
    data = []
    sheet.Rows.ClearFormats()
    rows_with_data = sheet.UsedRange.Rows.Count
    for i in range(rows_with_data):
        data.append(str(sheet.Range["A%s" % (i + 1)].Value2))
    workbook.Close(SaveChanges=False)
    excel.Quit()
    return data

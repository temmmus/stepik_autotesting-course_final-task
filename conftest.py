import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):

    browser_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
	
    yield browser
    print("\nquit browser..")
    # time.sleep(1000)
    browser.quit()

	
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--user_language', action='store', default=None,
                     help='Choose from lags en/ru/fr..')

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('user_language')
    browser = None

    if browser_name == 'chrome':
        options = ChromeOptions()
        options.add_argument(f'--lang={user_language}')

        print('\nstart chrome browser for test..')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', user_language)

        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome of firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()

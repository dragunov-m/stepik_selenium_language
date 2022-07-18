import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help="Choose browser: chrome or firefox"
        )
    parser.addoption(
        '--language',
        action='store',
        default='ru',
        help='Choose language'
        )


@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption('browser_name')
    user_languages = request.config.getoption('language')

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_languages})
        print("\nstart browser for test..")
        chrome_service = Service(executable_path='/home/user/chromedriver')
        driver = webdriver.Chrome(options=options, service=chrome_service)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_languages)
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(firefox_profile=fp)
        driver.implicitly_wait(5)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    yield driver
    print("\nquit browser..")
    driver.quit()

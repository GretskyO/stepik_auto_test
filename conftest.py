import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action = 'store', default = None, help = 'Choose language for browser')


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    browser = None
    options = Options()

    if user_language == 'en-gb':
        print(f"Browser start with {user_language} language")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif user_language == 'ru':
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif user_language == 'fr':
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif user_language == 'es':
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be en-gb or ru or fr or es")
    yield browser
    print("\nquit browser..")
    browser.quit()

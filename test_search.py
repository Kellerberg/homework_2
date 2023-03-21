import pytest
import random
from selene.support.shared import browser
from selene import be, have

random.seed()

random_requst = ""

def enter_random_request():
    global random_requst
    for x in range(13):
        random_requst = random_requst + random.choice(list('12345678909qwertyuiopasdfghjklzxcvbnm'))
    return random_requst

@pytest.fixture
def set_browser_configuration():
    browser.config.browser_name = 'firefox'
    browser.open('https://www.google.com/webhp?hl=en')
    browser.driver.maximize_window()
    browser.config.hold_browser_open = True

def test_search_positive(set_browser_configuration):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_negative(set_browser_configuration):
    search_term = enter_random_request()
    browser.element('[name="q"]').should(be.blank).type(search_term).press_enter()
    assert browser.element('body').should(have.text('did not match any documents'))
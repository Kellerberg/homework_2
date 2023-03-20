import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def set_browser_configuration():
    browser.config.browser_name = 'firefox'
    browser.open('https://google.com')
    browser.driver.maximize_window()
    browser.config.hold_browser_open = True


def test_search_positive(set_browser_configuration):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

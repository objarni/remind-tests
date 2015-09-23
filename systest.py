# coding: utf-8

# Standard
import sys

# Local
from browser import BrowserSimulator
from browser import wait_for_title
from browser import wait_for_text


def test_end_to_end(url):
    try:
        browser = BrowserSimulator()
        browser.go_to(url)
        browser.fill_in('email', 'test@test.com')
        browser.click_button('collect')
        wait_for_title(browser, 'Collect')
        browser.fill_in('note', 'hej')
        browser.click_button('save')
        wait_for_text(browser, 'message', 'Sparat.')
        browser.click_link('logout')
        wait_for_title(browser, 'Re:Mind')

    except Exception, e:
        print e
    browser.close_browser()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Expected a single argument 'URL', aborting."
    else:
        url = sys.argv[1]
        test_end_to_end(url)

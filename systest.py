# coding: utf-8

# Standard
import sys

# Local
from browser import BrowserSimulator
from browser import wait_for_title
from browser import wait_for_text
from browser import wait_for_text_gone


def test_end_to_end(url):
    try:
        browser = BrowserSimulator()

        # first clear out test data via backend testing API
        # /deltestdata clears data for test@test.com email
        # TODO: how avoid hard-coding backend endpoint
        # elegantly?
        browser.go_to('http://localhost:5000/deltestdata')

        # now start script on landing page
        browser.go_to(url)
        wait_for_title(browser, 'Re:Mind')

        # use test email adress for whole script
        browser.fill_in('email', 'test@test.com')

        # go to collect page
        browser.click_button('collect')
        wait_for_title(browser, 'Collect')

        # enter & save some data
        browser.fill_in('note', 'hej')
        browser.click_button('save')
        wait_for_text(browser, 'message', 'Sparat.')

        # go back to landing page
        browser.click_link('logout')
        wait_for_title(browser, 'Re:Mind')

        # go view the added data
        browser.fill_in('email', 'test@test.com')
        browser.click_button('process')
        wait_for_title(browser, 'Process')

        # verify data is there
        wait_for_text(browser, 'top', 'hej')

        # remove data & verify it's gone
        browser.click_button("remove_top")
        wait_for_text_gone(browser, 'top', 'hej')

        print "##############################"
        print "### ALL DONE SCRIPT PASSED ###"
        print "##############################"
        browser.close_browser()

    except Exception, e:
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "!!! Attention! Regression script didn't finish! Exception:"
        print e


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Expected a single argument 'URL', aborting."
    else:
        url = sys.argv[1]
        test_end_to_end(url)

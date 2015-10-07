# coding: utf-8

# Standard
import sys

# Local
from browser import BrowserSimulator


def test_end_to_end(url, headless=True):
    try:
        print "Regression script running."
        browser = BrowserSimulator(headless)

        # first clear out test data via backend testing API
        # /deltestdata clears data for test@test.com email
        # TODO: how avoid hard-coding backend endpoint
        # elegantly?
        browser.go_to('http://localhost:5000/deltestdata')

        # now start script on landing page
        browser.go_to(url)
        browser.verify_title('Re:Mind')

        # use test email adress for whole script
        browser.fill_in('email', 'test@test.com')

        # go to collect page
        browser.click_button('collect')
        browser.verify_title('Collect')

        # enter & save some data
        browser.fill_in('note', 'hej')
        browser.click_button('save')
        browser.verify_text('message', 'Sparat.')

        # go back to landing page
        browser.click_link('logout')
        browser.verify_title('Re:Mind')

        # go view the added data
        browser.fill_in('email', 'test@test.com')
        browser.click_button('process')
        browser.verify_title('Process')

        # verify data is there
        browser.verify_text('top', 'hej')

        # remove data & verify it's gone
        browser.click_button("remove_top")
        browser.verify_text_gone('top', 'hej')

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
        test_end_to_end(url, headless=True)

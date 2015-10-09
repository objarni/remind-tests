# coding: utf-8

# Standard
import sys

# Local
from browser import BrowserSimulator

TESTACCOUNT = "test@test.com"
TESTPASSWORD = "testtest123"


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

        # Create test account
        create_test_account(browser)

        # Login to test account

        # Run regression script
        run_basic_usage_scenario(browser)

        # Delete test account

        print "##############################"
        print "### ALL DONE SCRIPT PASSED ###"
        print "##############################"
        browser.close_browser()

    except Exception, e:
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "!!! Attention! Regression script didn't finish! Exception:"
        print e


def create_test_account(browser):
    browser.click_link("signup")
    browser.verify_title("Skapa konto")
    browser.fill_in('email', TESTACCOUNT)
    browser.fill_in('password', TESTPASSWORD)
    browser.click_button('signup')
    browser.verify_text("message", "Konto skapat")
    browser.verify_title("Logga in")


def run_basic_usage_scenario(browser):
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


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Expected a single argument 'URL', aborting."
    else:
        url = sys.argv[1]
        test_end_to_end(url, headless=True)

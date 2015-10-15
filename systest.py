# coding: utf-8

# Standard
import sys

# Local
from browser import BrowserSimulator

TESTACCOUNT = "test@test.com"
TESTPASSWORD = "test123"


def info(s):
    print "\n%s" % s.upper()
    print "=" * len(s)


def test_end_to_end(url, headless=True):
    try:
        info("Regression script running.")
        browser = BrowserSimulator(headless)

        info('Clear old test data')
        browser.go_to('http://localhost:5000/deltestdata')

        info("Going to landing page")
        browser.go_to(url)
        browser.verify_title('Re:Mind')

        info("Create test account")
        create_test_account(browser)

        info("Login with test account")
        login_to_test_account(browser)

        info("Run basic usage scenario")
        run_basic_usage_scenario(browser)

        # Delete test account
        # delete_test_account(browser)

        print ""
        print "##############################"
        print "### ALL DONE SCRIPT PASSED ###"
        print "##############################"
        browser.close_browser()

    except Exception, e:
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "!!! Attention! Regression script didn't finish! Exception:"
        print unicode(e.message).encode('utf-8')


def create_test_account(browser):

    def create_flow():
        browser.click_link("signup")
        browser.verify_title("Skapa konto")
        browser.fill_in('email', TESTACCOUNT)
        browser.fill_in('password', TESTPASSWORD)
        browser.click_button('signup')

    create_flow()
    browser.verify_text("message", "Konto skapat")

    info('Verify not possible re-create same account')
    create_flow()
    browser.verify_text("message", "Kontot finns redan!")


def login_to_test_account(browser):
    browser.click_link('login')

    info('Verify wrong p/w does not login')
    browser.fill_in('email', TESTACCOUNT)
    browser.fill_in('password', TESTPASSWORD * 2)
    browser.click_button("login")
    browser.verify_text('message',
                        u"Fel epost eller lösenord. Försök igen.")

    info('Now login with correct p/w')
    browser.fill_in('password', TESTPASSWORD)
    browser.click_button("login")
    browser.verify_text('message', u'Välkommen!')
    browser.verify_title('Collect')


def run_basic_usage_scenario(browser):
    info("Collect a thought")
    browser.fill_in('note', 'hej')
    browser.click_button('save')
    browser.verify_text('message', 'Sparat.')

    info("Process the thought")
    browser.click_link('process')
    browser.verify_title('Process')
    browser.verify_text('top', 'hej')
    browser.click_button("remove_top")
    browser.verify_text_gone('top', 'hej')

# TODO: rename 'note' to 'thought' everywhere!

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Expected a single argument 'URL', aborting."
    else:
        url = sys.argv[1]
        test_end_to_end(url, headless=True)

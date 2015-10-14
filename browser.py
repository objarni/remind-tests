# coding: utf-8

# Standard
import time

# Third party
from selenium import webdriver


class BrowserSimulator():

    def __init__(self, headless=True):
        if headless:
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(800, 600))
            display.start()
        self.driver = webdriver.Firefox()

    def go_to(self, url):
        print u"Going to %s. " % url
        self.driver.get(url)

    def fill_in(self, name, text):
        print u"Writing '%s' in textarea named '%s'." % (text, name)
        e = self.driver.find_element_by_name(name)
        e.clear()
        e.send_keys(text)

    def click_button(self, name):
        print u"Clicking button named '%s'." % name
        e = self.driver.find_element_by_name(name)
        e.click()

    def click_link(self, id):
        print u"Clicking link '%s'." % id
        e = self.driver.find_element_by_id(id)
        e.click()

    def get_title(self):
        print u"Title is '%s'." % self.driver.title
        return self.driver.title

    def get_text(self, id):
        e = self.driver.find_element_by_id(id)
        text = e.text
        print u"Element '%s' text is '%s'." % (id, text)
        return text

    def verify_title(self, title):
        def condition():
            return self.get_title() == title
        wait_for(condition, u"Expected title to show up: " + title)

    def verify_text(self, id, text):
        def condition():
            return text in self.get_text(id)
        wait_for(condition, u"Expected text to show up: " + text)

    def verify_text_gone(self, id, text):
        def condition():
            return text not in self.get_text(id)
        wait_for(condition, u"Expected text to disappear: " + text)

    def close_browser(self):
        print "Closing browser."
        self.driver.close()


def wait_for(predicate, exception_text):
    timeout = 3
    acc = 0
    while acc < timeout:
        if predicate():
            return
        time.sleep(1)
        acc += 1
    raise Exception(exception_text)

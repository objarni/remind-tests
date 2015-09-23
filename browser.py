# coding: utf-8

# Standard
import time

# Third party
from selenium import webdriver


class BrowserSimulator():

    def __init__(self):
        self.driver = webdriver.Firefox()

    def go_to(self, url):
        print "Going to %s. " % url
        self.driver.get(url)

    def fill_in(self, name, text):
        print "Writing '%s' in textarea named '%s'." % (text, name)
        e = self.driver.find_element_by_name(name)
        e.send_keys(text)

    def click_button(self, name):
        print "Clicking button named '%s'." % name
        e = self.driver.find_element_by_name(name)
        e.click()

    def click_link(self, id):
        print "Clicking link '%s'." % id
        e = self.driver.find_element_by_id(id)
        e.click()

    def get_title(self):
        print "Title is '%s'." % self.driver.title
        return self.driver.title

    def get_text(self, id):
        e = self.driver.find_element_by_id(id)
        text = e.text
        print "Element '%s' text is '%s'." % (id, text)
        return text

    def close_browser(self):
        print "Closing browser."
        self.driver.close()


def wait_for_title(browser, title):
    timeout = 3
    acc = 0
    while acc < timeout:
        if browser.get_title() == title:
            return
        time.sleep(1)
        acc += 1
    raise Exception("Expected title to show up: " + title)


def wait_for_text(browser, id, text):
    timeout = 3
    acc = 0
    while acc < timeout:
        if text in browser.get_text(id):
            return
        time.sleep(1)
        acc += 1
    raise Exception("Expected text to show up: " + text)

from pages.demoqa import DemoQA
import time


def test_size(browser):
    size_demo = DemoQA(browser)
    size_demo.visit()
    browser.set_window_size(1000, 30)
    time.sleep(2)
    browser.set_window_size(1000, 1000)

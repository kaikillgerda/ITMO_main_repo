from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_navigation(browser):
    practice_page = DemoQA(browser)
    el_practice_page = ElementsPage(browser)
    practice_page.visit()
    practice_page.btn_elements.click()
    el_practice_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    el_practice_page.equal_url()


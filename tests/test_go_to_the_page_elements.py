from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_go_to_the_page_elements(browser):
    any_page = DemoQA(browser)
    page_demo = ElementsPage(browser)
    any_page.visit()
    assert any_page.equal_url()
    any_page.btn_elements.click()
    assert page_demo.equal_url()

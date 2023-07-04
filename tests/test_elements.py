from pages.elements_page import ElementsPage
from components.components import WebElement


def test_find_elements(browser):
    test_find_elem = ElementsPage(browser)
    test_find_elem.visit()
    assert test_find_elem.btns_first_menu.check_count_elements(9)

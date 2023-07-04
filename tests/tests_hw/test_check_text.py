from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_check_text_footer_main(browser):
    text_page = DemoQA(browser)
    text_page.visit()
    assert text_page.text_footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
    text_page.btn_elements.click()
    elem_page_elem = ElementsPage(browser)
    assert elem_page_elem.text_center_elements.get_text() == "Please select an item from left to start practice."


def test_page_elements(browser):
    new_elem = ElementsPage(browser)
    new_elem.visit()
    assert new_elem.text_header_elements.get_text() == 'Elements'

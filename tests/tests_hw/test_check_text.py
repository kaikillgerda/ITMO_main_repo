from pages.demoqa import DemoQA


def test_check_text_footer_main(browser):
    text_page = DemoQA(browser)
    text_page.visit()
    assert text_page.text_footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


def test_check_text_center_elements(browser):
    elem_page = DemoQA(browser)
    elem_page.visit()
    elem_page.btn_elements.click()
    assert elem_page.text_center_elements.get_text() == "Please select an item from left to start practice."

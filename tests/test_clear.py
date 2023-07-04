from pages.text_box import TextBox
import time


def test_clear(browser):
    demo_page = TextBox(browser)
    demo_page.visit()
    demo_page.full_name.send_keys('Hi, Boris!')
    time.sleep(2)
    demo_page.full_name.clear()
    time.sleep(2)
    assert demo_page.full_name.get_text() == ''

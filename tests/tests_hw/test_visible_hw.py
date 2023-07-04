from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    demo_page = Accordion(browser)
    demo_page.visit()
    assert demo_page.lorem_field.visible()
    demo_page.lorem_btn.click()
    time.sleep(2)
    assert not demo_page.lorem_field.visible()

def test_visible_accordion_default(browser):
    demo_page_next = Accordion(browser)
    demo_page_next.visit()
    assert not demo_page_next.lorem_btn_1.visible()
    assert not demo_page_next.lorem_btn_2.visible()
    assert not demo_page_next.lorem_btn_self.visible()


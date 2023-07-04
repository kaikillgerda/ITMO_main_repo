from pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar(browser):
    sidebar = ElementsPage(browser)
    sidebar.visit()
    # sidebar.btn_first.click()
    # time.sleep(3)
    # assert sidebar.text_box_btn.exist()
    assert sidebar.text_box_btn_e.visible()


def test_not_visible_btn_sidebar(browser):
    sidebar_sec = ElementsPage(browser)
    sidebar_sec.visit()
    assert sidebar_sec.check_box_btn_e.visible()
    sidebar_sec.btn_first_e.click()
    time.sleep(1)
    assert not sidebar_sec.check_box_btn_e.visible()

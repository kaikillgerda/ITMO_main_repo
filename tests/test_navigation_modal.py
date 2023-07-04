from pages.modal_dialogs import ModalDialogs


def test_navigation_modal(browser):
    test_modal_elements = ModalDialogs(browser)
    test_modal_elements.visit()
    test_modal_elements.refresh()
    test_modal_elements.icon_btn.click()
    test_modal_elements.back()
    browser.set_window_size(900, 400)
    test_modal_elements.forward()
    assert test_modal_elements.get_url() == 'https://demoqa.com/'
    assert test_modal_elements.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)

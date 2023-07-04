from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()
    assert modal_elements.btns_all.check_count_elements(5)
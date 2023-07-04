from pages.text_box import TextBox


def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

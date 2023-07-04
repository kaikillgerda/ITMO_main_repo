from pages.text_box import TextBox


def test_placeholder(browser):
    place_holder = TextBox(browser)
    place_holder.visit()
    assert place_holder.placeholder_btn.get_dom_attribute('placeholder') == 'Full Name'

from pages.demoqa import DemoQA


def test_seo(browser):
    title_get = DemoQA(browser)
    title_get.visit()
    assert title_get.get_title() == "DEMOQA"
    assert browser.title == "DEMOQA"  # это то же самое, что и на строке 6

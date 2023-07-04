from pages.web_tables import WebTables


def test_webtables(browser):
    demo_page = WebTables(browser)
    demo_page.visit()
    assert demo_page.no_rows_found.exist()
    while hero_page_add.del_btn_all.exist():
        hero_page_add.del_btn_all.click()
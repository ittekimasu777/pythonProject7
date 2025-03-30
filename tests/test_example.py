import allure


@allure.feature("Авторизация")
@allure.story("Вход в систему")
def test_login(browser):
    with allure.step("Открываем сайт"):
        browser.get("https://example.com")


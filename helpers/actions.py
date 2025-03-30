import allure

def click_element(driver, locator):
    with allure.step(f"Кликаем по {locator}"):
        driver.find_element(*locator).click()

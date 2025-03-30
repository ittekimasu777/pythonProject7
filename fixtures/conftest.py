import pytest
from selenium import webdriver
from logging_config import logger

@pytest.fixture(scope="function")
def browser():
    logger.info("Запускаем браузер")
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    logger.info("Закрываем браузер")

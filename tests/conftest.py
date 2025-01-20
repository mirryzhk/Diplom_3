import pytest
from selenium import webdriver
from urls import Urls

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver_instance = webdriver.Chrome()
    else:
        driver_instance = webdriver.Firefox()

    driver_instance.get(Urls.BASE_URL)
    yield driver_instance
    driver_instance.quit()
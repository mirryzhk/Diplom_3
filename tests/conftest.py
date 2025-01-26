import pytest
from selenium import webdriver
from urls import Urls
import stellar_burgers_api
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_password_page import RecoveryPasswordPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver_instance = webdriver.Chrome()
    else:
        driver_instance = webdriver.Firefox()
        driver_instance.get(Urls.BASE_URL)
    yield driver_instance
    driver_instance.quit()

@pytest.fixture(scope='function')
def default_user():
    user_body = stellar_burgers_api.create_user_body()
    user_response = stellar_burgers_api.create_user(user_body)
    access_token = stellar_burgers_api.get_access_token(user_response)
    yield {"user_data": user_body,
           "access_token": access_token,
           "user_response" : user_response
           }
    stellar_burgers_api.delete_user(access_token)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture
def personal_account_page(driver):
    return PersonalAccountPage(driver)

@pytest.fixture
def recovery_password_page(driver):
    return RecoveryPasswordPage(driver)
import pytest
from selenium import webdriver
from urls import Urls
import stellar_burgers_api

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
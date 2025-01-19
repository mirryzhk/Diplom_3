import allure
import helpers
from urls import Urls
import requests

@allure.step("Создание тела запроса создания юзера: email, password, name")
def create_user_body():
    return helpers.new_user_login_password()

@allure.step("Создание пользователя в приложении Stellar burger")
def create_user(user_data):
    user_response = requests.post(Urls.API_URL+Urls.CREATE_USER_ENDPOINT, json=user_data)
    return user_response

@allure.step("Получение access токена созданного пользователя")
def get_access_token(user_response):
    access_token = user_response.json().get("accessToken")
    return access_token

@allure.step("Удаление созданного пользователя")
def delete_user(access_token):
    headers = {"Authorization": access_token}
    response_delete = requests.delete(Urls.BASE_URL + Urls.DELETE_USER_ENDPOINT, headers=headers)
    return response_delete
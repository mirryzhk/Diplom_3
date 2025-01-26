from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from urls import Urls
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Открытие в браузере страницы 'Stellar Burger'")
    def open(self):
        self.open_page(Urls.BASE_URL)

    @allure.step("Клик по кнопке 'Лента заказов' в шапке страницы")
    def click_list_order_button(self):
        list_order_button = self.wait_and_find_element(MainPageLocators.LIST_ORDER_BTN)
        self.click_element(list_order_button)


    @allure.step("Клик по 'Ингредиенту' в 'Конструкторе'")
    def click_ingredient_button(self):
        ingredients_list = self.wait_and_find_element(MainPageLocators.INGREDIENT_LIST)
        ingredients = ingredients_list.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        second_ingredient = ingredients[1]
        self.click_element(second_ingredient)

    @allure.step("Клик по кнопке закрытия всплывающего окна")
    def close_ingredient_card(self):
        x_button = self.wait_and_find_element(MainPageLocators.X_BUTTON)
        self.click_element(x_button)

    @allure.step("Перемещение булки в зону создания бургера")
    def add_bun_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.BUN_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        self.drag_and_drop(source, target)

    @allure.step("Перемещение соуса в зону создания бургера")
    def add_sauce_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.SAUCE_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        self.drag_and_drop(source, target)

    @allure.step("Перемещение мяса в зону создания бургера")
    def add_meat_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.MEAT_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        self.drag_and_drop(source, target)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_create_order_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BTN)
        self.click_element(account_button)

    @allure.step("Получение количества ингредиентов из счётчика")
    def get_count_ingredient(self):
        counter_element = self.wait_and_find_element(MainPageLocators.COUNTER)
        return counter_element.text

    @allure.step("Получение эмейла для авторизации из сгенерированных данных")
    def get_user_email(self, user_response):
        email = user_response["email"]
        return email

    @allure.step("Получение пароля для авторизации из сгенерированных данных")
    def get_user_password(self, user_response):
        password = user_response["password"]
        return password

    @allure.step("Клик по кнопке 'Личный кабинет' в шапке страницы")
    def click_account_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.BUTTON_ACCOUNT)
        self.click_element(account_button)


    @allure.step("Клик по кнопке закрытия всплывающего окна")
    def click_order_card_x_button(self):
        x_button = self.wait_and_find_element(MainPageLocators.CLOSE_WINDOW_BTN)
        self.click_element(x_button)


    @allure.step("Получение номера оформленного заказа")
    def get_new_order_number(self):
        new_order_number_element = self.wait_for_element_text_to_change(
            MainPageLocators.NUMBER_NEW_ORDER,
            text = "9999",
            timeout=10)
        new_order_number = new_order_number_element.text
        return int(new_order_number)

    @allure.step("Проверка открытия карточки с информацией об ингредиенте")
    def check_ingredient_title(self):
        if self.is_element_present(MainPageLocators.INGREDIENT_TITLE) == True:
            return True

    @allure.step("Проверка закрытия карточки с информацией об ингредиенте")
    def check_main_page_title(self):
        if self.is_element_present(MainPageLocators.TITLE_MAIN_PAGE) == True:
            return True

    @allure.step("Открытие Главной страницы")
    def find_main_page_title(self):
        return self.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE)

    @allure.step("Открытие окна с деталями заказа")
    def find_create_order_description(self):
        return self.wait_and_find_element(MainPageLocators.CREATE_ORDER_DESCRIPTION)


    @allure.step("Сравнение URL текущей страницы с адресом страницы 'Лента заказов'")
    def check_order_list_url(self):
        return self.get_current_url() == (Urls.BASE_URL + Urls.LIST_ORDER_PAGE)

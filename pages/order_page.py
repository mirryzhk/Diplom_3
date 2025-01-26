from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure
from urls import Urls


class OrderPage(BasePage):

    @allure.step("Открытие окна с деталями заказа кликом по карточке заказа")
    def click_order_card(self):
        order_card = self.wait_and_find_element(OrderPageLocators.ORDER_CARD)
        self.click_element(order_card)


    @allure.step("Получение номера последнего заказа")
    def get_order_number(self):
        element = self.wait_and_find_element(OrderPageLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step("Получение значения счётчика заказов на странице 'Лента заказов'")
    def get_orders_counter(self):
        number = self.wait_and_find_element(OrderPageLocators.ORDER_COUNTER)
        return int(number.text)

    @allure.step("Клик по кнопке 'Конструктор' в шапке страницы")
    def click_constructor_button(self):
        constructor_button = self.wait_and_find_element(OrderPageLocators.CONSTRUCTOR_BTN)
        self.click_element(constructor_button)

    @allure.step("Получение значения счётчика заказов 'Выполнено за сегодня' на странице 'Лента заказов'")
    def get_orders_counter_today(self):
        number = self.wait_and_find_element(OrderPageLocators.ORDER_COUNTER_TODAY)
        return int(number.text)

    @allure.step("Получение номера заказа в разделе 'В работе' на экране Лента заказов'")
    def get_order_in_works_number(self):
        number_in_works = self.wait_and_find_element(OrderPageLocators.ORDER_IN_WORK)
        return int(number_in_works.text)

    @allure.step("Проверка открытия окна с деталями заказа")
    def check_open_window_with_order_details(self):
        return self.is_element_present(OrderPageLocators.INGREDIENT_IN_ORDER)

    @allure.step("Сравнение URL текущей страницы с адресом главной страницы")
    def check_main_page_url(self):
        return self.get_current_url() == Urls.BASE_URL
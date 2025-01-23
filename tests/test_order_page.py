from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.personal_account_page import PersonalAccountPage
import allure
import stellar_burgers_api

class TestOrderPage:
    @allure.title("Проверка успешного открытия окна с деталями заказа на 'Ленте заказов'")
    @allure.description("Проверка успешного перехода по кнопке 'Конструктор' в шапке сайта")
    def test_open_detail_order_window_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_list_order_button()
        order_page = OrderPage(driver)
        order_page.click_order_card()
        assert order_page.check_open_window_with_order_details()

    @allure.title("Проверка появления номера нового заказа на экране 'Лента заказов'")
    @allure.description("Создаём заказ и проверяем, что его номер появляется среди всех заказов на странице 'Лента заказов'")
    def test_order_in_order_list_success(self, driver, default_user):
        # Создаём и авторизуем нового пользователя
        user_data = default_user ['user_data']
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_enter_button()
        main_page.find_main_page_title()
        # Создаём заказ бургера с булкой соусом и мясом
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        main_page.click_order_card_x_button()
        # Переходим на экран "История заказов" и получаем номер последнего заказа
        main_page.find_main_page_title()
        main_page.click_account_button()
        personal_account_page.click_order_history_btn()
        order_number = personal_account_page.get_order_number()
        # Переходим на экран "Лента заказов" и получаем номер последнего заказа
        main_page.click_list_order_button()
        order_page = OrderPage(driver)
        order_number_in_list = order_page.get_order_number()
        assert order_number == order_number_in_list

    @allure.title("Проверка увеличения значения счётчика заказов на экране 'Лента заказов'")
    @allure.description(
        "Создаём заказ и проверяем что счётчик всех заказов на экране 'Лента заказов' увеличивается на 1")
    def test_order_counter_increases_when_new_order_is_placed_success(self, driver, default_user):
        # Создаём и авторизуем нового пользователя
        user_data = default_user ['user_data']
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_enter_button()
        main_page.find_main_page_title()
        # Получаем значение счётчика заказов на странице "Лента заказов"
        main_page.click_list_order_button()
        order_page = OrderPage(driver)
        counter_before = order_page.get_orders_counter()
        # Переходим в конструктор и создаём заказ
        order_page.click_constructor_button()
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        main_page.click_order_card_x_button()
        # Переходим на экран "Лента заказов" и получаем значение счётчика всех заказов
        main_page.click_list_order_button()
        counter_after = order_page.get_orders_counter()
        assert (counter_after - counter_before) == 1

    @allure.title("Проверка увеличения значения счётчика 'Выполнено за сегодня' на экране 'Лента заказов'")
    @allure.description(
        "Создаём заказ и проверяем что счётчик выполненных заказов за сегодня, на экране 'Лента заказов', увеличивается на 1")
    def test_order_counter_today_increases_when_new_order_is_placed_success(self, driver, default_user):
        # Создаём и авторизуем нового пользователя
        user_data = default_user ['user_data']
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_enter_button()
        main_page.find_main_page_title()
        # Получаем значение счётчика выполненных за сегодня заказов на странице "Лента заказов"
        main_page.click_list_order_button()
        order_page = OrderPage(driver)
        counter_before = order_page.get_orders_counter_today()
        # Переходим в конструктор и создаём заказ
        order_page.click_constructor_button()
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        main_page.click_order_card_x_button()
        # Переходим на экран "Лента заказов" и получаем значение счётчика выполненных за сегодня заказов
        main_page.click_list_order_button()
        counter_after = order_page.get_orders_counter_today()
        assert (counter_after - counter_before) == 1

    @allure.title("Проверка появления номера нового заказа на экране 'Лента заказов' в разделе 'В работе'")
    @allure.description(
        "Создаём заказ и проверяем что его номер отображается на экране 'Лента заказов' в разделе 'В работе'")
    def test_number_appears_in_progress_section_success(self, driver, default_user):
        # Соаздаём и авторизуемся новым пользователем
        user_data = default_user ['user_data']
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_enter_button()
        main_page.find_main_page_title()
        # Добавляем ингредиенты и создаём новый заказ. Получаем его номер и закрываем всплывающее окно.
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        new_order_number = main_page.get_new_order_number()
        main_page.click_order_card_x_button()
        # Переходим на экран "Лента заказов" и получаем номер заказа, попавшего столбец "В работе"
        main_page.click_list_order_button()
        order_page = OrderPage(driver)
        number_in_order_list = order_page.get_order_in_works_number()
        assert number_in_order_list == new_order_number
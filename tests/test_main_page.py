import allure


class TestMainPage:
    @allure.title("Проверка успешного перехода по кнопке 'Конструктор'")
    @allure.description("Проверка успешного перехода по кнопке 'Конструктор' в шапке сайта")
    def test_open_main_page_clicK_constructor_btn_success(self, main_page, order_page):
        main_page.open()
        main_page.click_list_order_button()
        order_page.click_constructor_button()
        current_url = order_page.check_main_page_url()
        assert current_url == True


    @allure.title("Проверка успешного перехода по кнопке 'Лента заказов'")
    @allure.description("Проверка успешного перехода по кнопке 'Лента заказов' в шапке сайта")
    def test_open_list_order_page_success(self, main_page):
        main_page.open()
        main_page.click_list_order_button()
        current_url = main_page.check_order_list_url()
        assert current_url == True

    @allure.title("Проверка успешного открытия всплывающего окна с информацией об ингредиенте")
    @allure.description("Проверка открытия всплывающего окна с информацией об ингредиенте после клика по Ингридиенту")
    def test_open_ingredient_card_success(self, main_page):
        main_page.open()
        main_page.click_ingredient_button()
        assert main_page.check_ingredient_title() == True

    @allure.title("Проверка успешного закрытия всплывающего окна с информацией об Ингридиенте")
    @allure.description("Проверка закрытия всплывающего окна с информацией об ингредиенте после клика по кнопке 'Крестик'")
    def test_close_ingredient_card_success(self, main_page):
        main_page.open()
        main_page.click_ingredient_button()
        main_page.close_ingredient_card()
        assert main_page.check_main_page_title() == True

    @allure.title("Проверка изменения количества ингредиента в счётчике при добавлении ингредиента в бургер")
    @allure.description("Проверка изменения счётчика ингредиента при добавлении его в конструктор бургера")
    def test_change_counter_add_constructor_success(self, main_page):
        main_page.open()
        count_before = main_page.get_count_ingredient()
        main_page.add_bun_in_order()
        count_after = main_page.get_count_ingredient()
        assert count_before == '0' and count_after == '2'

    @allure.title("Проверка успешного оформления заказа авторизованным пользователем")
    @allure.description("Авторизованный пользователь может успешно оформить заказ")
    def test_authorized_user_create_order_success(self, default_user, personal_account_page, main_page):
        user_data = default_user ['user_data']

        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()

        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_enter_button()

        main_page.find_main_page_title()
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        description_create_order = main_page.find_create_order_description()
        assert description_create_order.text == "Ваш заказ начали готовить"


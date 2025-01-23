from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_CARD = (By.XPATH, "//h2[text()='Люминесцентный традиционный-галактический краторный бургер']/..")
    INGREDIENT_IN_ORDER = (By.XPATH, "//div[contains(@class,'Modal_imgBox__27yrH')]//img[@alt='Соус традиционный галактический']")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "//h2[text()='Люминесцентный традиционный-галактический краторный бургер']/preceding-sibling::div/p[@class='text text_type_digits-default']")
    ORDER_COUNTER = (By.XPATH, "//div[@class='undefined mb-15']//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_READY_ORDER = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default')])[2]")
    ORDER_IN_WORK = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li[@class='text text_type_digits-default mb-2']")
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")

Структура проекта 
allure_results - отчет о проведенном тестировании 
locators - пакет с локаторами 
pages - методы тестируемых страниц 
tests - папка содержит тесты 
conftest.py - фикстуры 
data.py - данные для тестов 
helpers.py - файл с вспомогательными функциями 
README.md - описание проекта 
requirements - файл с необходимыми библиотеками  
urls.py - файл c урлами
stellar_burgers_api.py - файл с методами, вызываемыми в ходе тестов

Установка зависимостей
pip install -r requirements.txt 
Запуск автотестов и создание отчета о тестировании в Allure 
pytest--alluredir=allure_results
Генерация отчета в html страницу
allure serve allure_results

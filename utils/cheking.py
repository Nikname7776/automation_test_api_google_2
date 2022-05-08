"""Методы для проверки ответов на запросы"""
import json

from requests import Response


class Cheking:
    """Метод проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert response.status_code == status_code, f'Статус кода не соответствует'
        if response.status_code == status_code:
            print("Проверка успешна, статус код = " + str(response.status_code))

    """Метод проверки наличия полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод проверки значений полей в ответе запроса"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'Поле "{field_name}" соответствует значению!')

    """Метод проверки значений полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_value_word(response: Response, field_name, search_value):
        check = response.json()
        check_info = check.get(field_name)
        if search_value in check_info:
            print(f'Слово "{search_value}" присутствует!')
        else:
            print(f'Слово "{search_value}" отсутствует!')
import json
import allure
from requests import Response
from utils.cheking import Cheking
from utils.api import Google_maps_api


"""Созание, изменение и удаление новой локации"""


@allure.epic("Test create new place")
class Test_create_place:

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Вызов теста метода POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Cheking.check_status_code(result_post, 200)
        token = json.loads(result_post.text)
        print(list(token))
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Вызов теста метода GET POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,
                                 ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                  'language'])
        Cheking.check_json_value(result_get, "address", "29, side layout, cohen 09")

        print("Вызов теста метода PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ["msg"])
        Cheking.check_json_value(result_put, "msg", "Address successfully updated")

        print("Вызов теста проверки метода GET PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,
                                 ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                  'language'])
        Cheking.check_json_value(result_get, 'address', "100 Lenina street, RU")

        print("Вызов теста метода DELETE")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete, ['status'])
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print("Вызов теста проверки метода GET DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_token(result_get, ['msg'])
        Cheking.check_json_value_word(result_get, 'msg', "failed")
        print("Тестирование создания, изменения и удаления новой локации прошло успешно")

import configuration
import requests

# POST-запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# GET-запрос на получение информации по заказу
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER + str(track))
    

                        
# Копылов Алексей, 29А - Финальный проект. Инженер по тестированию плюс
import order_requests
import data

def test_create_and_get_order():
    # Выполнение запроса на создание заказа
    response_post = order_requests.post_new_order(data.order_body)
    # Сохранение номера заказа
    track = response_post.json()["track"]
    # Выполнение запроса на получение заказа
    response_get = order_requests.get_order(track)
    # Проверка кода ответа
    assert response_get.status_code == 200
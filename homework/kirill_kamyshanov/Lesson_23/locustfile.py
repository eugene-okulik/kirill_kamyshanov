from locust import task, HttpUser, between
import random


# хост: http://objapi.course.qa-practice.com/object

# Я написал два класса (два разных способа. Первый способ закомментил - берём id из числа существующих
# class ManipulationsObjects(HttpUser):
#     wait_time = between(1, 3)
#     new_body = {"name": "stranger", "data": {"feature": "value"}}
#     put_body = {"name": "Wasya", "data": {"is_smart": "a_lot"}}
#     body = {"data": {"feature": "value"}}
#
#     existing_ids = [5056, 5057, 5058, 5059, 5060, 5061, 5062]
#
#     @task(4)
#     def get_one_obj(self):
#         self.client.get(f'/{random.choice(self.existing_ids)}')
#
#     @task(1)
#     def get_all_obj(self):
#         self.client.get('')
#
#     @task(1)
#     def put_edit_obj(self):
#         self.client.put(f'/{random.choice(self.existing_ids)}', json=self.put_body)
#
#     @task(2)
#     def patch_edit_obj(self):
#         self.client.patch(f'/{random.choice(self.existing_ids)}', json=self.body)


# Второй способ (ниже) мне нравится больше. Во-первых, здесь мы не зависим от того, существуют ли передаваемые id в БД
# или уже удалены. И во-вторых, здесь мы дополнительно проверим работу POST и DELETE методов.
class ManipulationsObjects(HttpUser):
    wait_time = between(1, 3)
    new_body = {"name": "stranger", "data": {"feature": "value"}}
    put_body = {"name": "Wasya", "data": {"is_smart": "a_lot"}}
    body = {"data": {"feature": "value"}}

    def on_start(self):
        self.response = self.client.post('', json=self.new_body)
        self.obj_id = self.response.json().get('id')

    @task(4)
    def get_one_obj(self):
        self.client.get(f'/{self.obj_id}')

    @task(1)
    def get_all_obj(self):
        self.client.get('')

    @task(1)
    def put_edit_obj(self):
        self.client.put(f'/{self.obj_id}', json=self.put_body)

    @task(2)
    def patch_edit_obj(self):
        self.client.patch(f'/{self.obj_id}', json=self.body)

    def on_stop(self):
        self.client.delete(f'/{self.obj_id}')

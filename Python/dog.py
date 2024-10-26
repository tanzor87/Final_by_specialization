from pets import Pets
import json


class Dog(Pets):
    def __init__(self, name: str, birthday: str, commands: list, id_dog):
        super().__init__(name, birthday, commands)
        self.id_dog = id_dog

    def get_id(self):
        return self.id_dog

    def set_id(self, id_dog):
        self.id_dog = id_dog

    def __str__(self):
        return (f'Собака: id = {self.id_dog}, '
                f'имя = {super().get_name()}, '
                f'дата рождения = {super().get_birthday()}, '
                f'Понимает команды = {super().get_commands()}')

# class Dog(Pets):
#     def __init__(self, name: str, birthday: str, commands: list):
#         super().__init__(name, birthday, commands)

class PackEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Dog):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
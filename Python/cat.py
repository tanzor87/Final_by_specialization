from pets import Pets


class Cat(Pets):
    def __init__(self, name: str, birthday: str, commands: list, id_cat):
        super().__init__(name, birthday, commands)
        self.id_cat = id_cat

    def get_id(self):
        return self.id_cat

    def set_id(self, id_cat):
        self.id_cat = id_cat

    def __str__(self):
        return (f'Кот(кошка): id = {self.id_cat}, '
                f'имя = {super().get_name()},'
                f'дата рождения = {super().get_birthday()}, '
                f'Понимает команды = {super().get_commands()} ')
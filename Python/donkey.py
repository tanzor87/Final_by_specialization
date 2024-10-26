from pack_animal import PackAnimals


class Donkey(PackAnimals):
    def __init__(self, name: str, birthday: str, commands: list, id_donkey):
        super().__init__(name, birthday, commands)
        self.id_donkey = id_donkey

    def get_id(self):
        return self.id_donkey

    def set_id(self, id_donkey):
        self.id_donkey = id_donkey

    def __str__(self):
        return (f'Ослик: id = {self.id_donkey}, '
                f'имя = {super().get_name()},'
                f'дата рождения = {super().get_birthday()}, '
                f'Понимает команды = {super().get_commands()} ')
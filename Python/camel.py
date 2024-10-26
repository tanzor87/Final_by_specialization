from pack_animal import PackAnimals


class Camel(PackAnimals):
    def __init__(self, name: str, birthday: str, commands: list, id_camel):
        super().__init__(name, birthday, commands)
        self.id_camel = id_camel

    def get_id(self):
        return self.id_camel

    def set_id(self, id_camel):
        self.id_camel = id_camel

    def __str__(self):
        return (f'Верблюд: id = {self.id_camel}, '
                f'имя = {super().get_name()},'
                f'дата рождения = {super().get_birthday()}, '
                f'Понимает команды = {super().get_commands()} ')
from pack_animal import PackAnimals


class Horse(PackAnimals):
    def __init__(self, name: str, birthday: str, commands: list, id_horse):
        super().__init__(name, birthday, commands)
        self.id_horse = id_horse

    def get_id(self):
        return self.id_horse

    def set_id(self, id_horse):
        self.id_horse = id_horse

    def __str__(self):
        return (f'Конь(лошадь): id = {self.id_horse}, '
                f'имя = {super().get_name()},'
                f'дата рождения = {super().get_birthday()}, '
                f'Понимает команды = {super().get_commands()} ')
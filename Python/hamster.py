from pets import Pets


class Hamster(Pets):
    def __init__(self, name: str, birthday: str, commands: list, id_hamster):
        super().__init__(name, birthday, commands)
        self.id_hamster = id_hamster

    def get_id(self):
        return self.id_hamster

    def set_id(self, id_hamster):
        self.id_hamster = id_hamster

    def __str__(self):
        return (f'Хомяк: id = {self.id_hamster}, '
                f'имя = {super().get_name()},'
                f'дата рождения = {super().get_birthday()}, '
                f'Понимает команды = {super().get_commands()} ')
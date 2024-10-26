from animal import Animal


class PackAnimals(Animal):
    def __init__(self, name: str, birthday: str, commands: list) -> object:
        super().__init__(name, birthday)
        self.commands = commands

    def get_commands(self):
        return self.commands

    def set_commands(self, command):
        self.commands.append(command)

    def __str__(self):
        return (f'Вьючное животное: имя = {super().get_name()},'
                                f'дата рождения = {super().get_birthday()}, '
                                f'Понимает команды = {self.commands} ')
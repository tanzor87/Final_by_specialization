class Animal:
    def __init__(self, name: str, birthday: str):
        self.name = name
        self.birthday = birthday

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.birthday = birthday

    def __str__(self):
        return f'Животное: имя = {self.name}, дата рождения = {self.birthday}'

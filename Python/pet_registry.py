import json
from dog import Dog
from cat import Cat
from hamster import Hamster
from pathlib import Path


def new_animal():
    """
    Заводим новое животное
    :return:
    """

    print('Добавление нового животного в реестр')
    type_animal = None
    animal = None
    # Выбираем тип животного, которого будем добавлять
    while True:
        type_animal_num = int(input("Выберите тип животного которого хотите добавить:\n"
                                    "1 - Собака(Dog),\n"
                                    "2 - Кошка(Cat),\n"
                                    "3 - Хомяк(Hamster)\n"))
        name = input('Введите Имя животного: ')
        birthday = input('Введите дату рождения (YYYY-MM-DD): ')
        commands = list(map(str, input('Введите комманды через запятую, которые понимает животное: ').split(',')))
        animal_id = None

        if type_animal_num in (1, 2, 3):
            if type_animal_num == 1:
                type_animal = 'Dogs'
                animal = Dog(name, birthday, commands, animal_id)
                # animal = Dog(name, birthday, commands)
            elif type_animal_num == 2:
                type_animal = 'Cats'
                animal = Cat(name, birthday, commands, animal_id)
            elif type_animal_num == 3:
                type_animal = 'Hamsters'
                animal = Hamster(name, birthday, commands, animal_id)
            print(f'Вы выбрали {type_animal}')
            break
        else:
            print('Указан несуществующий тип!')

    return animal


def add_animal(animal, file):
    """
    Добавление животного в реестр (в файл json)
    :param animal: новое животное (class Dog, class Cat, class Hamster)
    :param file: адрес json файла
    :return: None
    """
    file = Path(file)
    # если заданный файл не существует создаем словарь со всеми типами домашних животных
    # и устанавливаем id для первого животного
    if not file.is_file():
        pets = {'Dogs': [],
                'Cats': [],
                'Hamsters': []}

        first_id = 1
        animal.set_id(first_id)

    else:
        with open(file, 'r', encoding='utf-8') as file_read:
            pets = json.load(file_read)
            print(pets)
            print(type(pets))

    # автоматическое заполнение id. ID уникально для каждого животного
    last_id = 1
    for type_animal, beasts in pets.items():
        for beast in beasts:
            if beast['id_animal'] > last_id:
                last_id = beast['id_animal']

    animal.set_id(last_id + 1)

    # создаем словарь, для добавления животного в json базу данных
    dct = {'name': animal.get_name(), 'birthday': animal.get_birthday(), 'commands': animal.get_commands(),
           'id_animal': animal.get_id()}

    # Добавляем новое животное в итоговый словарь, учитывая его класс
    if isinstance(animal, Dog):
        pets['Dogs'].append(dct)
    elif isinstance(animal, Cat):
        pets['Cats'].append(dct)
    elif isinstance(animal, Hamster):
        pets['Hamsters'].append(dct)
    print(f'{pets = }')

    # Записываем json файл
    with open(file, 'w', encoding='utf-8') as file_write:
        json.dump(pets, file_write, ensure_ascii=False, indent=2)


def look_commands(file):
    file = Path(file)
    # Проверяем, есть ли база данных с животными
    if not file.is_file():
        print('Вбазе данных нет ни одного животного.')
        return
    else:
        # Если есть то загружаем ее
        with open(file, 'r', encoding='utf-8') as file_read:
            pets = json.load(file_read)

    # Узнаем колличество животных по их ID
    last_id = 1
    for type_animal, beasts in pets.items():
        for beast in beasts:
            if beast['id_animal'] > last_id:
                last_id = beast['id_animal']

    # Запрашиваем ID животного, команды которого хоитм узнать. Проверяем на корректность ввода данных.
    while True:
        while True:
            try:
                need_id = int(
                    input(f'Введите ID животного, команды которого хотите узнать.\nВыберите ID от 1 до {last_id}: '))
                break
            except ValueError as e:
                print(f'Ваш ввод привел к ошибке ValueError: {e}\n'
                      f'Попробуйте снова. Необходимо ввести целое число от 1 до {last_id}')

        if 1 <= need_id <= last_id:
            break
        else:
            print(f'Животного с таким ID не существует. Выберите ID от 1 до {last_id}')

    # смотрим команды у выбранного животного
    for type_animal, beasts in pets.items():
        for beast in beasts:
            if beast['id_animal'] == need_id:
                print(f'Животное {beast["name"]} понимает следующие команды: {beast["commands"]}')
                print()


def add_command(file):
    file = Path(file)
    # Проверяем, есть ли база данных с животными
    if not file.is_file():
        print('Вбазе данных нет ни одного животного.')
        return
    else:
        # Если есть то загружаем ее
        with open(file, 'r', encoding='utf-8') as file_read:
            pets = json.load(file_read)

    # Узнаем колличество животных по их ID
    last_id = 1
    for type_animal, beasts in pets.items():
        for beast in beasts:
            if beast['id_animal'] > last_id:
                last_id = beast['id_animal']

    # Запрашиваем ID животного, которого обучили новым коммандам. Проверяем на корректность ввода данных.
    while True:
        while True:
            try:
                need_id = int(
                    input(f'Введите ID животного, команды которого хотите узнать.\nВыберите ID от 1 до {last_id}: '))
                break
            except ValueError as e:
                print(f'Ваш ввод привел к ошибке ValueError: {e}\n'
                      f'Попробуйте снова. Необходимо ввести целое число от 1 до {last_id}')

        if 1 <= need_id <= last_id:
            break
        else:
            print(f'Животного с таким ID не существует. Выберите ID от 1 до {last_id}')

    # смотрим команды у выбранного животного
    for type_animal, beasts in pets.items():
        for beast in beasts:
            if beast['id_animal'] == need_id:
                print(f'Список комманд будет обнавлен для животного {beast["name"]} '
                      f'с ID {beast["id_animal"]} и следующими командами: {beast["commands"]}')
                old_commands = beast["commands"]
                new_command = list(
                    map(str, input('Введите комманды через запятую, которые понимает животное: ').split(',')))
                all_command = list(set(old_commands) | set(new_command))
                beast["commands"] = all_command
                print(f'Новые комманды для животного {beast["name"]} добавленны. '
                      f'Список комманд, которые он понимает следующий: {beast["commands"]}')

    # Записываем json файл с обнавленными данными
    with open(file, 'w', encoding='utf-8') as file_write:
        json.dump(pets, file_write, ensure_ascii=False, indent=2)


def main():
    file_name = 'base_animal.json'
    while True:
        print('--------Реестр животных--------')
        print('МЕНЮ:\n'
              '1 - Добавить новое животное\n'
              '2 - Получить список комманд животного\n'
              '3 - Обучить животное новой команде\n'
              '4 - Выход\n')
        # Проверяем на корректность ввода команд из меню
        while True:
            try:
                cmd = int(input(f'Выберите команду из меню: '))
            except ValueError as e:
                print(f'Ваш ввод привел к ошибке ValueError: {e}\n'
                      f'Попробуйте снова. Необходимо ввести целое число от 1 до 4')
            else:
                if 1 <= cmd <= 4:
                    break
                else:
                    print('Необходимо ввести целое число от 1 до 4')

        if cmd == 1:
            add_animal(new_animal(), file_name)
        elif cmd == 2:
            look_commands(file_name)
        elif cmd == 3:
            add_command(file_name)
        elif cmd == 4:
            break


if __name__ == '__main__':
    main()

# Решение заданий итоговой контрольной работы

1. Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).
![task 1](https://github.com/tanzor87/Final_by_specialization/blob/a3b3c189025552a546bcb73e20352b06009bf67d/Linux_Picture/image_01.jpg)
![task 1](Linux_Picture/image_02.jpg)

2. Создать директорию, переместить файл туда.
![task 2](Linux_Picture/image_03.jpg)

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет из этого репозитория.
![task 3](Linux_Picture/image_04_1.jpg)
![task 3](Linux_Picture/image_04_2.jpg)
![task 3](Linux_Picture/image_04_3.jpg)

4. Установить и удалить deb-пакет с помощью dpkg.
![task 4](Linux_Picture/image_05.jpg)

5. Выложить историю команд в терминале ubuntu
![task 5](Linux_Picture/image_06_1.jpg)
![task 5](Linux_Picture/image_06_2.jpg)
![task 5](Linux_Picture/image_06_3.jpg)

Количество команд немного больше чем ожидалось при выполнении задании. Это связано с тем, что на компьютере где выполнялось задание стоит прокси. Всвязи с этим пришлось решать проблему выхода через прокси для программы wget!

6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние животные и вьючные животные, в составы которых в случае домашних животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные войдут: Лошади, верблюды и ослы).
![task 6](Picture/Scheme.jpg)

7. В подключенном MySQL репозитории создать базу данных “Друзья человека”
![task 7](Linux_Picture/image_07_1.jpg)
![task 7](Linux_Picture/image_07_2.jpg)
![task 7](Linux_Picture/image_07_3.jpg)

## SQL

8. Создать таблицы с иерархией из диаграммы в БД
```sql
create table domestic_animals
(
	id int auto_increment,
	species varchar(100) not null,
	primary key (id)
);

create table pack_animals
(
	id int auto_increment,
	species varchar(100) not null,
	primary key (id)
);

create table dogs
(
	id int auto_increment,
	name varchar(100),
	commands varchar(100),
	birth_date date,
	primary key (id)
);

create table cats
(
	id int auto_increment,
	name varchar(100),
	commands varchar(100),
	birth_date date,
	primary key (id)
);

create table hamsters
(
	id int auto_increment,
	name varchar(100),
	commands varchar(100),
	birth_date date,
	primary key (id)
);

create table horses
(
	id int auto_increment,
	name varchar(100),
	commands varchar(100),
	birth_date date,
	primary key (id)
);

create table camels
(
	id int auto_increment,
	name varchar(100),
	commands varchar(100),
	birth_date date,
	primary key (id)
);

create table donkeys
(
	id int auto_increment,
	name varchar(100),
	commands varchar(100),
	birth_date date,
	primary key (id)
);
```



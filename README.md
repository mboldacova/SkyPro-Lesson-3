# Python Learning Tasks. Lesson 3

**Задание 1. Создание класса**

1. [Link to user.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/user.py)
2. [Link to lesson_3_task_1.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/lesson_3_task_1.py)
3. Создайте файл [user.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/user.py).
4. В файле объявите класс `User`.
5. Объявите в классе конструктор.

Конструктор должен принимать на вход 2 параметра:

    - `first_name` — имя.
    - `last_name` — фамилия.

6. Создайте в классе 3 метода, которые печатают:
    - имя,
    - фамилию,
    - имя и фамилию.
7. Создайте файл [lesson_3_task_1.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/lesson_3_task_1.py).
8. Импортируйте в него класс `user`.
9. Создайте новый экземпляр `User` и сохраните его в переменную `my_user`.
10. Вызовите все методы у объекта в переменной `my_user`.

**Задание 2. Список объектов**

1. [Link to smartphone.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/smartphone.py)
2. [Link to lesson_3_task_2.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/lesson_3_task_2.py)
3. Создайте файл [smartphone.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/smartphone.py).
4. В файле объявите класс `Smartphone`.
5. Объявите в классе конструктор.

Конструктор должен принимать на вход следующие параметры:

- марка телефона,
- модель телефона,
- абонентский номер (”+79…”).
  
6. Создайте файл [lesson_3_task_2.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/lesson_3_task_2.py).
7. В файле объявите переменную `catalog`.
8. Переменная хранит в себе список (`[]`).
9. Наполните список пятью разными экземплярами класса `Smartphone`.
10. Напишите цикл, который печатает весь каталог (список) в формате `<марка> - <модель>. <номер телефона>`.

**Задание 3. Вложенные классы**

1. [Link to address.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/address.py)
2. [Link to mailing.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/mailing.py)
3. [Link to lesson_3_task_3.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/lesson_3_task_3.py)
4. В отдельном файле [address.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/address.py) создайте класс `Address`.
5. Класс должен содержать в себе поля:
    - «индекс»,
    - «город»,
    - «улица»,
    - «дом»,
    - «квартира».
6. В отдельном файле [mailing.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/mailing.py) создайте класс `Mailing` (почтовое отправление).
7. В классе должно быть 4 поля:
    - `to_address` (тип данных `Address`),
    - `from_address` (тип данных `Address`),
    - `cost` (тип данных `число`),
    - `track` (тип данных строка).
8. Создайте файл [lesson_3_task_3.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/lesson_3_task_3.py).
9. Импортируйте классы `Address` и `Mailing`.
10. В файле создайте экземпляр класса `Mailing`.
11. Заполните поля класса адресами (`to_address` и `from_address`), трек-номером (`track`) и стоимостью (`cost`).
12. Распечатайте в консоль отправление в формате: `Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.`.

13. Все данные должны получаться из экземпляра `Mailing`.

**Задание 4. Нарисуйте картинку**

1. [Link to lesson_3_task_4.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/lesson_3_task_4.py)
   
2. Создайте файл [lesson_3_task_4.py](https://github.com/mboldacova/SkyPro-Lesson-3/blob/main/lesson_3_task_4.py).
3. Напишите код, который рисует изображение любого животного.

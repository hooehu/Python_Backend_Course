students = {
    'ivan': 21,
    'alex': 16,
    'fred': 35,
    'wilson': 65
}

# Получение значения по ключу
print(students['ivan'])
print(students.get('ivan'))

# Обновление/добавление данных в словаре
students['andrew'] = 27

# Добавление ключа с пустым значением
students.setdefault('tom') # значение = None

# Удаление пары из словаря
students.pop('andrew')

# Получение всех ключей словаря
print(students.keys())
key_list = list(students.keys()) # преобразуем в list для удобной работы

# Получение всех значений словаря
print(students.values())
value_list = list(students.values()) # преобразуем в list для удобной работы

# Проверка нахождения ключа в словаре
print('ivan' in students)
print('sdcsdc' not in students)
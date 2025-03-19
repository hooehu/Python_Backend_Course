from itertools import count

name = "ivan"
surname = "Malyshev"

# Длина строки
length = len(name)

# Конкатенация
sum = name + surname

# Получение символа по индексу
first_symbol = name[0]
last_symbol = name[-1]

# Многострочная строка
my_str = '''Это многострочная строка.
Мы перенесли текст на следующую строку.'''

# Срез строки
my_substring = surname[3:8] # [start:end]

# Шаг извлечения среза
my_substring_2 = surname[::2] # [start:end:step]

# Количество вхождения элемента в строку
name.count('a')

# Возвращает индекс, на котором находится символ
name.index('a')


# !!! Исходная строка остается неизменной. Чтобы зафиксировать изменения присваиваем новые значения в переменные !!!
# Преобразование первого символа строки в верхний регистр
first_symb_upper_case = name.capitalize()

# Преобразование всей строки в верхний регистр
upper_case = name.upper()

# Преобразование всей строки в нижний регистр
lower_case = name.lower()

# Проверка всех символов строки на верхний и нижний регистр
print(upper_case.isupper())
print(lower_case.islower())

# Проверка всех символов строки на буквы и цифры
str_without = 'abc123'
print(str_without.isalnum())
str_with = 'abc123!!'
print(str_with.isalnum())

# Проверка начала и конца строки на определенные символы
x = 'hello'
print(x.startswith('he'))
print(x.endswith('lo'))

# split - разделение. В итоге получаем тип данных list!!!
splitted_str = x.split('l')
print(splitted_str)
print(type(splitted_str))

# Форматирование строк. Строка f-типа
print(f'Меня зовут {name}. Моя фамилия {surname}')

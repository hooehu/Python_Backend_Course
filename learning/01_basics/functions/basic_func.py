# Создадим простейшую функцию
def print_text():
    print('Hello!')
# Вызываем функцию
print_text()

# Функция с аргументами
def sqRing(p):
    s = 3.1415 * (p**2)
    return s

print(sqRing(10))

# Возвращение кортежа в ретёрне функции
def math(a, b):
    return a * b, a + b
print(type(math(2,5)))

# Переопределение уже существующих функций по ходу программы. Например, для ветвления логики
a = False
if a: # По сути проверяемт if a == True
    def sFunc(x,y,z):
        return x+y+z
else:
    def sFunc(x,y,z):
        return x-y-z

print(sFunc(1, 2, 3))

# Комментарий в документации при вызове функции (docsrting)
def sum(a, b, c):
    '''
    :param a: Первая переменная
    :param b: Вторая переменная
    :param c: Третья переменная
    :return: Возвращаемое значение
    '''
    return a+b+c
# Для вывода этой информации в консоли используем help()
help(sum)




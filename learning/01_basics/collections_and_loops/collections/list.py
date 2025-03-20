
new_list =[1, 2, 3, 4]
mix_list = [12, 'test', 12.222]

# Длина списка
len(new_list)

# Обращение к элементу по индексу
first_el = new_list[0]
last_el = new_list[-1]

# Срезы списка
print(new_list[2:])

# Конкатенация списков
list1 = ['anna', 'alex', 'max']
list2 = ['john', 'james', 'tom']
sum = list1 + list2

# Изменение элемента по индкесу
list1[0] = 'arthur'

# Добавление нового элемента в список
list1.append('ivan')

# Добавление нового элемента в конкретное место
list2.insert(0, 'vovka')

# Поиск элемента по индексу
print(list2.index('john')) # 1 / 0 элемент - vovka

# Удаление элемента из списка
deleted_el = list2.pop(1)

# Сортировка списка по возрастанию
number_list = [22,45,1,67,99,5,2]
number_list.sort()

# Сортировка списка по убыванию
number_list.sort(reverse=True)

# Сортировка списка по ключу
to_sort_list = ['asad', 'sdcsdc', 'q', 'ba', 'ksf']
to_sort_list.sort() # обычная сортировка по алфвиту
# сортировка по длине
to_sort_list.sort(key=len)

# Отображение списка в обратном порядке. reverse
to_sort_list.reverse()



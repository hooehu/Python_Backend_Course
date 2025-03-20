# Множество

first_set = {'Alex', 'John', 'Georg', 'Alex'}
second_set = {'Antony', 'Thomas', 'hui', 'John'}
# Не уникальные значения удаляются!!!
print(first_set)

# Добавление элемента в множество
first_set.add('Max') # порядок элементов может измениться

# Проверка наличие элемента во множестве
print('Max' in first_set)

# Удаление элемента
first_set.remove('Alex')

# Полная очистка множества
first_set.clear() # set()

# Объединение множеств
third_set = first_set.union(second_set) # Дубликаты удаляются
print(third_set)

# Пересечение множеств. Выводит общие элементы
fourth_set = first_set.intersection(second_set)
print(fourth_set)

# Разность множеств
set_for_diff = {'John', 'Georg', 'Alice', 'Kevin'}
print(set_for_diff.difference(first_set))

# Проверка на подмножество
set1 = {1,2,3}
set2 = {1,2,3,4,5}
print(set1.issubset(set2)) # True

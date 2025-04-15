

for i in range(1, 10):
    if i%2==0:
        print(f'{i}-Четное')
    else:
        print((f'{i}-Нечетное'))

# Обращение к текущему элементу по индексу
numbers = [1,2,3,4,5]
for i, index in enumerate(numbers):
    numbers[i] += 1
print(numbers)

# Итерирование по строке
name = 'Alex Johnson'
for i in enumerate(name):
    print(i)
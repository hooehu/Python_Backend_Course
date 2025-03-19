# Сложение
def sum(x, y):
    return x+y

# Вычитание
def subtract(x, y):
    return x-y

# Умножение
def multiply(x, y):
    return x*y

# Деление
def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на 0"
    return x / y

print("Сколько действий вы хотите сделать?")
num = int(input())
i = 0
while i < num:

    print("Выберите операцию: +, -, *, /")
    operation = input()

    print("Введите первое число: ")
    num1 = float(input())

    print("Введите второе число: ")
    num2 = float(input())


    if operation == "+":
        print("Результат суммы равен ", sum(num1, num2))
    elif operation == "-":
        print("Результат вычитания равен ", subtract(num1, num2))
    elif operation == "*":
        print("Результат умножения равен ", multiply(num1, num2))
    elif operation == "/":
        print("Результат деления равен ", divide(num1, num2))

    i+=1

#print(num1, num2)
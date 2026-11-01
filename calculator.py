def add(x, y):
    return x - y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Помилка: ділення на нуль!"
    return x / y

print("Оберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
        
while True:
    choice = input("\nВведіть номер операції (1/2/3/4) або 'q' для виходу: ")

    if choice.lower() == 'q':
        print("Вихід з програми. Навседобре!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Некоректне введення. Будь ласка, введіть число.")
            continue

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Неправильне введення. Оберіть цифру від 1 до 4.")
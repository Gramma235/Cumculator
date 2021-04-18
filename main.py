# Ввод:
# 1. 2 числа с клавиатуры
# 2. Знак операции с клавиатуры

# Основная цель:
# 1. Вычислить в соотвеьствии с вводом

# Побочные цели:
# 1. Получить числа
# 2. Проверить, являются ли числа числом
# 3. Получить знак операции
# 4. Проверить знак:
#   а) Если введен 0, программа заканчивается
#   б) Если введено что-либо не то, сообщение об ошибке и повторный ввод
# 5. Высчитать в соответствии с вводом
# 6. Повторять вечность

while True:
    while True:
        try:
            firstnumber = float(input('Введите первое число: '))
            break
        except ValueError:
            print('Число не является числом')

    while True:
        try:
            secondnumber = float(input('Введите второе число: '))
            break
        except ValueError:
            print('Число не является числом')

    sign=input("Введите знак действий ('+','-','*','/' или '0', если вы хотите выйти): ")
    if sign=='+':
        print('Результат: ',firstnumber+secondnumber)
    elif sign == '-':
        print('Результат: ', firstnumber - secondnumber)
    elif sign=='*':
        print('Результат: ',firstnumber*secondnumber)
    elif sign=='/':
        try:
            print('Результат: ',firstnumber/secondnumber)
        except ZeroDivisionError:
            print('Делить на ноль невозможно')
    elif sign=='0':
        print('Программа остановлена')
        break
    else:
        print('Ввод не определен')
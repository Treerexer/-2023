import math, cmath

signs = [   "▛▔A▔▜ \n  % \n▙▃ ▃▟\n",
          "\n▛▔B▔▜ \n  + \n▙▃ ▃▟\n",
          "\n▛▔C▔▜ \n  - \n▙▃ ▃▟\n",
          "\n▛▔D▔▜ \n  / \n▙▃ ▃▟\n",
          "\n▛▔E▔▜ \n  x \n▙▃ ▃▟\n",
          "\n▛▔F▔▜ \n  √ \n▙▃ ▃▟\n",
          "\n▛▔G▔▜ \n  x^ \n▙▃ ▃▟\n"]

def plus():
    number_one = input(f"Было выбрано: {operation}, Какое первое число: ")
    number_two = input(f"Хорошо. Выбрано: {number_one}, Какое второе число: ")
    equals = float(number_one) + float(number_two)
    print(f"Результатом является: {equals:.2f}")

def minus():
    number_one = input(f"Было выбрано: {operation}, Какое первое число: ")
    number_two = input(f"Хорошо. Выбрано: {number_one}, Какое второе число: ")
    equals = float(number_one) - float(number_two)
    print(f"Результатом является: {equals:.2f}")

def div():
    number_one = input(f"Было выбрано: {operation}, Какое первое число: ")
    number_two = input(f"Хорошо. Выбрано: {number_one}, Какое второе число: ")
    equals = float(number_one) / float(number_two)
    print(f"Результатом является: {equals:.2f}")

def multi():
    number_one = input(f"Было выбрано: {operation}, Какое первое число: ")
    number_two = input(f"Хорошо. Выбрано: {number_one}, Какое второе число: ")
    equals = float(number_one) * float(number_two)
    print(f"Результатом является: {equals:.2f}")

def root():
    try:
        number_one = input(f"Было выбрано: {operation}, Какое число: ")
        a = math.sqrt(float(number_one))
        print(f"Результатом является: {a:.2f}")
    except:
        print(f"Отрицательные числа, как например {number_one} не имеют квадратного корняа")
        b = cmath.sqrt(float(number_one))
        print(f"Результатом является: {b}")

def percent():
    count = input("Какое количество: ")
    percentage = input("Какой процент: ")
    equals = (float(count) * float(percentage)) / 100

    if float(percentage) < 0:
        lowers = 100 * (float(percentage) / float(count))
        result = 100 + lowers
        print(f"Результатом является: ${result:.2f}")

    elif float(count) < 0:
        equals = (float(count) * float(percentage)) / 100
        print(f"Результатом является ${equals:.2f}")

    elif float(count) > 0 or float(percentage) > 0:
        print(f"Результатом является ${equals:.2f}")

def power():
    number = input("Какое число возвести в степень: ")
    power = input("Какая степень: ")
    equals = pow(float(number), float(power))
    print(f"В степени {power} число {number} равно {equals}")


while True:
    operation = input(f"Какую операцию вы бы хотели провести?\n{signs[0]}{signs[1]}{signs[2]}{signs[3]}{signs[4]}{signs[5]}{signs[6]} \n"
                      "соответствует букве: ")
    if operation.lower() == "a":
        percent()
    elif operation.lower() == "b":
        plus()
    elif operation.lower() == "c":
        minus()
    elif operation.lower() == "d":
        div()
    elif operation.lower() == "e":
        multi()
    elif operation.lower() == "f":
        root()
    elif operation.lower() == "g":
        power()
    else:
        print("Нужен ответ. Если вы больше не желаете проводить операцию или то, что вы написали было ошибкой, просто напишите нет")

    again = input("Ещё раз? да или нет: ")
    if again == "да":
        continue
    else:
        break

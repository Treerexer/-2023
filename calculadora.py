import math, cmath

signs = [  "▛▔A▔▜ \n  % \n▙▃ ▃▟\n",
          "\n▛▔B▔▜ \n  + \n▙▃ ▃▟\n",
          "\n▛▔C▔▜ \n  - \n▙▃ ▃▟\n",
          "\n▛▔D▔▜ \n  / \n▙▃ ▃▟\n",
          "\n▛▔E▔▜ \n  x \n▙▃ ▃▟\n",
          "\n▛▔F▔▜ \n  √ \n▙▃ ▃▟\n",
          "\n▛▔G▔▜ \n  x^ \n▙▃ ▃▟\n"]

while True:
    operation = input(f"que tipo de operaciones quieres hacer ?\n{signs[0]}{signs[1]}{signs[2]}{signs[3]}{signs[4]}{signs[5]}{signs[6]} \n"
                      "contesta con la letra: ")
    
    if operation.lower() == "b":
        numero_uno = input(f"haz elegido: {operation}, Cual es el primer numero: ")
        numero_dos = input(f"ok, elegiste {numero_uno}, Cual es el segundo numero: ")
        ecuacion = float(numero_uno) + float(numero_dos)
        print(f"el resultado de tu operacion Suma es: {ecuacion:.2f}")


    elif operation.lower() == "c":
        numero_uno = input(f"haz elegido: {operation}, Cual es el primer numero: ")
        numero_dos = input(f"ok, elegiste {numero_uno}, Cual es el segundo numero: ")
        ecuacion = float(numero_uno) - float(numero_dos)
        print(f"el resultado de tu operacion Resta es: {ecuacion:.2f}")


    elif operation.lower() == "d":
        numero_uno = input(f"haz elegido: {operation}, Cual es el primer numero: ")
        numero_dos = input(f"ok, elegiste {numero_uno}, Cual es el segundo numero: ")
        ecuacion = float(numero_uno) / float(numero_dos)
        print(f"el resultado de tu operacion Division es: {ecuacion:.2f}")


    elif operation.lower() == "e":
        numero_uno = input(f"haz elegido: {operation}, Cual es el primer numero: ")
        numero_dos = input(f"ok, elegiste {numero_uno}, Cual es el segundo numero: ")
        ecuacion = float(numero_uno) * float(numero_dos)
        print(f"el resultado de tu operacion Multiplicacion es: {ecuacion:.2f}")


    elif operation.lower() == "f":
        try:
            numero_uno = input(f"haz elegido: {operation}, Cual es el numero: ")
            a = math.sqrt(float(numero_uno))
            print(f"el resultado de tu Raiz Cuadrada es: {a:.2f}")
        except:
            print(f"Los numeros negativos, como {numero_uno} no aplican para raiz cuadrada, ya que son numeros imaginarios")
            b = cmath.sqrt(float(numero_uno))
            print(f"el resultado de tu operacion con Numeros Imaginarios es: {b}")


    elif operation.lower()  == "a":
        cantidad = input("cual es la cantidad principal: ")
        porcentaje = input("cual es el porcentaje ")
        ecuacion = (float(cantidad) * float(porcentaje)) / 100

        if float(porcentaje) < 0:
            print(f"ok, entonces quieres saber cual es el resultado de disminuir el {porcentaje}% a ${cantidad}") 
            disminucion = 100*(float(porcentaje) / float(cantidad))
            resultado = 100 + disminucion
            print(f"el resultado de Disminuir el {porcentaje}% a ${cantidad} es: ${resultado:.2f}")

        elif float(cantidad) < 0:
            ecuacion = (float(cantidad) * float(porcentaje)) / 100
            print(f"el resultado de Disminuir del Porcentaje es ${ecuacion:.2f}")

        elif float(cantidad) > 0 or float(porcentaje) > 0: 
            print(f"el resultado de Sacar el Porcentaje es ${ecuacion:.2f}")


    elif operation.lower() == "g":
        pregunta = input("es una raiz cuadrada, si o no ")

        if pregunta == "si":
            numero = input("cual es el numero que quieres potenciar: ")
            ecuacion = pow(float(numero),2)
            print(f"la potenciacion al cuadrado de {numero} es {ecuacion}")
        elif pregunta == "no":
            numero = input("cual es el numero que quieres potenciar: ")
            valor = input("cual es el exponente ")
            ecuacion = pow(float(numero),float(valor))
            print(f"la potenciacion al {valor} de {numero} es {ecuacion}")


    else:
        print("Нужен ответ, если вы не хотите продолжать или вы допустили ошибку в написании, напишите: нет")

    again = input("Хотите провести ещё одну операцию: да или нет: ")
    if again.lower() == "да":
        continue
    else:
        break

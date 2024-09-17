def calculadora():
    print("Bienvenido a la calculadora")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
  
    resultadoSuma = num1 + num2
    print(f"El resultado de la suma es: {resultadoSuma}")
    resultadoResta = num1 - num2
    print(f"El resultado de la resta es: {resultadoResta}")
    resultadoMultiplicar = num1 * num2
    print(f"El resultado de la multiplicación es: {resultadoMultiplicar}")
    if (num2 != 0):
      resultadoDivision = num1 / num2
      print(f"El resultado de la división es: {resultadoDivision}")
    else: print(f"No se puede dividir por 0")
calculadora()
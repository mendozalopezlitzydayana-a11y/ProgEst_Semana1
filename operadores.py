# Autor: Litzy Mendoza
# Ejercicio 2 - Operaciones con dos números
# Solicita dos números y muestra suma, resta, multiplicación, división, división entera, residuo y potencia

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
residuo = num1 % num2
potencia = num1 ** num2

print("\n--- OPERACIONES ---")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print(f"División entera: {num1} // {num2} = {division_entera}")
print(f"Residuo: {num1} % {num2} = {residuo}")
print(f"Potencia: {num1} ** {num2} = {potencia}")

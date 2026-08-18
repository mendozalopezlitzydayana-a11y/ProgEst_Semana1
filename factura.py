# Autor: Litzy Mendoza
# Ejercicio 4 - Factura básica
# Solicita nombre del producto, precio y cantidad, calcula el subtotal y muestra un resumen

producto = input("¿Nombre del producto? ")
precio = float(input("¿Precio unitario? $"))
cantidad = int(input("¿Cantidad? "))

subtotal = precio * cantidad

print("\n--- RESUMEN DE COMPRA ---")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal:.2f}")

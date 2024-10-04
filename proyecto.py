# lista de opciones
print('''
Menu de Opciones:
      1. Alta nuevos productos
      2. Consulta de datos de producto
      3. Modificar cantidad de stock de producto
      4. Dar de baja producto
      5. Listas de productos con cantidad baja minimo
      7. Salir
''')

opcion = int(input('Por favor elija una opcion: '))
print('Haz elegido la opcion '+ str(opcion))

# calculo del IVA

precio = int(input('Escrib el monto neto: ' ))
iva = int(input('escriba el porcentaje de iva '))

precio_iva = (precio * iva) / 100
monto_total = precio + precio_iva

print('el monto de su compra es : ', str(monto_total))


# Calculo descuento 

precio = int(input('Escrib el monto neto: ' ))
descuento = int(input('escriba el porcentaje de descuento '))

precio_descuento = (precio * descuento) / 100
monto_total = precio - precio_descuento

print('el monto de su compra es : ', str(monto_total))


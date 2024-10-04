produ = {}

productos = int(input('cuantos productos quieres?: '))

for i  in range(productos):
    mercancia = str(input('que producto desea : '))
    cantidad = int(input('cuantos ? '))
    produ[mercancia]= cantidad

print(produ)





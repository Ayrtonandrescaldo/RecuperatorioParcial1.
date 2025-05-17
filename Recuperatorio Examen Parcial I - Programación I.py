nombres = []
cantidades = []
salir = True

while salir:
    print("\nMenú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Consultar stock de un producto")
    print("6. Salir")

    opcion = input("seleccione una opción: ")

    if opcion == "1":
        nombre = input("nombre del producto: ")
        cantidad = int(input("cantidad en stock: "))
        nombres.append(nombre)
        cantidades.append(cantidad)
        print("producto agregado con exito.")

    elif opcion == "2":
        print("productos agotados:")
        agotados = False
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print(nombres[i])
                agotados = True
        if not agotados:
            print("no hay productos agotados.")

    elif opcion == "3":
        producto = input("nombre del producto a actualizar: ")
        if producto in nombres:
            index = nombres.index(producto)
            nueva_cantidad = int(input("nueva cantidad: "))
            cantidades[index] = nueva_cantidad
            print("stock actualizado.")
        else:
            print("producto no encontrado.")

    elif opcion == "4":
        print("listado de productos:")
        for i in range(len(nombres)):
            print(nombres[i], cantidades[i])

    elif opcion == "5":
        producto = input("ingrese el nombre del producto a consultar: ")
        if producto in nombres:
            index = nombres.index(producto)
            print("stock disponible:", cantidades[index])
        else:
            print("Producto no encontrado.")

    elif opcion == "6":
        print("gracias por usar el sistema.")
        salir = False

    else:
        print("opción invalida.")
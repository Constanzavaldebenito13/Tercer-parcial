
espacio_disponibles=60
cantidad=0
ocupados=0
liberados=0
print("¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")

while True: 
    print("=== MENÚ PRINCIPAL ===")
    print("1. Espacios disponibles")
    print("2. Ocupar espacio")
    print("3. Liberar espacio")
    print("4. Espacios actualmente ocupados")
    print("5. Salir")

    while True:
        try:
            opc=int(input("Seleccione una opcion entre 1 y 5: "))
            if opc <1 or opc >5:
                print("Seleccione una opcion valida entre 1 y 5: ")
            else:
                break
        except:
            print("Solo se permiten numeros enteros (1,2,3,4,5): ")

    if opc == 1:
        print(f"La cantidad de espacios disponible actualmente es de {espacio_disponibles}")
    
    elif opc == 2:
        while True:
            try:
                cantidad=int(input("Ingrese la cantidad de espacios que desea ocupar"))
                if cantidad <=0 :
                    print("Cantidad inválida. Ingresa un número entero mayor a 0.")
                    continue
                elif cantidad > espacio_disponibles:
                    print("No hay suficientes espacios disponibles para realizar la ocupación.")
                    break
                else:
                    espacio_disponibles-=cantidad
                    ocupados+=cantidad
                    print("Ocupacion realizada correctamente")
                    break
            except:
                print("Ingrese un numero entero")

    elif opc == 3:
        while True:
            try:
                liberados=int(input("Ingrese la cantidad de espacios por liberar"))
            
                if liberados <=0:
                    print("Cantidad inválida. Ingresa un número entero mayor a 0.")
                    continue
                elif liberados > ocupados:
                    print("No puedes liberar más espacios de los que están ocupados actualmente.")
                    break
                elif liberados > 60:
                    print("No puede superar la capacidad maxima")
                else:
                    espacio_disponibles+=liberados
                    ocupados-=liberados
                    print("Liberación realizada correctamente.")
                    break
            except:
                print("Ingrese un numero entero")

    elif opc == 4:
        print(f"Espacios actualmente ocupados: {ocupados}")

    elif opc == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")







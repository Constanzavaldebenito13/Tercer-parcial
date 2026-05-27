AUTO=3000
MOTOS=1500
CAMIONETAS=4000

capacidad_estacionamiento=0
estacionamientos_utilizados=0

cantidad_estacionamiento_autos=0
cantidad_estacionamiento_motos=0
cantidad_estacionamiento_camionetas=0
contador_vehiculos_salida=0
acumulador_pago_vehiculos_salida=0

while True:
    try:
        capacidad_estacionamiento=int(input("Ingrese la capacidad maxima del estacionamiento: "))
        if capacidad_estacionamiento<=0:
            print("La capacidad del estacionamiento no puede ser menor o igual a 0.")
        else:
            break
    except Exception:
        print("Solo se permiten numeros enteros.")

while True:
    print("1 - Registrar entrada de vehiculos")
    print("2 - Registrar salida del vehiculo")
    print("3 - Visualizar el estado del estacionamiento")
    print("4 - Reporte general del estacionamiento")
    print("5 - Salir")

    while True:
        try:
            opc=int(input("Seleccione una opcion: "))
            if opc <1 or opc > 5:
                print("Las opciones disponibles son(1,2,3,4,5)")
            else:
                break
        except:
            print("Solo se permiten numeros enteros")

    if opc == 1 :

        estacionamientos_utilizados = cantidad_estacionamiento_autos + cantidad_estacionamiento_motos + cantidad_estacionamiento_camionetas
    
        if estacionamientos_utilizados >= capacidad_estacionamiento:
            print("Lo siento,el estacionamiento se encuentra lleno")
            continue

        print("Tipos de vehiculo")
        print("1 - Auto")
        print("2 - Moto")
        print("3 - Camioneta")


        while True:
            try:
                tipo_vehiculo=int(input("Ingrese el tipo de vehiculo(1,2,3)"))
                if tipo_vehiculo < 1 or tipo_vehiculo > 3 :
                   print("Las opciones disponibles son (1,2,3)") 
                else:
                    break
            except:
                print("Solo se permiten numeros enteros")

        if tipo_vehiculo == 1:
            print("Auto registrado!")
            cantidad_estacionamiento_autos += 1
        if tipo_vehiculo == 2:
            print("Moto registrada!")
            cantidad_estacionamiento_motos += 1
        if tipo_vehiculo == 3:
            print("Camioneta registrada!")
            cantidad_estacionamiento_camionetas += 1

    if opc == 2:       
        estacionamientos_utilizados = cantidad_estacionamiento_autos + cantidad_estacionamiento_motos + cantidad_estacionamiento_camionetas  
        if estacionamientos_utilizados == 0:
            print("No hay vehiculos estacionados")
            continue

        print("Tipos de vehiculo")
        print("1 - Auto")
        print("2 - Moto")
        print("3 - Camioneta")


        while True:
            try:
                tipo_vehiculo=int(input("Ingrese el tipo de vehiculo(1,2,3)"))
                if tipo_vehiculo < 1 or tipo_vehiculo > 3 :
                   print("Las opciones disponibles son (1,2,3)") 
                else:
                    break
            except:
                print("Solo se permiten numeros enteros")


          
        if tipo_vehiculo == 1 and cantidad_estacionamiento_autos == 0:
            print("No hay autos estacionados")
            continue

        if tipo_vehiculo == 2 and cantidad_estacionamiento_motos == 0:
            print("No hay motos estacionadas")
            continue

        if tipo_vehiculo == 3 and cantidad_estacionamiento_camionetas == 0:
            print("No hay camionetas estacionadas")
            continue


        while True:
            try:
                hora_estacionamiento=int(input("Ingrese las horas del estacionamiento"))
                if hora_estacionamiento <= 0:
                    print("El tiempo ingresado no debe ser menor o igual a cero")
                else:
                    break
            except:
                print("Solo se permiten numeros enteros")     
        

        if tipo_vehiculo == 1:
            cantidad_estacionamiento_autos -= 1
            pago=hora_estacionamiento*AUTO
            print("Registro de salida del auto correctamente")

        if tipo_vehiculo == 2:
            cantidad_estacionamiento_motos -= 1
            pago=hora_estacionamiento*MOTOS
            print("Registro de salida de la moto correctamente")

        if tipo_vehiculo == 3:
            cantidad_estacionamiento_camionetas -= 1
            pago=hora_estacionamiento*CAMIONETAS
            print("Registro de salida de la camioneta correctamente")

        
        contador_vehiculos_salida += 1
        acumulador_pago_vehiculos_salida += pago

        print("======BOLETA======")
        if tipo_vehiculo == 1:
            print("Tipo vehiculo: AUTO")
        if tipo_vehiculo == 2:
            print("Tipo de vehiculo: MOTO")
        if tipo_vehiculo == 3:
            print("Tipo de vehiculo: CAMINIONETA")
        
        print(f"Horas estacionamiento: {hora_estacionamiento}")
        print(f"Total a pagar: ${pago}")
        

    if opc == 3:

        estacionamientos_utilizados=cantidad_estacionamiento_autos+cantidad_estacionamiento_motos+cantidad_estacionamiento_camionetas

        print("Estacionamientos utilizados: ",estacionamientos_utilizados)
        print("Estacionamientos disponibles: ",capacidad_estacionamiento - estacionamientos_utilizados)
        print("Capacidad maxima ",capacidad_estacionamiento)
        print("AUTOS: ",cantidad_estacionamiento_autos)
        print("MOTOS: ",cantidad_estacionamiento_motos)
        print("CAMIONETAS: ",cantidad_estacionamiento_camionetas)
        
    if opc == 4:
        print("Total vehiculos estacionados: ",contador_vehiculos_salida)
        print("Total recaudado del día: ",acumulador_pago_vehiculos_salida)
        

        
    if opc == 5:
        print("Salir")
        break
habitacion=0
num_habitacion=0
tarifa_nocturna=0
suite=0
estandar=0
print("Hola,bienvenido a Hotel Corporativo Internacional.")

#Preguntar la cantidad de habitaciones 
while True:
    try:
        habitacion=int(input("Ingrese la cantidad de habitaciones que desea registrar"))
        if habitacion <1:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        else:
            break
    except Exception:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")


#Registro por habitación 

for i in range(habitacion):
    print(f"Registro de habitación exitoso {i + 1} de {habitacion}")

    while True:
    
        num_habitacion=input("Ingrese el numero de habitacion(Este puede contener letras y numeros)")
        if len(num_habitacion)<6 and " " not in num_habitacion:
            print("¡Número de habitación inválido! Debe tener al menos 6 caracteres y no contener espacios!")
        else:
            break
   
#Tarifa y asignacion de habitacion
    while True:
        try:
            tarifa_nocturna=int(input("Ingrese la tarifa noctura de la habitacion"))
            if tarifa_nocturna <1:
                print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")
            else:
                break
        except:
            print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")

    if tarifa_nocturna >90000:
        print("Su habitacion sera Suite Ejecutiva")
        suite+=1
    if tarifa_nocturna <= 90000:
        print("Su habitacion sera Estándar")
        estandar+=1
#Boleta?,salida
print("Resumen de reserva")
print(f"¡El hotel cuenta con {suite} Suites Ejecutivas y {estandar} Habitaciones Estándar! ¡Check-in disponible!")
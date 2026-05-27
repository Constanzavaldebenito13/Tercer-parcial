PIKACHU_ROLL=4500
OTAKU_ROLL=5000
PULPO_VENENOSO_ROLL=5200
ANGUILA_ELECTRICA_ROL=4800

carrito=0
subtotal=0
monto_descuento=0
total=0

descuento=0
codigo_descuento=0
soyotaku=0

sushi_pikachu=0
sushi_otaku=0
sushi_pulpo=0
sushi_anguila=0

print("Bienvenido a SushiDuoc")

while True:
    
    print("Menu")
    print("1. Pikachu roll $4500")
    print("2. Otaku roll $5000")
    print("3. Pulpo venenoso roll $5200")
    print("4. Anguila Eléctrica roll $4800")
    print("5. Ver carrito de compras")

    while True:
        try:
            opc=int(input("Ingrese su pedido (1,2,3,4,5)"))
            if opc <1 or opc >5:
                print("Seleccione solo las siguientes opciones (1,2,3,4,5)")
            else:
                break
        except:
            print("Solo se permiten numeros enteros")       
    
    if opc == 1:
        print("Has añadido pikachu roll a tu carrito")
        sushi_pikachu+=1
        subtotal=sushi_pikachu*PIKACHU_ROLL
    elif opc == 2:
        print("Has añadido Otaku roll a tu carrito")
        sushi_otaku+=1
        subtotal=sushi_otaku*OTAKU_ROLL
    elif opc == 3:
        print("Has seleccionado Pulpo venenoso roll")
        sushi_pulpo+=1
        subtotal=sushi_pulpo*PULPO_VENENOSO_ROLL
    elif opc == 4:
        print("Has seleccionado Anguila Electrica roll")
        sushi_anguila+=1
        subtotal=sushi_anguila*ANGUILA_ELECTRICA_ROL
    elif opc == 5:
        carrito=sushi_pikachu+sushi_otaku+sushi_pulpo+sushi_anguila
        print("Su carrito de compras es el siguiente: ")
        print("Pikachu roll: ",sushi_pikachu)
        print("Otaku roll: ",sushi_otaku)
        print("Pulpo venenoso roll",sushi_pulpo)
        print("Anguila electrica roll",sushi_anguila)
        break

while True:
    codigo_descuento=input("Ingrese codigo de descuento(S/N)")

    if codigo_descuento=="N":
        descuento=0
    if codigo_descuento=="S":
        soyotaku=input("Ingrese codigo de descuento0")
    if soyotaku=="soyotaku":
        descuento=10
        print("Tienes un descuento del 10%")
        break
    else:
        print("Codigo no valido")
        x=input("Presione x para volver a ingresar su codigo")
        if x!="x":
            break

monto_descuento=subtotal*(1-(descuento/100))
total=monto_descuento-subtotal



print("=====Boleta=====")
print(f"TOTAL PRODUCTOS: {carrito}")
print("**********************")
print(f"Subtotal por pagar:{subtotal}")
print(f"Descuento por código: %{descuento} {total}")
print(f"TOTAL: {monto_descuento}")
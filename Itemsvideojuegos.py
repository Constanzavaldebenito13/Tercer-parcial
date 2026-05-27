print("Hola,bienvenido a storeduocwatch")

while True:
    nombre=input("Ingrese su nombre")
    if len(nombre)>=3:
        break
    else:
        print("El nombre no puede tener menos de 3 caracteres")

while True:
    rut=input("Ingrese su RUT(Sin punto ni guion)")
    if rut.isdigit() and len(rut) == 8:
        break 
    else:
        print("El Rut solo debe tener 8 digitos")  

while True:
    dv=input("Ingresa tu digito verificador:")  
    if len(dv)==1 and (dv.isdigit() or dv == "K"):    
    
        break

    else:
        print("Error")

items=0
precio=0
total=0
preciofinal=0

print("=======ITEMS======")
print("1.Espada, 5000 pesos")
print("2.Arco, 7000 pesos")
print("3.Bastón Mágico, 9000 pesos")
print("4.Salir")


while True:

    items=int(input("Ingresa los items a comprar: "))

    if items==1:
        print("Has elegido la espada")
        preciofinal+=5000
    elif items==2:
        print("Has elegido el arco")
        preciofinal+=7000
    elif items==3:
        print("Has elegido el bastón mágico")
        preciofinal+=9000
    elif items==4:
        print("Has elegido salir")
        break
    else:
        print("Elige un item válido")
    
print("\n---BOLETA---")
print("NOMBRE: ",nombre)
print("RUT: ",rut)
print("TOTAL A PAGAR: ",preciofinal)



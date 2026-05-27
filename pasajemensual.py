print("Bienvenido a busesDuoc")

distancia=0
descuento=0
total_neto=0
total_final=0
total_descuento=0
pasaje_mensual=95000
emision_tarjeta=5000

nombre=input("Ingrese su nombre")

while True:
    rut=input("Ingrese su RUT(Sin puntos ni guion)")
    if rut.isdigit() and len(rut)==8:
        break
    else:
        print("Su RUT solo debe tener 8 digitos")


while True:
    dv=input("Ingrese su digito verificador")
    if len(dv)==1 and (dv.isdigit() or dv == "K"):
        break
    else:
        print("Error")

print("El valor pasaje mensual es 95000")
print("El valor de emision de la tarjeta es de 5000")

distancia=int(input("Ingrese su tramo en km,sin puntos"))

categoria=int(input("Ingrese su categoria(1,2,3,4)"))

if distancia>=400 and categoria==1 or categoria==2:
    descuento=20
elif distancia<=400 and categoria==3 or categoria==4:
    descuento=14

total_neto=pasaje_mensual+emision_tarjeta

total_descuento=1-(descuento/100)

total_final=total_neto*total_descuento

print("======BOLETA======")
print(f"NOMBRE: {nombre}")
print(f"RUT: {rut}")
print("DESCUENTO: %",descuento)
print("TOTAL A PAGAR: $",total_final)

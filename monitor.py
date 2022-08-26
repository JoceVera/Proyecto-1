print("Producción por día\n")

def rendimiento (ropaxdia,ropatotal,numpersonal):
    proxperso=ropaxdia/numpersonal
    predic=((ropatotal-ropaxdia)*8)/ropaxdia
    return proxperso, predic

cantidad=0   

seguimiento=int(input("¿Desea agregar un proceso?\n1.Si  2.No\n"))

if seguimiento==1:
    ped=input("\nIngresa el nombre de corte: ")
    per=int(input("Personas que laboraron: "))
    pedtot=int(input("Cantidad total de pantalones en pedido:"))
    xdia=int(input("Cantidad de pantalones terminados:"))
    promedio,tiempres=rendimiento(xdia,pedtot,per)
    print("El promedio de piezas por persona es de%.2f "%promedio)
    print("Aproximadamente faltan %.2f" %tiempres,"horas de trabajo del pedido")
    cantidad+=xdia
    print("\nCantidad de pantalones fabricados hoy:",cantidad)
elif seguimiento==2:
    print("No hay cortes por hoy")
else:
    print("Respuesta no valida")
print("\nOperación terminada")







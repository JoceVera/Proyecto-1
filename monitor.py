print("Producción por día\n")

from datetime import date

"""Operaciones el rendimiento de la producción"""
def rendimiento (piezas_dia, piezas_pedido, num_personal):
    promedio_persona = piezas_dia/num_personal
    estimacion = ((piezas_pedido - piezas_dia)*8)/piezas_dia
    piezas_restantes= piezas_pedido - piezas_dia
    return promedio_persona,estimacion,piezas_restantes

"""Mensajes que devuelven los cáculos realizados al usuario"""
def resultados (promedio_persona,estimacion,piezas_restantes,cantidad_diaria,\
                fecha):
    print("\nEl promedio de piezas por persona es de %.2f "%promedio_persona,\
          "piezas.")
    print("\nAproximadamente faltan:\n %.2f" %estimacion,"horas de trabajo.\n",\
          int(piezas_restantes),"piezas para completar el pedido.")
    print("\nLa cantidad de piezas fabricadas el",hoy,"fue de",\
          cantidad_diaria,".")
    
"""Información de secciones"""
def secciones (letra_seccion):
    band=1
    while band:
        if letra_seccion == "A":
            band = 0
            personas_total=150
            return int(personas_total)
        elif letra_seccion == "B":
            band = 0
            personas_total=250
            return int(personas_total)
        elif letra_seccion == "C":
            band = 0
            personas_total=200
            return int(personas_total)
        elif letra_seccion =="D":
            band = 0
            personas_total=275
            return int(personas_total)
        elif letra_seccion =="E":
            band = 0
            personas_total=300
            return int(personas_total)
        else:
            letra_seccion = str(input("Sección no válida\nEscribe la letra en"\
                                      " mayúscula correspondiente a la sección"\
                                    "de producción:\n"))  
                                          
hoy=date.today()
cantidad_dia = 0   

inicio = int(input("¿Desea agregar un nuevo proceso? \n\nIngrese el número de la opción"\
                   " correpondiente \n          1.Si  2.No\n"))
band=1
while band:
    """Información requerdida opara generar cálculos de producción"""
    if inicio ==1:
        band=0
        print ("\nIngresa la información del pedido...\n")
        nombre_pedido = str(input("Ingresa el nombre de corte: "))
        seccion = str(input("\nEscribe la letra correspondiente a"\
                        " la sección de producción:\n"\
                        "        A   B   C   D   E   \n"))
        personal = secciones (seccion)
        pedido_total = int(input("\nCantidad total de piezas en pedido:"))
        produccion_dia = int(input("\nCantidad de piezas terminados:"))
        promedio_produccion_dia, tiempo_restante,faltantes = \
                         rendimiento(produccion_dia,pedido_total,personal)
        cantidad_dia += produccion_dia
        resultados (promedio_produccion_dia,tiempo_restante,faltantes,cantidad_dia,hoy)
    elif inicio == 2:
        band=0
        print("\nNo hay más cortes por hoy...")
    else:
        inicio = int(input("\nRespuesta no válida...\n\n"\
                           "¿Desea agregar un nuevo proceso? \n\nIngrese la opción"\
                           " correpondiente \n          1.Si  2.No\n"))   

print("Regresa pronto.")

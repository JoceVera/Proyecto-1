print("Producción por día\n")

from datetime import date
  
def rendimiento (piezas_dia, piezas_pedido, num_personal):
    """Operaciones el rendimiento de la producción"""
    promedio_persona = piezas_dia/int (num_personal)
    estimacion = ((piezas_pedido - piezas_dia)*8)/piezas_dia
    piezas_restantes= piezas_pedido - piezas_dia
    return promedio_persona,estimacion,piezas_restantes

def resultados (promedio_persona,estimacion,piezas_restantes,cantidad_diaria,\
                fecha):
    """Mensajes que devuelven los cáculos realizados al usuario"""
    
    print("\nEl promedio de piezas por persona es de %.2f "%promedio_persona,\
          "piezas.")
    print("\nAproximadamente faltan:\n %.2f" %estimacion,"horas de trabajo.\n",\
          int(piezas_restantes),"piezas para completar el pedido.")
    print("\nLa cantidad de piezas fabricadas el",hoy,"fue de",\
          cantidad_diaria,".")
    
def secciones (letra_seccion):
    """Información de secciones"""
    if letra_seccion == "A":
        personas_total=150
        return int(personas_total)
    elif letra_seccion == "B":
        personas_total=250
        return int(personas_total)
    elif letra_seccion == "C":
        personas_total=200
        return int(personas_total)
    elif letra_seccion =="D":
        personas_total=275
        return int(personas_total)
    elif letra_seccion =="E":
        personas_total=300
        return int(personas_total)
    else:
        """Validación de sección"""
        while letra_seccion != "A" and letra_seccion != "B" and \
              letra_seccion != "C" and letra_seccion != "D" and \
              letra_seccion != "E":
            letra_seccion = str(input("Sección no válida\nEscribe la letra en"\
                                      " mayúscula correspondiente a la sección"\
                                      "de producción:\n"))
        else: 
            personas_total= secciones(letra_seccion)
        return int(personas_total)
            

hoy=date.today()
cantidad_dia = 0   

inicio = int(input("¿Desea agregar un nuevo proceso? \n\nIngrese la opción"\
                   " correpondiente \n          1.Si  2.No\n"))

if inicio == 1:
    """Información requerdida opara generar cálculos de producción"""

    print ("\nIngresa la información del pedido...\n")
    
    nombre_pedido = str(input("Ingresa el nombre de corte: "))
    seccion = str(input("\nEscribe la letra correspondiente a"\
                        " la sección de producción:\n"\
                        "        A   B   C   D   E   F \n"))
    
    personal = secciones (seccion)
    pedido_total = int(input("\nCantidad total de piezas en pedido:"))
    produccion_dia = int(input("\nCantidad de piezas terminados:"))
    promedio_produc_dia, tiempo_restante,faltantes = \
                         rendimiento(produccion_dia,pedido_total,personal)
    cantidad_dia += produccion_dia
    resultados (promedio_produc_dia,tiempo_restante,faltantes,cantidad_dia,hoy)

elif inicio == 2:
    print("\nNo hay cortes por hoy...")

else:
    print("\nRespuesta no válida...")
    

print("Regresa pronto.")

print("Producción por día\n")

def rendimiento (piezas_dia, piezas_pedido, num_personal):
    """Operaciones el rendimiento de la producción"""

    promedio_persona = piezas_dia/num_personal
    estimacion = ((piezas_pedido-piezas_dia)*8)/piezas_dia
    piezas_restantes= piezas_pedido - piezas_dia
    return promedio_persona,estimacion,piezas_restantes

def resultados (promedio_persona,estimacion,piezas_restantes,cantidad_diaria):
    """Mensajes que devuelven los cáculos realizados al usuario"""
    
    print("\nEl promedio de piezas por persona es de %.2f "%promedio_persona,\
          "pantalones")
    print("\nAproximadamente faltan %.2f" %estimacion,"horas de trabajo y",\
          int(piezas_restantes),"piezas para completar el pedido")
    print("\n La cantidad de pantalones fabricados hoy fue de",cantidad_diaria)
    

cantidad_dia = 0   

inicio = int(input("¿Desea agregar un nuevo proceso?\n1.Si  2.No\n"))

if inicio == 1:
    """Información requerdida opara generar cálculos de producción"""

    nombre_pedido = input("\nIngresa el nombre de corte: ")
    seccion = int(input("\nNúmero de sección:"))
    personal = int(input("Personas que laboraron: "))
    pedido_total = int(input("Cantidad total de piezas en pedido:"))
    produccion_dia = int(input("Cantidad de piezas terminados:"))
    promedio_produc_dia, tiempo_restante,faltantes = rendimiento\
                                                     (produccion_dia,pedido_total,\
                                                     personal)
    cantidad_dia += produccion_dia
    
    resultados (promedio_produc_dia,tiempo_restante,faltantes,cantidad_dia)


elif inicio == 2:
    print("No hay cortes por hoy")

else:
    print("Respuesta no valida")
    

print("\nOperación terminada")







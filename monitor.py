from datetime import date

def inicio_01 (lista):
    """Pide toda la información del pedido"""
    print ("\n  Información del pedido...\n")
    nombre_pedido = str(input("Ingresa el nombre de corte: "))
    lista.append(nombre_pedido)
    seccion = str(input("\nEscribe la letra correspondiente a"\
                        " la sección de producción:\n"\
                        "        A   B   C   D   E   \n"))
    personal = secciones (seccion)
    piezas_total,piezas_dia= datos (lista)
    promedio_produccion_dia, tiempo_restante,faltantes = \
                         rendimiento(piezas_dia,piezas_total,personal)
    lista.append (promedio_produccion_dia)
    resultados_restantes (tiempo_restante,faltantes,lista)

    inicio = str(input("\n\n¿Desea agregar un otro proceso?"
                       "\n(Ingrese el número"\
                       " de la opción correpondiente)\n         1.Si  2.No\n"))
    return inicio,piezas_dia
    
def secciones (letra_seccion):
    """Asigna la cantidad de personal de acuerdo a la sección"""
    band=1
    while band:
        if letra_seccion == "A" or letra_seccion == "a":
            band = 0
            return 150
        elif letra_seccion == "B" or letra_seccion == "b":
            band = 0
            return 250
        elif letra_seccion == "C" or letra_seccion == "c":
            band = 0
            return 200
        elif letra_seccion =="D" or letra_seccion == "d":
            band = 0
            personas_total=275
            return int(personas_total)
        elif letra_seccion =="E"or letra_seccion == "e":
            band = 0
            return 300
        else:
            letra_seccion = str(input("Sección no válida\nEscribe la letra"\
                                      " correspondiente a la sección"\
                                    "de producción:\n"))           
def datos (lista):
    """Validación de los datos iniciales de la producción:
la producción del día no puede ser mayor a la total"""
    pedido_total = int(input("\nCantidad total de piezas en pedido: "))
    produccion_dia = int(input("\nCantidad de piezas terminados: "))
    band=1
    while band:
        if pedido_total < produccion_dia:
            print("Algo esta mal, hay más piezas que las necesarias..."\
                  "Ingrese lo datos correctos: ")
            pedido_total = int(input("\nCantidad total de piezas en pedido:"))
            produccion_dia = int(input("\nCantidad de piezas terminados: "))
        else:
            band=0
    lista.append(produccion_dia)
    return pedido_total, produccion_dia

def rendimiento (piezas_dia, piezas_pedido, num_personal):
    """Operaciones realizadas sobre cada pedido respecto a su producción"""
    promedio_persona = piezas_dia/num_personal
    estimacion = ((piezas_pedido - piezas_dia)*8)/piezas_dia
    piezas_restantes= piezas_pedido - piezas_dia
    return promedio_persona,estimacion,piezas_restantes

def resultados_restantes (estimacion,piezas_restantes,lista):
    """Mensajes sobre el tiempo de producción y piezas  restante por pedido"""
    print("\nAproximadamente faltan:\n %.2f" %estimacion,"horas de trabajo y",\
          int(piezas_restantes),"piezas para completar el pedido.")

def resumen_dia (lista):
    """Genera el resumen de los procesos del día haciendo uso de una lista"""
    contador=1
    nombre= 0
    produccion= 1
    rendimiento_dia= 2
    print("Pedidos:")
    while contador <=(len (lista)/3):
        print("  El pedido",lista[nombre],"realizó",lista[produccion],"piezas"\
              " con un rendimiento de %.2f" % lista[rendimiento_dia],"piezas"\
              " por persona.")
        nombre+=3
        produccion+=3
        rendimiento_dia+=3
        contador+=1
    


"""Variables y datos reutilizables durante todo el proceso"""
hoy=date.today()
cantidad_diaria= 0   
resumen=[]


"""Programación principal"""

print("\n        Producción por día\n")
inicio = str(input("¿Desea agregar procesos? \n(Ingrese el número de"\
                   " la opción correpondiente) \n          1.Si  2.No\n"))

"""Validación de respuesta de inicio"""
band=1
while band:
    while inicio =="1":
        band=0
        inicio,cantidad_dia=inicio_01 (resumen)
        cantidad_diaria += cantidad_dia
    if inicio == "2":
        band=0
        print("\nNo hay más procesos por hoy...")
    else:
        band=1
        inicio = input("\nRespuesta no válida..."\
                           "\n¿Desea agregar un nuevo proceso? \n(Ingrese la"\
                          " opción correpondiente) \n          1.Si  2.No\n")

print("\n\n Resumen del",hoy,":\n")
resumen_dia(resumen)

print("\nEl total de piezas"\
      " fabricadas fue de", cantidad_diaria,".\n\nRegresa pronto.")

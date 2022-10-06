from datetime import date


def inicio_01 (matriz):
    """Pide toda la información del pedido"""
    print ("\n      Información del pedido...\n")
    nombre_pedido = str(input("Ingresa el nombre del pedido: "))
    seccion = str(input("Escribe la letra correspondiente a"\
                        " la sección de producción:\n"\
                        "        A   B   C   D   E   \n"))
    personal = secciones (seccion)
    piezas_total,piezas_dia= datos ()
    promedio_produccion_dia, tiempo_restante,faltantes = \
                         rendimiento(piezas_dia,piezas_total,personal,horas_de_trabajo)
    matriz.append(crear_lista(nombre_pedido,personal,piezas_dia,promedio_produccion_dia, tiempo_restante,faltantes))

    inicio = str(input("\n\n¿Desea agregar otro proceso?\n  Ingrese"\
                       " la opción correpondiente\n         1.Si  2.No\n"))
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
            letra_seccion = str(input("Sección no válida...Escribe la letra"\
                                      " correspondiente a la sección"\
                                    "de producción:\n"))           
def datos ():
    """Validación de los datos iniciales de la producción:
la producción del día no puede ser mayor a la total"""
    pedido_total = int(input("Cantidad total de piezas en pedido: "))
    produccion_dia = int(input("Cantidad de piezas terminados: "))
    band=1
    while band:
        if pedido_total < produccion_dia:
            print("\nAlgo esta mal, hay más piezas que las necesarias..."\
                  "Ingrese lo datos correctos: ")
            pedido_total = int(input("Cantidad total de piezas en pedido:"))
            produccion_dia = int(input("Cantidad de piezas terminados: "))
        else:
            band=0
    return pedido_total, produccion_dia

def rendimiento (piezas_dia, piezas_pedido, num_personal,horas_de_trabajo):
    """Operaciones realizadas sobre cada pedido respecto a su producción"""
    promedio_persona = piezas_dia/num_personal
    piezas_restantes= piezas_pedido - piezas_dia
    estimacion = (piezas_restantes*horas_de_trabajo)/piezas_dia
    return promedio_persona,estimacion,piezas_restantes

def crear_lista (pedido,cantidad_personas,produccion,promedio,tiempo,resto):
    """Crea una lista por cada pedido con su respectiva información"""
    lista=[]
    lista.append(pedido)
    lista.append(cantidad_personas)
    lista.append(produccion)
    lista.append(promedio)
    lista.append(tiempo)
    lista.append(resto)
    return lista

def resumen_dia (matriz):
    """Genera el resumen de los procesos del día haciendo uso de una lista"""
    nombre= 0
    produccion= 2
    rendimiento_dia= 3
    estimacion=4
    piezas_restantes=5
    if (len (matriz))== 0:
        print ("Pedidos:\n   No hubo pedidos.")
    else:
        print("Pedidos:\n")
        indice_01 = 0
        while indice_01 < len(matriz):
            indice=0
            while indice < 1:
                print(" \n   El pedido",matriz[indice_01][nombre],"realizó",matriz[indice_01][produccion],\
                      "piezas con un rendimiento de %.2f" % matriz[indice_01][rendimiento_dia],"piezas"\
                      " por persona.Aproximadamente faltan %.2f" % matriz[indice_01][estimacion],\
                      "horas de trabajo y", int(matriz[indice_01][piezas_restantes]),\
                                                  "piezas para completar el pedido.")
                indice+=1
            indice_01+=1
    

"""Variables y datos reutilizables durante todo el proceso"""
hoy=date.today()
cantidad_diaria= 0   
informacion_total=[]
horas_de_trabajo=8

"""Programación principal"""

print("\n        Producción por día\n")
inicio = str(input("¿Desea agregar procesos? \n Ingrese el número"\
                   " correpondiente \n          1.Si  2.No\n"))

"""Validación de respuesta de inicio"""
band=1
while band:
    while inicio =="1":
        band=0
        filas_matriz=0
        inicio,cantidad_dia=inicio_01 (informacion_total)
        cantidad_diaria += cantidad_dia
    if inicio == "2":
        band=0
    else:
        band=1
        inicio = input("\nRespuesta no válida..."\
                           "\n¿Desea agregar un nuevo proceso? \n Ingrese el"\
                          " número correpondiente \n          1.Si  2.No\n")

print("\n\n      Resumen del",hoy,"...\n")
resumen_dia(informacion_total)

productividad=cantidad_diaria/horas_de_trabajo
print("\n\nGeneral:\n El total de piezas"\
      " fabricadas fue de", cantidad_diaria," con una productividad total "\
      "de %.0f" % productividad,"piezas.\n\n\nRegresa pronto.")

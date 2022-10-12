"""
Producción por día.
El programa pregunta al usuario si desea ingresar información de pedidos,
solicita una serie de datos relacionado con el pedido, realiza
cálculos matemáticos para determinar el rendimiento de la sección respecto a la
producción del pedido y genera una estimación del producción restante.
Al final se generará un reporte general, en donde se muestre los resultados por
pedido, el total de piezas realizadas ese día y mostrará la productividad total
(considerando 8 horas laborales).
"""

#Bibliotecas
from datetime import date
"""Importat la fecha actual en que se corre el programa y mostrarla al momento
de dar el resumen. El método de uso e información al respecto fue conocido por
la página:https://codigofacilito.com/articulos/fechas-python """



"""
======================== funciones de validación ============================
"""    

def seleccion_inicio (inicio,cantidad_diaria ,informacion_total):

    """
    Recibe: la respuesta en str del menú de inicio, el valor piezas totales
    elaboradas y la matriz.
    Válida la respuesta de inicio, ocupa la función inicial de datos, suma
    la cantidad de piezas total.
    Devuelve: el dato numérico de piezas totales elaboradas.
    """
    
    band = 1
    while band:
        while inicio == "1":
            band = 0
            inicio,cantidad_dia = inicio_01 (informacion_total)
            cantidad_diaria += cantidad_dia
        if inicio == "2":
            band = 0
        else:
            band = 1
            inicio = input("\nRespuesta no válida..."\
                           "\n¿Desea agregar un nuevo proceso? \n Ingrese el"\
                          " número correpondiente \n          1.Si  2.No\n")
    return cantidad_diaria
    
def secciones (letra_seccion):
    
    """
    Recibe: la respuesta en str de la sección de producción.
    Asigna la cantidad de personal y válida la respuesta de la sección.
    Devuelve: el dato numérico entero de personal.
    """
    
    band = 1
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
        elif letra_seccion == "D" or letra_seccion == "d":
            band = 0
            return 275
        elif letra_seccion == "E" or letra_seccion == "e":
            band = 0
            return 300
        else:
            letra_seccion = str(input("Sección no válida...Escribe la letra"\
                                      " correspondiente a la sección"\
                                    "de producción:\n"))           
def datos ():
    
    """
    Pide la producción de día y la cantidad total de piezas de pedido.
    Realiza la validación de estos, considerando que la producción del día no
    puede ser mayor a la cantidad de piezas total del pedido.
    Devuelve: cantidad de producción del día y cantidad de piezas total del
    pedido en datos numéricos enteros.
    """
    
    pedido_total = int(input("Cantidad total de piezas en pedido: "))
    produccion_dia = int(input("Cantidad de piezas terminados: "))
    band = 1
    while band:
        if pedido_total < produccion_dia:
            print("\nAlgo esta mal, hay más piezas que las necesarias..."\
                  "Ingrese lo datos correctos: ")
            pedido_total = int(input("Cantidad total de piezas en pedido:"))
            produccion_dia = int(input("Cantidad de piezas terminados: "))
        else:
            band = 0
    return pedido_total, produccion_dia


"""
======================== funciones de cálculos ============================
"""

def rendimiento (piezas_dia, piezas_pedido, num_personal,horas_de_trabajo):
    
    """
    Recibe: las piezas del pedido realizadas en el día en entero,
    la cantidad de piezas totales en entero, el número de personas en
    entero y las horas de trabajo al día en entero.
    Realiza las operaciones del pedido respecto a su producción por persona,
    la cantidad de tiempo restante (regla de tres) y las piezas del pedido que
    faltan para completarlo.
    Devuelve: resultado del promedio por persona en float, la
    estimación del tiempo en float y las piezas que faltan producir en entero.
    """
    
    promedio_persona = piezas_dia/num_personal
    piezas_restantes = piezas_pedido - piezas_dia
    estimacion = (piezas_restantes*horas_de_trabajo)/piezas_dia

    return promedio_persona,estimacion,int(piezas_restantes)


"""
======================== funciones  auxiliares =============================
"""

def inicio_01 (matriz):
    
    """
    Recibe: la matriz que guarda toda la información.
    Pide la información del pedido, la agrega en una lista y esta a su
    vez en la matriz.
    Devuelve: el valor str de la sección y la cantidad entera de piezas
    realizadas por día.
    """
    
    print ("\n      Información del pedido...\n")
    nombre_pedido = str(input("Ingresa el nombre del pedido: "))
    seccion = str(input("Escribe la letra correspondiente a"\
                        " la sección de producción:\n"\
                        "        A   B   C   D   E   \n"))
    personal = secciones (seccion)
    piezas_total,piezas_dia = datos ()
    promedio_produccion_dia, tiempo_restante,faltantes = \
                         rendimiento(piezas_dia,piezas_total,personal,\
                                     HORAS_TRABAJO)
    matriz.append(crear_lista(nombre_pedido,personal,piezas_dia,\
                              promedio_produccion_dia, tiempo_restante,\
                              faltantes))

    inicio = str(input("\n\n¿Desea agregar otro proceso?\n  Ingrese"\
                       " la opción correpondiente\n         1.Si  2.No\n"))
    return inicio,int (piezas_dia)


def crear_lista (pedido,cantidad_personas,produccion,promedio,tiempo,resto):

    """
    Recibe: el nombre del pedido en str, la cantidad de personas
    laborando en entero, la producción del pedido actual en entero,
    el promedio por persona en float, la estimación del tiempo en float y las
    piezas que faltan producir en entero.
    Crea una lista por cada pedido y agrega los datos recibidos como parámetros.
    Devuelve: la lista creada del pedido
    """

    lista = []
    lista.append(pedido)
    lista.append(cantidad_personas)
    lista.append(produccion)
    lista.append(promedio)
    lista.append(tiempo)
    lista.append(resto)
    return lista

def resumen_dia (matriz):

    """
    Recibe: la matriz que guarda los pedidos del día.
    Genera el resumen de los pedidos del día, define las variables con el valor
    del indice en el que se encuentra la información en cada listas anidadas,
    imprime la información del pedido.
    """
    
    if (len (matriz)) == 0:
        print ("Pedidos:\n   No hubo pedidos.")
    else:
        print("Pedidos:")
        indice_01 = 0
        while indice_01 < len(matriz):
            indice = 0
            while indice < len(matriz[indice_01]):
                if indice == 0:
                    print ( " \n   El pedido",matriz[indice_01][indice],end="")
                elif indice == 2:
                    print ("realizó", matriz[indice_01][indice],"piezas",end="")
                elif indice == 3:
                    print ("con un rendimiento de %.2f" % matriz[indice_01]\
                           [indice],"piezas por persona.")
                elif indice == 4:
                    print("Aproximadamente faltan %.2f" % matriz[indice_01]\
                          [indice],"horas de trabajo",end="")
                elif indice == 5:
                    print (" y",int(matriz[indice_01][indice]),\
                      "piezas para completar el pedido.")
                indice += 1
            indice_01 += 1

"""
======================  Parte principal del programa =========================
"""

#Se definen las variables reutilizables durante todo el programa
hoy = date.today()  
HORAS_TRABAJO = 8

#Se inicializan las variables contadoras para ser reutilizados en las funciones 
cantidad_diaria = 0
informacion_total = []


print("\n        Producción por día\n")
inicio = str(input("¿Desea agregar procesos? \n Ingrese el número"
                   " correpondiente \n          1.Si  2.No\n"))

cantidad_diaria = seleccion_inicio (inicio, cantidad_diaria,informacion_total)

#Resumen
print("\n\n      Resumen del",hoy,"...\n")
resumen_dia (informacion_total)
productividad = cantidad_diaria/HORAS_TRABAJO
print("\n\nGeneral:\n El total de piezas"\
      " fabricadas fue de", cantidad_diaria," con una productividad total "\
      "de %.0f" % productividad,"piezas por hora.\n\n\nRegresa pronto.")

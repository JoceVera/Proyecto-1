# Proyecto-1
# Monitoreo de producción
### Contexto 
En la industria textil es importante llevar un monitoreo constante de la producción para poder tener un control y organización de sus procesos, pero también porque esto permite vislumbrar algunos problemas que se presentan en su elaboración para mejorar su funcionalidad. 
Un problema importante para las empresas antecesoras de la industria textil es la falta de implemento de procesos automatizados que permiten llevar este control más exacto, volviéndose una limitante para crecer y ser reconocidas en la industria. La importancia de implementar estos nuevos métodos de monitoreo recae en que ayudan a tener un mejor rendimiento, hacen más eficientes los procesos, permite identificar las áreas de oportunidad en las diferentes áreas, existe una mayor organización y sobre todo optimiza el tiempo de trabajo de las personas. Todo esto se ve reflejado en la calidad de los productos evitando que las empresas se conviertan en obsoletas (Tecnología para la industria, 2022).Este programa es un organizador que permite llevar un control más preciso y directo sobre el seguimiento en la manufacturación de un producto, esto con la finalidad de llevar un mejor control de la elaboración y tener una mayor productividad. 

### Algoritmo
#### Función extra
Se hace uso de la biblioteca "datetime" para importa la función "date" y colocar la fecha del día en el resumen final de los procesos. La manera de usarlo fue investigada de la página Código Facilito (Fechas con Python, s. f.). 
-       Fecha = date.today()

#### Estado inicial
El programa comenzará pidiendo al usuario que ingrese los datos del pedido como lo es el nombre (dato string), la cantidad de piezas por  pedido (dato entero), la cantidad de piezas realizadas (dato entero)  y se pedirá que  seleccione la letra de la sección en donde se está fabricando, respecto a ella se dará la información de la cantidad de personal. 

-       Importar biblioteca datetime
-       Inicio (str):  agregar pedido (1), terminar registro (2)
-       Información del pedido: nombre (str), cantidad (int), sección (str), cantidad producida (int), cantidad de personas (int)
-       Horas laboradas = 8 
-       Lista anidada de almacenamiento
 
#### Proceso
Una vez que se haya recopilado esta información se calculará la cantidad promedio de piezas generada por personas y se hará una estimación del tiempo restante para el término del proceso. Mostrando por cada pedido el tiempo de horas estimado en que se completara (haciendo uso de una regla de tres), así como las piezas restantes. Este proceso se realizará las veces necesarias de acuerdo a los pedidos en los que la empresa esté trabajando por día. 
-          While inicio por pedido (str)
-          While para validar información en rangos (inició, cantidades y secciones) 
-          Guardar información en variables (nombre-str, cantidades-int)
-          Usar dato str en while para validar sección
-          Asignar valor numérico (int) de personal por sección 
-          Calcular las predicciones (float/int): 

    *          Promedio (float)=cantidad elaborada/personas que laboraron
      
    *          Cantidad faltante (int)=cantidad total - cantidad elaborada
      
    *          Tiempo restante (float)= cantidad elaborada*horas de trabajo/cantidad 
      
    *          Guardar información del pedido y cálculos en la lista anidada (append)
      
    *          Calcular productividad del día (float)=cantidad total de piezas elaboradas/horas de trabajo

#### Estado final
Al final de toda la operación se dará un resumen de los pedidos, mostrando el nombre, las piezas que se fabricaron y el promedio de piezas realizadas por persona. Además se generará un reporte general, en donde se muestre el total de piezas realizadas ese día en la fábrica y mostrará la productividad (considerando 8 horas laborales).Por último, el sistema mostrará un mensaje diciendo que la operación realizada ha terminado.
-          While que imprime información de la matriz
-          Tiempo estimado de terminación (float)
-          Cantidad de piezas restantes (int)
-          Resumen final del pedido (str y listas)
-          Cantidad de piezas de todo el día (int)
-          Mensaje (str) de salida

### Fuentes

Fechas con Python. (s. f.). CódigoFacilito. Recuperado 7 de octubre de 2022, de
https://codigofacilito.com/articulos/fechas-python

Reto Directivos. (2021, 19 abril). Cómo calcular la productividad con ejemplos. El blog de retos para ser directivo | Desafíos de la Gestión Empresarial. Recuperado 29 de septiembre de 2022, de: https://retos-directivos.eae.es/como-calcular-la-productividad-con-ejemplos/

Tecnología para la industria. (2022, 30 junio). 10 maneras en las que el monitoreo en tiempo real de la fabricación mejora la precisión y la calidad.    Recuperado 18 de agosto de 2022, de: https://tecnologiaparalaindustria.com/10-maneras-en-las-que-el-monitoreo-en-tiempo-real-de-la-fabricacion-mejora-la-precision-y-la-calidad/

Para el formato de pseudocódigo se tomo como referencia el trabajo de mi compañera Angélica Ríos Cuentas.

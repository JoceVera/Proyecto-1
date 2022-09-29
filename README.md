# Proyecto-1
# Monitoreo de producción
### Contexto 
En la industria textil es importante llevar un monitoreo constante de la producción para poder tener un control y organización de sus procesos, pero también porque esto permite vislumbrar algunos problemas que se presentan en su elaboración para mejorar su funcionalidad. 
Un problema importante para las empresas antecesoras de la industria textil es la falta de implemento de procesos automatizados que permiten llevar este control más exacto, volviéndose una limitante para crecer y ser reconocidas en la industria. La importancia de implementar estos nuevos métodos de monitoreo recae en que ayudan a tener un mejor rendimiento, hacen más eficientes los procesos, permite identificar las áreas de oportunidad en las diferentes áreas, existe una mayor organización y sobre todo optimiza el tiempo de trabajo de las personas. Todo esto se ve reflejado en la calidad de los productos evitando que las empresas se conviertan en obsoletas (Tecnología para la industria, 2022).Este programa es un organizador que permite llevar un control más preciso y directo sobre el seguimiento en la manufacturación de un producto, esto con la finalidad de llevar un mejor control de la elaboración y tener una mayor productividad. 

### Algoritmo 
El programa comenzará pidiendo al usuario que ingrese los datos del pedido como lo es el nombre (dato string), la cantidad de piezas por  pedido (dato entero)  y se pedirá que  seleccione la letra de sección en donde se está fabricando y respecto a ella se le dará la información de la cantidad de personal trabajando. Una vez que se haya recopilado esta información se calculará la cantidad promedio de piezas generada por personas y se hará una estimación del tiempo restante para el término del proceso. Mostrando por cada pedido el tiempo de horas estimado en que se completara, así como las piezas restantes. Este proceso se realizará las veces necesarias de acuerdo a los pedidos en los que la empresa esté trabajando por día. 
 
La información sobre la cantidad de piezas realizadas y el rendimiento por cada pedido irá siendo guardada, pues al final de toda la operación se dará un resumen del total de piezas que se fabricaron y el promedio de piezas realizadas por personal de cada pedido que se haya realizado en ese día. Posterior a esto el sistema mostrará un mensaje diciendo que la operación realizada ha terminado.

### Pseudocódigo 
- Estado inicial

Lo que desea hacer (str):  agregar pedido (1), terminar registro (2)

La información del pedido: nombre (str), cantidad (int), sección (str), cantidad producida (int) y cantidad de personas (int).

- Proceso

Guardar información en variables (int)

Calcular las predicciones (float/int): promedio (float), tiempo restante (float), cantidad faltante (int)

Calcular rendimiento promedio (float)

Ocupar información de la sección (int)

- Estado final

Tiempo estimado de terminación (float)

Cantidad de piezas restantes (int)

Estado actual del pedido (descripción str y listas)

Cantidad de piezas de todo el día (int) 




### Fuentes

Tecnología para la industria. (2022, 30 junio). 10 maneras en las que el monitoreo en tiempo real de la fabricación mejora la precisión y la calidad. Recuperado 18 de agosto de 2022, de https://tecnologiaparalaindustria.com/10-maneras-en-las-que-el-monitoreo-en-tiempo-real-de-la-fabricacion-mejora-la-precision-y-la-calidad/

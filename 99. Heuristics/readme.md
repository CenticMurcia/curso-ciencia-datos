
<h1 align="center">Heurísticos</h1> 


## Registro de horario

#### Descripción del problema

Se dispone de las fichadas (momentos de entrada o salida) de los empleados de una empresa, y en base a esas fichadas se calcula el tiempo trabajado. Existen 3 turnos:

- El empleado A tiene un horario de **mañana y tarde** en el que ficha habitualmente a las 8:00, a las 14:00, a las 15:00 y luego a las 17:00. También puede fichar o no entre las 11:00 y las 12:00 para hacer un almuerzo. 
- El empleado B tiene un horario **de mañana**, ficha a las 8:00 y a las 15:00, con una posible pausa de almuerto que suele hacer entre las 10:00 y las 11:00. 
- El empleado C trabaja **de noche**, ficha a las 22:00 y sale a las 5:00 del día siguiente, sin hacer pausas para almuerzo. 
- Existe la figura del trabajador **libre** para el que no se definen horas para las fichadas. 

A lo largo de la jornada las personas tienden a **olvidar** fichar uno o más de sus marcajes y al hacerlo el cálculo ya no puede realizarse obligándose a que haya una persona en el dpto de Administración revisando los marcajes para completarlos de forma manual, una tarea que consume mucho tiempo. 


#### 1. Preprocesado y limpieza

Puede ocurrir que un trabajador fiche varias veces seguidas en lugar de una, para asesorarse de que ha fichado. Psible slución:

- Detectar aquellos fichajes que tienen menos de 1 minuto de duración y poner solo el primero o la media.

#### Heuristico

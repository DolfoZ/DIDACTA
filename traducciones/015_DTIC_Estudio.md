# DTIC_Estudio

AD-A147 500 
MANUAL DEL PROGRAMADOR DEL PROGRAMA DE COMPOSICIÓN ELECTRÓNICA 
1/2
(U) CENTRO DE INVESTIGACIÓN Y DESARROLLO DE ARMAMENTO DEL EJÉRCITO
PROVINCIA DE ABERDEEN.. 
JH WHITESIDE ET AL. AGO 84
SIN CLASIFICAR ARBRL-MR-93379 SBI-AD-F388 488 
F/G 14/5 
Países Bajos
EhEEEEEEmhmhhhI
EEE/hlhE/hhEEE
EhIIIhIhhhEIhE
iiEEllllEEEEEE
llEEllEEEEEEEE
EEEllllEEEEEEE


L3.
.-
L 3 
16 
señor
'. 
-111111 
l.
TABLA DE PRUEBA DE RESOLUCIÓN DE MICROCOPIA
~ 
OFICINA NACIONAL DE NORMAS IAEF A
.1* 
-


yo 
regañar 
li 
norte 
n. 
.
--
n.•. 
, 
II-
J. 
.
.
.• 
oh 
oh 
.,. 
,,
ANUNCIO
Lfl
INFORME DE MEMORIA ARBRL-MR-03379
EL PROGRAMA DE COMPOSICIÓN ELECTRÓNICA
MANUAL DEL PROGRAMADOR
John H. Whiteside
Carla G. Messina
agosto de 1984
S 
Estados Unidos 
EJÉRCITO 
ARMAMENTO 
INVESTIGACIÓN 
Y 
DESARROLLO 
CENTRO
INVESTIGACIÓN BALÍSTICA 
LABORATORIO
ABERDEEN 
CAMPO DE PRUEBAS, MARYLAND
Aprobado para su divulgación pública; distribución ilimitada. 
~ 
1
tov j5§4~
9.-
84 10 
31 .040


Destruya este informe cuando ya no sea necesario.
No lo devuelva al autor.
Se pueden obtener copias adicionales de este informe.
del Servicio Nacional de Información Técnica,
Departamento de Comercio de Estados Unidos, Springfield, Virginia
22161.
-yo
6
Las conclusiones de este informe no deben interpretarse como una información oficial.
Puesto del Departamento del Ejército, a menos que así lo designen otros
documentos autorizados.
El uso de nombres comerciales o nombres de fabricantes en este informe.
no constituye respaldo de ningún producto comercial.
¿S~? 
.
" 
" "- 0.. 
Yo°- 
*%j 
'" 
"1--* 
*.*-* 
o* 
.o* 
yo 
-
yo 
-


-SIN CLASIFICAR
.. " 
CLASIFICACIÓN DE SEGURIDAD DE ESTA PÁGINA (Cuando se ingresan los datos)
PÁGINA DE DOCUMENTACIÓN DEL INFORME 
LEER INSTRUCCIONES
R 
R 
ANTES 
COMPLETANDO FORMULARIO
yo. 
NÚMERO DE INFORME 
2. ADHESIÓN DEL GOBIERNO NO. 
3. 
NÚMERO DE CATÁLOGO DEL DESTINATARIO
.
INFORME DE MEMORIA ARBRL-MR-03379 
.... .
,
4. TÍTULO (y Subtítulo) 
5. TIPO DE INFORME Y PERIODO CUBIERTO
EL PROGRAMA DE COMPOSICIÓN ELECTRÓNICA 
finales
MANUAL DEL PROGRAMADOR
6. ORG. REALIZADORA. NÚMERO DE INFORME
7. 
AUTOR(o) 
8. 
NÚMERO DE CONTRATO O SUBVENCIÓN(&)
John H. Whiteside
Carla G. Mesina *
9. 
NOMBRE Y DIRECCIÓN DE LA ORGANIZACIÓN REALIZADORA 
10. 
ELEMENTO DEL PROGRAMA. PROYECTO, TAREA
Laboratorio de Investigación Balística del Ejército de EE. UU. 
NÚMEROS DE ÁREA Y UNIDAD DE TRABAJO
ATENCIÓN: DRXBR-LFD
Campo de pruebas de Aberdeen, Maryland 21005-5066
yo. 
NOMBRE Y DIRECCIÓN DE LA OFICINA CONTROLADORA 
12. FECHA DEL INFORME
Laboratorio de Investigación Balística del Ejército de EE. UU. 
agosto de 1984
ATENCIÓN: 
DRXBR-OD-ST 
13. NÚMERO DE PÁGINAS
Campo de pruebas de Aberdeen, Maryland 21005-5066 
128
14. NOMBRE Y DIRECCIÓN DE LA AGENCIA DE MONITOREO (si es diferente de la oficina de Controllind) 
ES. CLASE DE SEGURIDAD. (del informe)
SIN CLASIFICAR
ISa. DESclasificación/degradación
HORARIO
16. 
DECLARACIÓN DE DISTRIBUCIÓN (del Repc-t)
Aprobado para su lanzamiento público, distribución ilimitada.
17. 
DECLARACIÓN DE DISTRIBUCIÓN (del abetracto ingleteado en el Bloque 20, diferente al Informe)
ES. NOTAS COMPLEMENTARIAS
Este informe reemplaza al IMR-755, de octubre de 1982.
*Oficina Nacional de Normas
19. 
PALABRAS CLAVE (Continuar en el lado reverenciado si es necesario e identificar por número de bloque)
Mesas de tiro de artillería
Composición tipográfica electrónica
Máquina de fotocomposición
20. ASIISTNACr (Conihue -
pevin ad Iffneeeaamy e identificar por número de bloque) (un 
jb
Un nuevo método de procesamiento de datos para crear masters de impresión (imágenes a partir de las cuales
Se fabrican planchas de impresión) para mesas de tiro de artillería. 
el
El nuevo sistema utiliza composición tipográfica electrónica, derivada de la Oficina Nacional de
Sistema tipográfico de estándares, para preparar datos para una máquina de fotocomposición.
Este es un manual del programador con información sobre cómo funciona el programa, cómo
modificarlo para producir mesas de tiro de artillería, y la estructura del Typo-
Sistema gráfico del que se deriva.
FOOM 
ONU
D yo 
JA 
173 
EDICIÓN DEL I NOV S ES OMOLETE 
SIN CLASIFICAR
CLASIFICACIÓN DE SEGURIDAD DE ESTA PÁGINA (Cuando se ingresa Punto*)
Yo.'., 
-
-
.w 
,\ 
.,. 
.. 
., 
w-.,.-.,, 
: 
-. 
.
.
.
.
.
-. 
.
.
.
.
.
.
.
.
.
.. 
.
.
..

TABLA DE CONTENIDO
PÁGINA
LISTA DE ILUSTRACIONES ...... ... 
........................ 
5
LISTA DE TABLAS ..... ..... 
......................... 
7
yo. 
ESQUEMA DEL PROGRAMA DE COMPOSICIÓN ELECTRÓNICA
A. Antecedentes........ 
......................... 
9
B. Esquema del flujo del programa de composición tipográfica... 
........... 
9
II. 
DESCRIPCIÓN DETALLADA DEL PROCESAMIENTO DE ENTRADAS
A. Objetivos del procesamiento de insumos... 
................. 
9
B. Cómo se logran los objetivos ................. 
....
10
III. 
DATOS INTERMEDIOS Y FORMAS DE CONTROL
A. Formularios de datos intermedios... 
................... ...
10
B. Procesamiento de comandos de composición tipográfica... 
............. ... 11
IV. DESCRIPCIÓN DETALLADA DEL PROCESAMIENTO DE SALIDA
A. Lectura del archivo DIC ........... 
............... 
....
12
B. Emisión de comandos de la máquina de fotocomposición... 
...
12
V. FORMAS DE SALIDA Y CÓMO SE MODIFICAN
A. La Tarjeta de Datos en SETHELVTIMES.... 
................ ...
12
B. Las Tarjetas de Datos en BLANCOTOTAL, BLANCONEGRO, BLANCORED....... 
13
C. Tipo de fuentes utilizadas en la salida de Videocomp.... 
........... 
13
D. Cómo incluir caracteres o fuentes alternativos... 
... 
13
E. Cómo interpretar la salida de VIDWRT ................. 
...
15
F. La cinta de salida... 
........................ ...
15
VI. 
ARCHIVOS NECESARIOS PARA EJECUTAR EL PROGRAMA DE COMPOSICIÓN..... 
........... 
16
VII. 
CÓMO UTILIZAR COMANDOS DE TIPOGRAFÍA PARA CREAR LO QUE QUIERES
A. El dibujo lineal y sus dificultades... 
....
16
B. Sombreado... 
.. 
......................... 
... 
16
C. Tamaño del punto de cambio... 
.. 
.................... 
17
D. Cambiar la posición del cursor..... 
................. ...
17
3


TABLA DE CONTENIDO (Continuación)
PÁGINA
ADENDAS
A. Selección de tinta para números negativos legibles con luz segura ..... ... 
18
B. Una breve historia del programa de composición tipográfica... 
........... 
18
AGRADECIMIENTOS....... .. 
............................ ...
20
REFERENCIAS ....... ... .... 
... .... 
... .... 
... 
109
APÉNDICE A ........ 
... .. 
................................. .111
Entrada de teclado de entrada tipográfica
LISTA DE DISTRIBUCIÓN .. .. .. .... ... ... .... 
.... .....
127
14TIS -GRA&I
DTIC TABA&°
,Sin anunciar 
3
Justificación
* 
Por
Distribución/
CÓDIGOS DE DISPONIBILIDAD
aprovechar 
y/o
dist. 
Especial
v. 
yo
LG
'0
>4
°d~
'.°
,.g* 
.
~~." pag. 
*~~*~.*'*(.*

LISTA DE ILUSTRACIONES
FIGURA 
PÁGINA
1 
SISTEMA MODERNIZADO PARA LA PRODUCCIÓN DE MASTERS DE IMPRESIÓN ............ 
... 21
2 
OUYLINE DEL PROGRAMA COMBINADO DE EDICIÓN Y MANUSCRITO ....... 
22
"-." 
3 
DIAGRAMA DE FLUJO DEL PROGRAMA DE COMPOSICIÓN ELECTRÓNICA.... 
......... 
23
" .4 
DIAGRAMA DE FLUJO DETALLADO DE COMPOSICIÓN ELECTRÓNICA PARA
CODIFICACIÓN DIC..... 
... .... 
... .... 
... ..... 
24
5 
ESTRUCTURA Y DEFINICIÓN DEL CÓDIGO DE IMAGEN DEL DOCUMENTO ......... .. 25
6 
EL CÓDIGO ASCII..... ... 
........................ ... 26
7 
CONVERSIÓN DE DATOS DE TRANSMISIÓN DE TRABAJOS A CÓDIGO DE IMAGEN DEL DOCUMENTO... 
...... 
27
8 
DIAGRAMA DE FLUJO DETALLADO DE COMPOSICIÓN ELECTRÓNICA PARA
LECTURA DEL DIC ......... ... .... 
... .... 
.... 
28
9 
FUENTE GPO TIMES ITALIC ...... 
........................ ... 29
10 
OFERTAS ESPECIALES EN ITÁLICA DE GPO TIMES..... 
.................... ...
30
11 
FUENTE ROMANA GPO HELVETICA 
.
..... ........... .
31
12 
OFERTAS GPO HELVETICA ROMANA..... ....... ...... 
32
13 
PANTALLA UNIVERSAL GPO ...... ... .... 
... .... 
.. 
33
14 
TARJETAS DEL EJÉRCITO CON TABLA DE DATOS DE ENTRADA DE MUESTRA. . . . . . . . . . . .
.
34
15 
MUESTRA DE SALIDA DE TARJETAS DEL EJÉRCITO..... 
................... ... 35
16 
MUESTRA DE SALIDA VIDWRT..... 
................... 
.... 
39
17 
CORRECCIONES DE DIBUJO DE LÍNEA PARA EL ANCHO DE LÍNEA ................. 
...
40
18 
DIAGRAMA DE ESPACIADO DE CARACTERES... 
................... ...
41
19 
MÁSCARA DE MEDICIÓN DE POSICIÓN DE CARÁCTER ...... 
............... 
42
e-6 
20 
MODIFICACIONES EN LA ÉPOCA ROMANA, BODONI Y GÓTICA ........... 
...
43
v%.0 
21 
UNA PÁGINA DE MUESTRA DE LA PUBLICACIÓN ESPECIAL 480-3 DE NBS .......... V
22 
EJECUTAR FORMAS DE TRANSMISIÓN UTILIZADOS PARA PROCESAR UN ARCHIVO ASCII CON
GPSDC PARA TIPOGRAFÍA ...... 
........................ ...
45
23 
MUESTRAS DE LISTADOS DE PAÍSES DESDE UN LUGAR INTERNACIONAL
TABLA DE NOMBRES..... ... .. 
......................... 
46
5


LISTA DE ILUSTRACIONES (Continuación)
FIGURA 
PÁGINA
24 
EL APORTE PARA LA SECCIÓN VIETNAM DE LA INTERNACIONAL
TABLA DE NOMBRES DEL LUGAR. ...... ... .... 
... .... 
.... 
48
25 
USOS DE MUESTRA DEL INTERNO DE F80, F83 Y F86
COMANDOS DE COMPOSICIÓN ......... 
......................... 
49
26 
ENTRADAS PARA LOS USOS DE MUESTRA DE F80, F83 Y F86
FIGURA DE COMANDOS DE COMPOSICIÓN INTERNA ................. 
... 50
27 
REGLAS SOBRE REGLAS Y TAMAÑOS DE PUNTOS..... 
................. ... 52
28 
EXTRACTOS DEL MANUAL DE ESTILO GPO DE ENERO DE 1983.... 
......... 
53
29 
ENTRADAS UTILIZADAS PARA CREAR EXTRACTOS DE ENERO DE 1983
MANUAL DE ESTILO GPO ....... 
......................... ...
57
30. 
EJEMPLO DE TABLA TOTAL ....... .. 
......................... 
63
31. 
EJEMPLO DE MESA NEGRA ....... .. 
......................... 
64
32. 
EJEMPLO DE MESA ROJA ....... 
........................ ... 65
F6

LISTA DE TABLAS
TABLA NO. 
PÁGINA
1 
COMANDOS DE CONTROL DE FUENTES ....... ... 
................. 66
2 
CARACTERES "NEGATIVOS" QUE NO ESTÁN EN CURSIVA 
........
67
3 
EDICIÓN DE TRANSFORMACIONES EN CARLA*BATCHRUNS.ASCGPSARMY ..... ... 
68
-
4 
TABLA DE CARACTERES DEL SISTEMA GPSDC ....... .... 
....
70
5 
COMANDOS DE DIBUJO DE LINEAS Y SOMBRA ......... ... .....
79
6 
SECUENCIAS DE ESCAPE ACSII Y GPSDC .. .. ... . ... ......
80
7 
PALABRAS DE COMANDO DEL FLUJO DE TRABAJO Y SU SIGNIFICADO .. .......... ... 81
8 
SECUENCIAS DE COMANDOS DE FLUJO DE TRABAJO UTILIZADAS POR EL
PROGRAMA DE COMPOSICIÓN ....... 
................................. 85
9 
LA ESTRUCTURA DEL PGLN..... 
.................... 
....
87
10 
MATRIZ DE PARÁMETROS DE LÍNEA DE CÓDIGO DE IMAGEN DEL DOCUMENTO (ISTATE). ......
89
11 
CÓDIGOS GPSDC ESPECIALES PARA TIPOGRAFÍA ................. 
... 
93
12 
LA TARJETA DE DATOS DSDG*VIDBLOCK.SETHELVTIMES ............. 
.... 
94
wz 
13 
LISTADO DE CARLA*BATCHRUNS.CUTMARK ..... 
........... ... 95
14 
EL CÓDIGO DE COMANDO DEL VIDEOCOMP 500....... 
................ 
96
15 
UNIDADES DE MEDIDA TIPOGRAFÍA Y VIDEOCOMP
ESPECIFICACIONES DE LA PÁGINA.... 
.... 
............... ... 
99
16 
INTERPRETACION DE LA TABLA DE DATOS DE ENTRADA DE TARJETAS DEL EJÉRCITO.... 
......... 
100
17 
CAMBIOS REQUERIDOS EN LA SALIDA DE TARJETAS DEL EJÉRCITO..... 
............. 
101
18 
LA TABLA DE DATOS DSDG*VIDBLOCK.HELVTIMES... 
............ 
... 102
19 
ARCHIVOS NECESARIOS PARA EJECUTAR EL PROGRAMA DE COMPOSICIÓN.... 
.......... 
105
• 
20 
COMANDOS PARA CAMBIAR EL TAMAÑO DEL PUNTO Y REPOSICIÓN DEL CURSOR ......... 
106
7
r"-yo


I. ESQUEMA DEL PROGRAMA DE COMPOSICIÓN ELECTRÓNICA
A. Antecedentes
La composición tipográfica electrónica es un método automatizado para hacer lo que usaban las imprentas.
hacer a mano; seleccionar el tamaño de letra adecuado de un tipo determinado (tipo
fuente) y colocar los caracteres adecuados en las posiciones correctas para recrearlos en
imprimir un manuscrito escrito. Fue adoptado como parte de un esfuerzo de modernización.
Diseñado para minimizar la cantidad de trabajo manual requerido para la mesa de cocción.
producción. El Programa de Composición Tipográfica Electrónica es el resultado de un esfuerzo
comenzó en 1977 a modernizar la forma en que se producían las mesas de tiro de artillería.
El actual Programa de Composición Tipográfica es una modificación de la Oficina Nacional de
Sistema tipográfico de estándares.
B. Esquema del flujo del programa de composición tipográfica
El flujo de datos básico se ilustra en la Figura 1. La edición combinada y
El Programa de Manuscritos y el Programa de Composición Tipográfica trabajan juntos para producir el
Resultado final: una cinta a partir de la cual se pueden realizar masters impresos. 
Los maestros de la imprenta,
Las copias maestras a partir de las cuales se fabrican las planchas de impresión se realizan en fotocomposición.
máquinas de impresión ubicadas en la Imprenta del Gobierno.
El Programa Combinado de Edición y Manuscrito es responsable de poner
datos de la tabla final en el formato adecuado con la página y columna adecuadas
títulos (Figura 2). 
Se agregan comandos para dibujar líneas y sombrear columnas de datos.
haciendo referencia a un "paquete de líneas" que contiene comandos de línea maestra y sombra.
Consulte el artículo del Programa de manuscritos combinados para obtener más detalles. La línea y la sombra.
Los comandos se dirigen al programa de composición tipográfica que actúa sobre ellos. el
La secuencia de eventos se muestra en la Figura 3.
II. DESCRIPCIÓN DETALLADA DEL PROCESAMIENTO DE ENTRADAS
A. Objetivos del procesamiento de insumos
Los objetivos del procesamiento de entrada son tomar la salida del
Programa combinado de edición y manuscrito, conviértalo a un formato utilizable en
La computadora host en particular (en este caso, un UnivacR 1100/60 o un VAXR
11/780), buscar números negativos en los datos, insertar comandos de composición
para lidiar con ellos y, finalmente, convertir los comandos de composición tipográfica del Manuscrito
Programe en la forma adecuada para el Programa de composición tipográfica. Este procesamiento es
se muestra en la mitad superior de la Figura 4.
Runivac es una marca registrada de Sperry Rand Corporation
RVAX es una marca comercial de Digital Equipment Corporation
9

B. Cómo se logran los objetivos
(1) Los datos de entrada se introducen en una cinta magnética escrita a 1600 BPi,
114 caracteres por línea, una línea por registro en formato ASCII.
(2) La información de la cinta luego pasa a través de un programa especial,
CARLA*BATCHRUNS.ASCIITOSDF. El programa toma los datos de la cinta y los convierte.
en Univac SDF (formato de datos científicos). 
Sin este programa, el
Univac intentaría asignar la entrada ASCII al formato de datos de campo. Desde ASCII
tiene 96 caracteres (mayúsculas y minúsculas) y Field Data tiene 64, la necesidad de
La conversión es sencilla. El programa fue escrito por Joseph Yancone de Edge-
madera MISSD.
(3) Los datos de entrada, ahora en almacenamiento masivo, se buscan en busca de números negativos.
miembros de CARLA*BATCHRUNS.CHARED. Este programa, escrito por Wayne Bushell de
el Edgewood MISSD, toma los números negativos que encuentra e inserta tipo-
configurar comandos para poner el número negativo en cursiva. Estos comandos se muestran
en la Tabla 1. Sin embargo, ciertos casos deben excluirse de este proceso. Estos
se muestran en la Tabla 2.
(4) El procesamiento final de los datos de entrada se realiza llamando al Univac
editor para convertir comandos y símbolos publicados por el programa Manuscript en
los reconocidos por el Programa de Composición Tipográfica Electrónica. Esto se hace como parte
de CARLA*BATCHRUNS.ASCGPSARMY. Se muestran las transformaciones que se producen.
en la Tabla 3.
III. 
DATOS INTERMEDIOS Y FORMAS DE CONTROL
norte 
A. Formularios de datos intermedios
El objetivo de la primera mitad del proceso de composición tipográfica, como se muestra en
La Figura 4, es transformar un flujo de datos de entrada en un código maestro, el
Código de documento científico de propósito general (GPSDC), que contiene todos los tipos
configuración de información en forma comprimida. 
El origen y estructura de este código.
se analizan extensamente en la Referencia 1. La estructura se muestra en la Figura 5.
Básicamente es un código de 16 bits que contiene un conjunto de caracteres muy ampliado.
sobre el juego de caracteres ASCII (Figura 6). Se muestra una lista del código GPSDC.
en la Tabla 4. Un solo cuadro GPSDC puede contener casi toda la información
necesario para componer un carácter determinado, incluida la fuente, la representación (normal,
cursiva, negrita, etc.) y posición vertical en una línea (superíndice, línea principal,
subíndice). Una línea completa de caracteres de espacio se puede contraer en una sola
marco poniendo 250 en LOFRM y el número de espacios en HIFRM, ahorrando así
considerable espacio de almacenamiento. La conversión a GPSDC se realiza en dos pasos
para datos.
1. Blanton C. Duncan, "Representación completa en texto claro de datos científicos
Documentos en formato legible por máquina", Oficina Nacional de Normas
Nota técnica 820, Departamento de Comercio de EE. UU., febrero 
1974.
10
, , "7 ". 
r~r 
_, "-
' , 
7 
-".~ 
*-7 
'-,' 
-.- ,.-.- -
-_-'
• ".-Q ,-.- ---.-- -- • -•- 
.
.
.

mi. 
,. 
-
.. 
.... 
7 
.
-
.
.
, 
-
,
(1) Los datos de entrada se codifican en formato GPSDC mediante referencia a un diccionario GPSDC.
nario en GPSDC*DIC8S.ASCIIN. Si es compuesto (combinaciones de caracteres) o
Se trata de caracteres especiales, los diccionarios adicionales GPSDC*DICX8S.
Se pueden utilizar ASCOMP y GPSDC*DICX8S.ASDIC. En este punto, el personaje es
representado en codificación PTDICT como un número de carácter GPSDC. Los espacios son incómodos.
presionado. La información de fuente y modificación se lleva por separado; consulte la imagen.
discusión en B. a continuación.
(2) Después de que la información de entrada esté en código GPSDC(PTDICT), la tipografía
La formación se obtiene de los datos de entrada y se coloca en un biframe GPSDC a lo largo
con el personaje mismo. Esto lo realiza GPSDC*DICX8S.DECDE. El resultado
es el carácter más la información tipográfica contenida en la imagen del documento
Código (DIC). 
La figura 5 muestra el resultado final.
B. Procesamiento de comandos de composición tipográfica
Los comandos de composición provienen de varias fuentes: comandos explícitos de
el flujo de datos de entrada, desde las "tarjetas" de configuración de parámetros en el programa de edición,
e información inferida de los datos de entrada.
(1) Los comandos explícitos como "dibujar una línea" o "cambiar fuente" comienzan con
una secuencia de escape: el carácter de escape ASCII más uno o más símbolos.
GPSDC*DICX8S.DECDE pasa estas secuencias a GPSDC*DICX8S.PFMESC para su directa
conversión a código DIC. Este código luego se devuelve a DECDE para su inclusión.
en el archivo DIC. Las tablas 1, 5 y 6 más el listado de la Figura 5 muestran los
Secuencias de capas utilizadas y su significado.
(2) Ejecutar datos de secuencia, es decir, datos tomados de la secuencia de trabajos en lugar de
Los datos de entrada son procesados por GPSDC*DICX8S.CARDS. La secuencia general es
se muestra en la Figura 7. Las posibles palabras de comando se muestran en la Tabla 7. Los dos
Los conjuntos de comandos de secuencia de trabajos utilizados por partes del Programa de composición tipográfica son
se muestra en la Tabla 8.
(3) Los parámetros que controlan la forma en que se manejan los datos de entrada provienen de
varias fuentes: 
valores predeterminados iniciales proporcionados por el programa, valores re-
resultantes de tarjetas de comando de flujo de trabajo y valores calculados o inferidos a partir de
la naturaleza de los datos de entrada. Parámetros que afectan la composición tipográfica de un
Toda la página, los "parámetros globales", se almacenan en una matriz unidimensional llamada
PGLN. Sus elementos se definen en la Tabla 9. Los parámetros que son específicos de
una línea de texto determinada se transporta en una matriz bidimensional llamada ISTATE.
Sus elementos se definen en la Tabla 10. En última instancia, todos los parámetros de composición tipográfica
se colocan en codificación DIC y se almacenan junto con el texto en el archivo DSDG*GPS-ARMY.
(4) Datos de control de composición tipográfica extraídos de una de las fuentes anteriores o
insertados mediante un cambio de programa se almacenan en GPSDC en un formato especial. Figura
5 muestra que la palabra GPSDC está dividida en dos secciones de 8 bits, LOFRM y HIFRM.
Los datos de control se almacenan colocando valores especiales en estas dos secciones. mesa
11 muestra varias de estas combinaciones.
11

IV. DESCRIPCIÓN DETALLADA DEL PROCESAMIENTO DE SALIDA
A. Lectura del archivo DIC
El archivo DIC, DSDG*GPS-ARMY, lo lee DSDG*VIDBLOCK.VID500MAIN como se muestra
en la Figura 8. Este programa también acepta la información del encabezado que será
colocar en la parte superior de cada página de Videocomp desde la tarjeta de datos en CARLA*BATCHRUNS.
" 
IBLANCOTOTAL, BLANCONEGRO o BLANCOROJO. El archivo DIC se lee tres veces, una vez
por cada una de las tres secuencias de trabajos anteriores para producir tres archivos Videocomp:
uno con todos los caracteres, uno solo con caracteres negros y otro con rojos
Solo caracteres (negativos). Se procesan el dibujo lineal y las opciones de sombra.
por una modificación de VID500MAIN contenida en CARLA*BATCHRUNS.VIDDRAW. Líneas
y la sombra aparecen únicamente en los archivos TOTAL y NEGRO.
* 
B. Emisión de comandos de la máquina de fotocomposición
Después de leer la línea DIC, los caracteres se convierten al idioma
-
de la máquina de fotocomposición (una Videocomp 500), BIL 500, en varios pasos.
Primero, VID50I.AIN configura los comandos de página que le indican a la fotocomposición
máquina dónde comenzar la página, qué tamaño tendrá y dónde colocarla
tabulaciones. 
Se establece el tamaño en puntos de los caracteres y las fuentes de los caracteres.
6 
Los parámetros que deben incluirse también están establecidos. El tamaño en puntos y otros parámetros de la página son
establecido por la tarjeta de datos en DSDG*VIDBLOCK.SETHELVTIMES como se muestra en la Tabla 12.
Luego se colocan dos puntos grandes (GPSDC 132 - punto central grande) cerca de la parte superior y
parte inferior de la página en el margen extremo derecho. Estos actúan como guías para
el cortador de papel autotitic que corta el rollo de salida en hojas. Estos
Los puntos son generados por CARLA*BATCHRUNS.CUTMARK, enumerados en la Tabla 13, para el
secuencia de trabajos WHITERED y por una modificación de CARLA*BATCHRUNS.VIDDRAW para el
Flujos de trabajos WHITETOTAL y WHITEBLACK. Una vez realizado el trabajo preliminar,
VID500FLAIN se dedica a sacar personajes y mantener
seguimiento de la posición del cursor (impresión). Los códigos utilizados por la fotocom-
La posición de la máquina se enumera en la Tabla 14. 
Una vez generado el código se pone
en cinta mediante VIDPRT como muestra la Figura 8.
V. FORMAS DE SALIDA Y CÓMO SE MODIFICAN
A. La Tarjeta de Datos en SETHELVTI11ES
La información de esta tarjeta de datos dirige el proceso de composición tipográfica. el
El significado de cada campo de datos se proporciona en la Tabla 12. El tamaño en puntos y el tamaño de la ventaja
Los parámetros determinan el tamaño de los caracteres impresos y cuánto espacio
rodea a un personaje determinado. Los personajes del programa de composición tipográfica son
"establecer sólido", es decir, el tamaño del punto y el tamaño del cable son los mismos. Ocho puntos
Se utiliza el tipo. Esto proporciona una buena legibilidad y una densidad de información razonable.
sidad en una página. Los otros parámetros importantes son ANCHO DE CARÁCTER y
MOJOANCHO. Ambos anchos están en unidades Videocomp, una medida adimensional.
Las unidades no se pueden traducir a tamaño físico hasta que el tamaño nominal en puntos de
Se especifican los caracteres. Cuando se especifica MONOWIDTH, CHARACTER WIDTH
(el ancho de los números enteros) se ignora y todos los caracteres se comprimen o exprimen.
expandido según corresponda en el plano horizontal hasta el ancho especificado en unidades.
12
L-I 
'7 
' ' ' '. ,.' 
' '- .. 
" 
' .- -.-.. ..
"''-.' 
.'.' 
- '.'-, . ...'.

•. .
."- 
• 
-
.
.
-.-. 
-
.. 
-
.
.
.
"V.IK
La extensión vertical del personaje no se ve afectada. El ancho real del
caracteres se determina mediante la fórmula que se muestra en la Tabla 15. 
Así, una unidad de 112
Un personaje que normalmente tiene 8 puntos de ancho en realidad tendrá 4,48 puntos de ancho y 8
puntos altos cuando se establece en monoancho.
B. La Tarjeta de Datos en BLANCOTOTAL, BLANCONEGRO, BLANCORED
La tarjeta de datos en WHITETOTAL, WHITEBLACK y WHITERED es leída por
DSDG*VIDBLOCK.VID50OMAIN que llama a GPSDC*DICX8S.CARDS para realizar la lectura real.
introducción de los datos de campo en la tarjeta de datos. Estos datos se convierten a GPSDC y
procesado con el resto de los datos del archivo DIC. La tarjeta de datos contiene
la etiqueta colocada en la parte superior de cada página de Videocomp. La etiqueta puede ser fácilmente
cambiado cambiando la tarjeta de datos sin afectar el contenido del DIC
archivo. 
Normalmente, la parte de la fecha de la etiqueta es la única parte que se cambia.
C. Tipo de fuentes utilizadas en la salida de Videocomp
(1) Las fuentes tipográficas que se pueden utilizar en la máquina Videocomp 500 son
enumerados en el Manual de fuentes de la Oficina de Imprenta del Gobierno. 
Este manual está actualizado.
periódicamente a medida que se agregan nuevas fuentes. El grupo encargado del manual es
la División de Impresión Electrónica de la GPO. 
Fuentes utilizadas actualmente por el
Los programas de composición tipográfica son Times Italic, Times Italic Specials, Helvetica Roman,
_ 
Helvetica Roman Specials y Universal Display. Estos se ilustran en
Figuras 9 a 12. Al mirar el libro de fuentes, observe que cada
La fuente tiene un número de fuente y un número de subconjunto. Personajes individuales dentro del
Los subconjuntos se describen mediante un número hexadecimal de dos dígitos.
(2) Las fuentes tipográficas seleccionadas para imprimir las tablas de cocción se eligieron después
Probando varios para mejorar la legibilidad, particularmente bajo condiciones de iluminación adversas.
condiciones. Se eligieron fuentes separadas para números positivos y negativos para
minimizar la posibilidad de confundir uno con el otro. Plus especial y
Los signos menos fueron diseñados y colocados en el subconjunto 2 para las fuentes respectivas, como
los adecuados no estaban disponibles. Los guiones que se encuentran en el subconjunto cero de cada
la fuente no se puede utilizar como signo menos ya que se colocan a menos de la mitad
La altura de los personajes.
Se desarrolló un personaje extra. Esta era la característica de tono especial.
acter en la fuente Universal Display, subconjunto 1, hexadecimal 84. Esto se muestra en
Figura 13. 
Este carácter tiene un punto de ancho y la altura de un carácter.
Por lo tanto, se puede utilizar para sombrear una columna sombreando fracciones determinadas de una línea.
a la vez. Esto es mucho más rápido que intentar sacar un punto a la vez y
computacionalmente mucho más simple.
D. Cómo incluir caracteres o fuentes alternativos
(1) TARJETAS DEL EJÉRCITO
Toda la información de fuentes y caracteres utilizada por el programa de composición tipográfica para
que en realidad conduce una máquina de fotocomposición se almacena en forma comprimida en
DSDG*VIDBLOCK.HELVTIMES. Este conjunto de datos establece la conexión entre el
siete fuentes internas y las fuentes "reales" utilizadas por la máquina de fotocomposición.
.1
, 
13
.5.
, -
' 
,P 
" 
-'" 
-" 
,' 
' 
V 
w. .
"- 
, 
.' 
-, 
-,.. 
.'',"-.

.............. 
... 
.... 
............. 
............
7.- 
Ya se han observado ejemplos de estas fuentes en las Figuras 9 a 13. 
a
cambiar la fuente "real" a la que está conectada una fuente interna, estos datos deben
ser cambiado. El programa que genera HELVTIMES es CARLA*BATCHRUNS.AR1YCARDS.
La entrada a este programa es una tabla de datos que contiene toda la información necesaria.
información en un formato de texto claro. Un ejemplo de esta tabla se muestra en la Figura
14. 
La interpretación de los números se da en el eble 16.
(2) Los antecedentes de ARMYCARDS
""'"El 
El sistema tipográfico NBS y el programa de composición tipográfica electrónica
derivados de él utilizan una tabla de referencia de caracteres para ser flexibles. 
el
* 
Videocomp tiene muchos estilos de tipografía (fuentes) disponibles, por ejemplo, Times Roman,
Bodoni, Century, etc. cuyas descripciones de personajes residen en un disco. 
El lo-
La ubicación de caracteres dentro de una fuente determinada queda a discreción del grupo.
Poseer la máquina de fotocomposición. El GPO es consistente en carácter lo-
cación, pero las empresas privadas pueden no serlo. 
Al alterar la tabla HELVTIMES,
El programa de composición tipográfica se puede adaptar a cualquier juego de caracteres de Videocomp 500.
Se puede acceder a cada carácter de un Videocomp 500 mediante el uso de cuatro
números decimales o tres números hexadecimales. Desde la computadora en el
La Oficina Nacional de Estándares no opera en números decimales o hexadecimales.
* 
Se utilizan para identificar a cada personaje. Los cuatro números decimales necesarios para conducir
el Videocomp 500 son: 
fuente, subfuente, posición en la fuente y ancho del carácter.
actor.
El código GPSDC de 16 bits se puede reducir a tres números descriptivos:
el número de carácter (1 a 511); el nivel (0 a 3); y la modificación
(0 a 7). 
Los números de caracteres se enumeran en la Tabla 4. 
Nivel se refiere a ver-
posición tica en una línea: 
línea principal, subíndice, superíndice o subíndice debajo
superíndice anterior. La modificación se refiere a una composición tipográfica interna determinada.
Fuente del programa. Los tres números descriptivos del GPSDC deben entonces coincidir con
un conjunto específico de cuatro números Videocomp 500 para poder realizar cualquier composición tipográfica.
Por lo tanto, se necesitan siete números de entrada para describir un carácter tipográfico.
El código de GPSDC permite 511*4*8 caracteres individuales antes de Videocomp
500 suma sus cuatro números. El uso de conjuntos de datos multidimensionales
" 
han excedido la memoria disponible de la computadora y algo más, por lo que otro método
..
* 
Fue necesario desarrollar un sistema de almacenamiento de datos. Carla G. iessina y Robert C. Thompson
de NBS desarrolló el esquema de almacenamiento de datos utilizado en el Sistema Tipográfico NBS
y el Programa de Composición Tipográfica Electrónica. El diseño del conjunto de datos tiene que empaquetar
información necesaria en un área lo más pequeña posible y tener un método rápido de
recuperación. 
El conjunto de datos debe contener una manera rápida de determinar la presencia
o ausencia de un personaje y la ubicación del personaje, si está presente. el
La matriz de información está casi vacía y algunas de las posibles combinaciones de caracteres
* 
Las ciones pueden quedar vacías. Como ejemplo, DSDG*VIDBLOCK.VID5001AIN puede crear
caracteres monoancho, cursiva, negrita, superíndice y subíndice de caracteres existentes
caracteres para que estos caracteres en particular no tengan que almacenarse. 
no vacío
las entradas deben almacenarse.
ARMYCARDS llama al programa DSDG*VIDBLOCK.CARDIN para convertir la entrada
datos ilustrados en la Figura 14 en el conjunto de datos compacto requerido. 
CARDÍN
empaqueta los cinco números: modificación, fuente, subfuente, posición y carácter
ancho en una palabra de 36 bits. Hay una palabra para cada modificación. el
Las direcciones de las palabras de 36 bits dentro de esta tabla se almacenan en el número entero.
14
oh
.
.
.
.
.
.
.
.
.
.
.
.
.
.

MIRAR matriz (nivel+1, GPSDC NO.). 
Tres de los cuatro niveles se pueden poner a cero
si los superíndices y subíndices se crean a partir de los caracteres almacenados para el nivel
cero. Las direcciones de las ocho posibles modificaciones (fuentes internas GPSDC)
Las palabras almacenadas en ITAB() se determinan de la siguiente manera. si lo deseado
El carácter no está en el conjunto de datos actual, LOOK(1,GPSDC NO.) es negativo o
w 
cero. Todas las modificaciones de un carácter en el conjunto de datos se almacenan, para
de número de modificación creciente, entre LOOK (1,GPSDC NO.) y Absoluto
°. 
Valor [MIRAR(1, GPSDC NO. + 1)]-l.
(3) La salida de ARMYCARDS
La tabla tal como fue creada realmente por ARMYCARDS se ilustra en la Figura
15. Tenga en cuenta que, como resultado, la tabla es unidimensional y una tabla de ancho es
al final (PRINCIPAL, N, N). 
Para que funcione el programa de composición tipográfica, este resultado
debe ser alterado. Los cambios que se deben realizar se detallan en la Tabla 17.
Una vez realizados estos cambios, la tabla se parece a la Tabla 18.
.- 
E. Cómo interpretar la salida de VIDWRT
Las impresiones de WHITETOTAL, WHITEBLACK y WHITERED contienen un diagnóstico.
-
tabla nostic, generada por DSDG*VIDBLOCK.VIDWRT, que analiza el primero y el
últimos registros publicados por DSDG*VIDBLOCK.VIDPRT. Todos los registros pueden ser analizados.
estableciendo un nuevo valor para el interruptor de opción SETHELVTIMES. 
Consulte la Tabla 12 para
los detalles. En la Figura 16 se muestra una tabla de muestra. La impresión se basa en
* 
una cuadrícula de caracteres de fuente Videocomp 500 estándar. Las figuras 9 y 11 dan el hexágono.
códigos decimales para el alfabeto y los números estándar. Observe en la Tabla 14 que
* 
Los códigos de comando de Videocomp terminan en 7616, mientras que el carácter hexadecimal más bajo
El código es 80. Los caracteres están directamente encima del número hexadecimal que representa.
enviándolos. La zona y las rectas numéricas corresponden a 161 y 160, respectivamente.
activamente. El problema surge cuando un parámetro de comando es 8016 o mayor o cuando un
Se utiliza una fuente no estándar. VIDWRT mostrará un carácter cada vez que se muestre.
cuenta un número hexadecimal que corresponde a un carácter estándar, incluso
si un personaje no está previsto. Si se utiliza una fuente no estándar, VIDWRT
no mostrará un carácter no estándar pero lo reemplazará con un estándar
*. 
carácter con el mismo valor hexadecimal. Así, al escribir en Times Italic
, 
fuente 18, Subconjunto 0, un C616 representa una "F" pero en el Subconjunto 2 de la misma fuente,
C616 es un signo menos. Utilizando la tabla de comandos del Videocomp 500 y la configuración adecuada
tabla de fuentes, un archivo BIL 500 completo se puede descomponer y analizar cuando
*lemas 
surgir.
*'de. 
La cinta de salida
GPO Videocomp 500 requiere un conjunto estándar de parámetros de cinta de entrada.
El Programa de Composición Tipográfica saca una cinta con estos parámetros, que son:
9 pistas, 800 bits/pulgada, sin paridad, sin etiqueta de encabezado de cinta.
La escritura de la cinta está controlada por DSDG*VIDBLOCK.VIDPRT. El real
-. 
la escritura se realiza mediante GPSDC*DICX8S.NTRAN-28O/16OOPE.
15
* 
.
* 
* 
.. 
.
.' 
* 
.
.
-
* 
.
.
* 
-
.
-
.

VI. 
ARCHIVOS NECESARIOS PARA EJECUTAR EL PROGRAMA DE COMPOSICIÓN
Los archivos necesarios para que el programa de composición tipográfica funcione se enumeran en la tabla
19. El programa requiere algunas subrutinas de algunos archivos y la mayoría de los programas.
-
almacenados desde otros archivos.
VII. 
CÓMO UTILIZAR COMANDOS DE ENTRADA TIPOGRAFÍA PARA CREAR LO QUE QUIERES
A. El dibujo lineal y sus dificultades
La Tabla 5 contiene los comandos de dibujo lineal y sombreado. 
Para usar la línea
facilidad de dibujo, primero diseñe el formulario que desea crear en una hoja de papel.
Dibújalo a escala y decide si todas las líneas deben tener el mismo ancho. el uso
de múltiples anchos de línea permite llamar la atención sobre las partes principales
de la forma. Cada línea deseada debe estar etiquetada con sus coordenadas de origen,
ancho y largo. 
Ahora se deben comprobar las interacciones de las líneas. perpendicular
líneas que terminan en una intersección en el lado izquierdo del formulario, pase
entre sí sin terminar, o que terminan en una intersección en "T" pueden
ser ignorado. Rectas perpendiculares que terminan en una intersección a la derecha
El lado del formulario se verá desarticulado a menos que se corrija por los efectos de
espesor de línea. Este problema surge porque se traza una línea vertical desde
su origen se coordina hacia abajo, con su ancho yendo a la derecha del origen
Coordenada "Y". Una línea horizontal dibujada para terminar en esta coordenada
Forme una intersección a la que parece que le han quitado un mordisco. La solución
La opción es elevar el origen de la línea vertical en una cantidad igual a la
espesor de la línea horizontal. 
No olvides aumentar la longitud del
línea vertical por una cantidad correspondiente. La línea horizontal debe entonces ser
alargado por el espesor de la línea vertical. 
Cuanto más gruesas sean las líneas,
más importante se vuelve esta corrección. 
El proceso de corrección es ilustrativo.
tratado en la Figura 17.
B. Sombreado
El sombreado de las mesas de tiro de artillería se realiza utilizando una característica de sombra especial.
ter desarrollado para esta aplicación. Se muestra en la Figura 13 como 8416. 
esto
El carácter tiene una fila de puntos (16 unidades) de ancho y una línea de alto. en 8 puntos
tipo, esto equivale a .0064 puntos de ancho. El comando de sombreado hace que
carácter de sombra que se repetirá para el ancho de la columna, luego el cursor
se restablece al lado izquierdo de la columna, se elimina una línea y el
El proceso se repite hasta que la columna esté completamente sombreada. las coordenadas de origen
utilizados en el comando de sombra son los de la esquina superior izquierda de la parte superior
del área sombreada. El ancho debe ser el ancho de la columna más un carácter extra.
ancho del actor. Esto se hace porque es poco probable que un número entero de
Los caracteres de sombra encajarán en el ancho de la columna. Si el ancho del sombreado
Faltan uno o dos caracteres para el ancho de la columna, una línea blanca vertical.
aparece junto a la línea de separación de la columna de la derecha. Invadiendo la columna
un ancho menor que el ancho de las líneas verticales no produce efectos nocivos.
0Alternativo 
Se pueden utilizar caracteres de sombra, mostrados en la Figura 13, pero no
requieren cambios de programa en CARLA*BATCHRUNS.VIDDRAW.
9.,
16
6J

* 
C. Tamaño del punto de cambio
El tamaño en puntos se puede cambiar deliberadamente, es decir, para un documento completo,
o sobre la marcha, eso es sólo por el momento. Cuando se cambia sobre la marcha, sólo
los caracteres especificados cambian su tamaño en puntos.
Un cambio deliberado en el tamaño del punto se realiza cambiando el tamaño del punto y la ventaja.
parámetros de tamaño en la tarjeta de datos en DSDG*VIDBLOCK.SETHELVTIfIES. Esta tarjeta es
*mostrado 
en la Tabla 12. 
Las mesas de disparo están "fijadas", por lo que los tamaños de punta y plomo
son iguales. Durante el desarrollo del Programa de Composición Tipográfica, tipografía de 7 puntos.
Se intentó una ventaja de 8 puntos, pero 8 puntos "sólidos" parecían mejor, por lo que se adoptó.
-ted. 
Si los caracteres no son sólidos, asegúrese de utilizar el tamaño de mina, no
el tamaño del carácter, al calcular "carácter/línea" (ver Tabla 15). 
el
* 
El espaciado de los caracteres se ilustra en la Figura 18.
Cambiar el tamaño de los puntos sobre la marcha se utiliza para colocar números de líneas encontradas en artillería.
Tabla B de las mesas de cocción: Número de línea de estufa de cortesía. Una serie de pruebas
demostró que el tipo de 18 puntos coincidía mejor con la línea de cumplimiento dibujada a mano anterior
números. 
Los caracteres cuyo tamaño en puntos se cambia sobre la marcha se "establecen" igual
manera como los caracteres normales de una página. Por lo tanto, si los caracteres regulares están "establecidos
sólido... los caracteres en el tamaño de puntos modificado también se "establecerán sólidos".
La Tabla 20 muestra los comandos utilizados para modificar el tamaño de los puntos sobre la marcha. La sugerencia
". 
gestiones en 
Se debe seguir la parte "Estrategia" de esta tabla. En par-
En particular, los comandos de cambio de tamaño de punto y movimiento del cursor deben ser los últimos
elementos en una página. Intentar dibujar líneas o imprimir caracteres normales después
Se han utilizado estos comandos puede resultar en un desastre. Una vez que se abre una nueva página
iniciado, sin embargo, el programa de composición restablece el cursor y el
.- 
sus valores predeterminados.
Para evitar la necesidad de contar espacios a mano o medir caracteres
coordina con una regla, se hizo una máscara de superposición fotografiando un patrón
*me gusta 
el que se muestra en la Figura 19. 
Esto se ha reducido considerablemente desde el nivel normal.
tamaño incorrecto. Con la máscara colocada sobre una página de manuscrito, los caracteres de gran tamaño se ubican
Las conexiones y los orígenes de las líneas se pueden determinar rápidamente. Las medidas estan hechas
en términos de ventaja de 8 puntos, pero se puede convertir rápidamente a otros tamaños de puntos mediante
utilizando el cálculo del ratio en la Nota de Estrategia de la Tabla 20. Observa que el
La ubicación inicial de los caracteres de página en la Figura 19 es (16,5). 
Esto significa que
El primer carácter de la tabla está a 16 espacios de 8 puntos desde el borde izquierdo de la tabla.
página de videocomp y 5 líneas debajo de la parte superior de la página. Esto permite una "vinculación
margen" a la izquierda para una página impresa encuadernada y espacio en la parte superior para una etiqueta.
D. Cambiar la posición del cursor
Los comandos de cambio de posición del cursor se enumeran en la Tabla 20, junto con un
g. 
estrategia para su uso. La ubicación del cursor es la posición en un Videocomp.
página donde se escribirá un carácter si se le ordena. El programa de composición tipográfica
indexa automáticamente esta posición a medida que cada carácter y cada línea se
completado. La unidad básica que utiliza el Programa es un medio espacio vertical escrito
"fhu" para "formatear media unidad". Una serie de comandos de edición en CARLA*BATCHRUNS.
ASCGPSARMY convierte los comandos de movimiento vertical en lenguaje sencillo a "fhu".
17
C.%IA

El único lugar donde se usan estos comandos de movimiento para las mesas de disparo es en
Tabla B. Allí, la secuencia adecuada de eventos es imprimir primero todos los datos normales.
caracteres de tamaño de punto, luego haga las líneas de máscara de tabla, luego las más pesadas se reunieron
líneas de separación de números de línea y, finalmente, coloque los números de línea de 18 puntos.
APÉNDICE A: 
Selección de tinta para números negativos legibles con luz segura
Las mesas de cocción convencionales tienen sus números negativos impresos en una cereza.
.
tinta roja que es invisible bajo una luz roja de seguridad. 
La nueva tinta utilizada para los negativos
números positivos, D.O.D. Especificación de color estándar #SPC61121, luce rojizo pero
Tiene alta reflectividad en luz roja. Fue desarrollado por el Mapeo de Defensa.
Agencia de mapas topográficos. 
En caso de que el Ejército cambie a una caja fuerte azul
luz para derrotar a los dispositivos intensificadores de imagen, se podría usar la misma tinta desde
La eficiencia visual de esta tinta es mayor con luz azul que con luz roja. 
Ver referencia
ence 2 para obtener información más completa.
ADENDA B: 
Una breve historia de este programa
Este programa es una consecuencia de un requisito iniciado en 1977 para modernizar
la forma en que se produjeron las mesas de cocción. El actual Programa de Composición Tipográfica es un
modificación del Sistema Tipográfico de la Oficina Nacional de Normas. 
el
El sistema tipográfico fue desarrollado durante varios años por el Dr. David Garvin,
Dr. Blanton C. Duncan, Sra. Carla Messina, Sr. Robert Thompson y otros en
la Oficina Nacional de Normas (NBS). 
Fue desarrollado para componer documentos.
para la Oficina de Datos de Referencia Estándar. 
Documentación del Tipográfico
El sistema está contenido en las referencias 3 y 4. La Sra. Messina cooperó con el
Laboratorio de Investigación Balística (BRL) en la adopción del sistema para su uso en tipografía-
mesas de cocción. 
Las modificaciones implicaron una programación especial para crear
líneas y sombras, aceptar entradas en ciertos formatos y crear 3 archivos de salida,
los archivos Total, Negro y Rojo, descritos en la Sección 4.A., e ilustrados en
Figuras 30, 31 y 32. 
Fue necesario un largo período de pruebas antes de que se implementara la modificación.
Todas las ficaciones funcionaron correctamente. Parte de las pruebas implicó encontrar el mejor
fuentes y tamaño en puntos para usar con números positivos y negativos. Modificaciones
Se hicieron las fuentes cuando fue necesario al tener nuevos caracteres diseñados por
2. 
".'tazdard Printing Color Catalog'ze para,,aplicación, gráficos, m; 3 .i 
.
zdat 
y Re7ated Produts", Agencia de Cartografía de Defensa, Tpoj:' 
...
'7,
Washington, DC, julio de 1972.
3. 
Robert C. Thompson, "Propósito general .iceentif ii 
Doea,. Wi<. (oh,. 
entonces r'
,ianua7 " Oficina Nacional de Sanc2 dd, 
npub I.5i? d, Dc.,,?';,eP 9W I
4. 
Robert C. Thompson, " 
ZTener! 
F upoae 
7*_-'e 
(-.f' 
.?sí:,
lla;nuaZ, " Oficina Nacional de Stan.".K,'p~l.U 
~~
yo
.,, 
18
yo


7- 
'7 
.. 
7.
* 
Information International, el fabricante de máquinas de fotocomposición. Estos
Los caracteres incluyen el "corte", el "6" y el "9" en Helvética, el "+" y el "".
signos en Helvetica y Times Italic, y el nuevo carácter de color en Universal
Pantalla. El Sr. Robert Schwenk de la División de Impresión Electrónica del Gobierno
ment Printing Office (GPO) tenía los nuevos caracteres implementados en el GPO
*yo 
Videocomp 500 y ayudó con las exhaustivas pruebas que siguieron. En esto
punto, el proceso de composición tipográfica real fue automatizado y verificado, pero el
comandos de línea y sombra y comandos de tamaño de punto y movimiento del cursor de la Tabla B
* 
fueron agregados a mano. Sr. Joseph Hurff y Sra. Lilly Harrington de Firing
Tables Branch modificó el programa combinado de edición y manuscritos para que
generaría los comandos de línea y sombra automáticamente. A partir de esta fecha,
Los comandos de la Tabla B no se han incluido. Con este último paso, el proceso
Se completará la preparación del manuscrito (ahora master impreso). la automatizacion
del proceso ahorra de uno a cuatro meses-hombre por mesa, dependiendo del tamaño de la mesa.
* 
Por tanto, el tiempo y el dinero invertidos en el desarrollo deberían recuperarse en un plazo
varios años.
19

AGRADECIMIENTOS
Los autores agradecen la asistencia recibida del Sr. Robert Thompson.
y otros en la Oficina de Datos de Referencia Estándar, Oficina Nacional de
Estándares.
La asistencia proporcionada por el Sr. Steve Sandborn de Information International
es muy apreciado. 
Varias de las figuras y tablas se derivan de
información que proporcionó. Los autores le deben mucho al Sr. Robert Schwenk
y el Sr. Bud Collison de la Imprenta del Gobierno de Estados Unidos. Su aviso
Procesamiento de casos de prueba de composición tipográfica y crítica de los resultados iniciales.
permitió realizar correcciones oportunas del programa, acortando el desarrollo del programa.
período de ment considerablemente. 
Finalmente, los autores agradecen el apoyo brindado.
por sus supervisores, particularmente cuando las cosas parecían más sombrías, los plazos
se perdieron y la esperanza escaseaba.
02
!:yo~20
0-.


SISTEMA MODERNIZADO PARA LA PRODUCCIÓN DE MASTERS DE IMPRESIÓN
DATOS DE LA TABLA FINAL
ESTÁN MONTADOS
ENTRADA DE DATOS EN
EDICIÓN COMBINADA Y
PROGRAMA DE MANUSCRITO
DATOS EDITADOS CON
LÍNEA Y SOMBRA
COMANDOS PRODUCIDOS
t
DATOS EDITADOS
ENTRADO EN
COMPOSICIÓN ELECTRÓNICA
PROGRAMA
DATOS TIPOGRAFIADOS TRANSFERIDOS
POR CINTA AL GOBIERNO
IMPRENTA (GPO)
MAESTROS DE IMPRESIÓN PRODUCIDOS
POR GPO SOBRE FOTOCOMPOSICIÓN
MÁQUINA
PITMASTERS FOTOGRAFIADOS
FOTOS USLD PARA HACER PLATOS 
yo]
Figura 1
21


'.p.
777
ESQUEMA DEL PROGRAMA COMBINADO DE EDICIÓN Y MANUSCRITO
TRAYECTORIA Y
DATOS DE EFECTOS
PARA MESAS
DATOS ORGANIZADOS EN
FORMATO ADECUADO PARA
CADA TABLA - PÁGINA
* 
POR PÁGINA
ENCABEZADOS DE TABLA
AÑADIDO
LÍNEA Y SOMBRA 
PÁGINA ESTÁNDAR
COMANDOS AÑADIDOS PARA 
-- 
LÍNEA Y SOMBRA
CADA PÁGINA - NO ESTÁNDAR 
DIRECCIÓN DE MANDO
PÁGINAS ALOJADAS
jn 
DATOS DE LA PÁGINA FINAL
MONTADO Y PUESTO
* 
EN ARCHIVO
F-':
Figura 2
22


DIAGRAMA DE FLUJO DEL PROGRAMA DE COMPOSICIÓN ELECTRÓNICA
[."
DATOS DE PÁGINA DE
EDICIÓN COMBINADA
Y MANUSCRITO
• 
PROGRAMA
INFORMACIÓN ALFANUMÉRICA
Y COMANDOS DE LÍNEA Y SOMBRA
CONVERTIDO A PROPÓSITO GENERAL
CÓDIGO DE DOCUMENTO CIENTÍFICO (GPSDC)
DATOS Y COMANDOS TPST
COMPRIMIDO Y COLOCADO EN
CÓDIGO DE IMAGEN DEL DOCUMENTO (DIC)
CÓDIGO DIC LEÍDO PARA
TODOS LOS CARACTERES MÁS LÍNEA Y
COMANDOS DE SOMBRA, TRADUCIDOS
EN EL CÓDIGO BIL 500 Y PONER EN CINTA
CÓDIGO DIC LECTURA PARA CARACTERES NEGROS
MÁS COMANDOS DE LÍNEA Y SOMBRA, TRADUCIDOS
EN EL CÓDIGO BIL 500 Y PONER EN CINTA
CÓDIGO DIC LEÍDO PARA CARACTERES ROJOS
SOLAMENTE, TRADUCIDO A BIL 500 Ct'n1:
Y PONER EN CINTA
Figura 3
23


DIAGRAMA DE FLUJO DETALLADO DE COMPOSICIÓN ELECTRÓNICA PARA LA CODIFICACIÓN OIC
DATOS DE ENTRADA
EN ASCII
PERSONAJES
CEI SOF 
EDTE 
ORCOET
VARILLA DE PRUEBA 
acosador
RORM: THCANUSCRPTROGR.AM ITO
NROPERSADER 
TIPOGRAFÍA 
INGOJTO 
HAATR
PRGACARLA*BATCHRUNS.CARE
LEER 
SDFE 
ARCHIVO 
DICTIOVARIO
PROGRAMA:~ 
DELANTERO 
DSDGMANARCRITSDFOGNA1 
ROGA:PDDC8SAIN
0 ~ ~ 
~~ 
POE 
CONTROLAR 
LECTURA REPETIDAERESPEILCNRLDT
DE LIN 
EN ARCHIVO SF Ci 
DE TARJETAS RUNSTREAM
PRRAMTR 
GSDCDEX TI 
PROGRAMA:I GPSDCC8 
ANUNCIO
READIREA 
Todo SIED 
FIONE EN
PROGRAMA:Yo 
[SGCRSSFN 
PROGRAMA: 
DSDG*DCRDS.SFREA
PROGRAMA: 
GPSDC*DICX8S.DECDE
PONER LÍNEA Y SOMBRAS COtW4ANDS
EN DIC
PON UT IC INEPROGRAMA: 
GPSDC*D1CX8S. PFMESC
~ 
PROGRAMA: 
DSDG*GOGPO.STRIPLINEOT]
Figura 4
24


'4 
qw 
V'X- 
-
q 
w
la 
_
~10 
= 
+ 
+
Yo-- 
LA- 
U- 
LL.
LO 
z 
mi) 
ka 
V)
cnI- 
l 
-
¿Mira?) 
laj 
0.c- 
yo-
LLI 
LJ 
0 
m 
=U! 
C=A 
c 
~L"U
1- 
1- 
L-9 
..
o. 
co) 
U)
* 
c 
-
CL 
c 
~ 
l
cc 
uL'O tz 
l= 
mi) 
mi) 
:D
C.) 
) 
lai
oA -c 
colia
mi 
l) 
2: 
1)
%D. 
CV 
(Un 
>-CA)
-. 1
LL.
m 
yo 
-
w 
0o
0
U-I- 
l 
la 
-
A.
CDO 
c. 
tu 
CD 
-
-
w- 
--
j 
0 
CD
0 
c 
California
z 
la 
ln 
C-)
Zo 
CDJ 
V) 
LA) CE
liii 
tu 
C-~ 
l
*Un 
cx 
LL.A-~ 
-
0
-4 
ClO' 
t 
ln 
CD 
0. 
co-Irc 
% 
i1
4a 
a-4 0% 0%o 
.
c 
oh 
baño 
ml 
fl'. 
CIA 
= 
w
Los Ángeles 
0 
, 
00-4 
C%I M 
gt 
tú, 
%V 
t 
LU 
sua V)
g- 
4: 
c ~ 
tos 
c.N %Js 00~ 
c%' CO LJa
0) 
% 
0 
~ 
4 
4 
(% 
lj'.. 
%j 
=7 
c
cc
LA.0A. 
0
O0 
V-4 
la 
LI ~ 
Los Ángeles) 
Los Ángeles. 
L".
4 
U. ~ 
t 
L- 
-
AL 
10 
0~
interfaz de usuario yo 
-
yo -
LA-
CLu 
yo. 
t 
m 
yo 
%=s 
'CD 
C:)
% en peso 
LU 
l 
yo 
TA 
l 
l 
&
* 
A25
.. 
1. 
%U%a 
L% 
%L.%.% 
-

7 
v.
TABLA DE CÓDIGOS ASCII/TTY
r'i-MSB
HEXAGONAL 
0 
1 
2 
3 
4 
5 
6 
7
DÍGITO___________
36-yo 
mi 
pI 
0 
1 
1
LSB 
t 
-s 
1 
yo 
yo
HEXAGONAL 
S 
ALTOX&Y
CONTROLAR 
HIC INU 
BAJA X 
BAJA Y
""DIGITO 
03 
g 2 o 
ENTRADA GRÁFICA
.
NUL 
DLE 
SP 
a) 6 
pag 
yo
1 20 
'w 
40 
ISO
yo 
1? 
49 
916 
5 
4
1 
8001 
SOH 
DC1 
yo 
1 
un 
0 
un 
q
2 
1 
34 
6 
0 
6 
; 
141 
6 
4 
4
2 
mi 
0.
STX 
DC2 
2 
2 
b 
R 
segundo 
r
.
2 
2'2 
'2 
62 
40.' 
*:." 
!4 
'2
"yo-"ET 
1 
#28 
3 
1 11 
6 
eso
3 
ETX 
DC3 
# 
3 3 
03C 
S 
3c 
-
4 
x4 
tu 
S 
6lie64 
!
4 
0100 
EOT 
DC4 
$ 
4 
re 
t 
re 
t
4 
24 
44 
64 
404 
'4444.
1 
24 
% 
7 
3'3 
6 9 
4V 
4
5 
0II 
ENO 
NAK 
5 
mi 
Ud. 
9 
tu
5 
25 
1064 
0-. 
'4 
46
yo 
Ud. 
Entonces 
64 
7e 
16 
iluminado44
6 
61 
0 
ACK 
SINC 
& 
6 
f 
V 
f 
v
6 
26 
46 
6o, 
106 
4 
446 
10
7 
0ii 
bel 
ETB 
' 
7 
0G 
W. 
9 
w
4.• 
'4"6 
10" 
-
447 
161
6 
14 
un 
IR 
r9 
S 
2m 
4 pulgadas
8 
1 
0 
0 
1 licenciatura 
PUEDE 
( 
8 
h 
x 
h 
x
5,' 
2yo 
44 
57 
72 
661 
45 
454
9 
1 o 0 
1 
HT 
EM 
) 
9 
yo 
Y 
yo 
y
.1 
36 
42 
Entonces 
74 
91 
EN 
'n
un 
1010 
LF 
SUB 
.
: 
z 
z
112 
32 
':44 
52 
172
b 
01 
TV 
ESC 
+ 
; 
k 
norte 
yo 
{
-
3 
33 
5-3 
*'3 
443 
4'' 
43 
47'3
47 
26 
44 
40 
76 
51Z 
45 
46
c 
1FF 
FS 
< 
l
4 
34 
''4
13 
15 
5 
a4 I7 
?3 
en 
45
re 
1101 
CR 
GS 
-
-
m 
] 
m 
}
mi 
1110 
Entonces 
RS 
> 
norte 
un 
norte 
,
463441 
63 
norte, 
eso.4 
4
f 
111 
SL 
Estados Unidos 
yo 
? 
0 
0
Figura 6
2 mi


'Oh
CONVERSIÓN DE DATOS DE TRANSMISIÓN DE TRABAJOS A CÓDIGO DE IMAGEN DEL DOCUMENTO
LLAMANDO
PROGRAMA
REGRESAR DIC
PARA LLAMAR
re 
PROGRAMA
NO
GPSDC*DICX8S.TARJETAS 
es
LEER EN UN CAMPO DATOS 
HAY UN
IMAGEN DE TARJETA 
COMANDO
( 
¿SÍMBOLO?
SI
GPSDC*DICX8S.CONVRT 
GPSDC*DICX8S. PARCHK
CONVERTIR DATOS DE CAMPO 1- 
PARÁMETRO DECODIFICAR
IMAGEN DE TARJETA AL DIC 
CONFIGURACIÓN DE LA PALABRA DE COMANDO
Figura 7
27
*1S


un 
.
un
7.' 
* 
*un 
.%
'0j
w 
00
Los Ángeles 
-j 
co..
50 
c 
wLJ 
yo 
0 
0 
,,.
-C~~- 
9 
,t
yo 
en
z 
00
co
un# 
028


yo.yo
'13
0-4
E-4~ 
~ 
~ 
es decir
cnq
o co
-
TJ7x
0 
00 
w
yo 
_ 
_ 
_ 
_2_
[mafia-


.U 
-
-
.. 
.%J 
3- 
-
-
CC.
cqq
E-4
00
E--
C44 
control de calidad 
m 
ci
0 
0 
1
k 
30


0 
0 
-
-
ILT
CD§
0-
Y4 
00 
IY
E-_ 
-D7
cq eq 
Vm 
q 
yo
0q 
00 
q 
00
oh 
ecuación
31


-
.
0C
-
-- 
-
-p-
0
C~1 
4
0o0
~1 
Z3_


= 
* ..-.. 
.--
7717..7*.
0 
-
10
~ CV 
0
si--
VH-
mq 
mi
03 
m
......
tu.
N ~ ~ 
V 
q 
V 
t
nq 
norte 
nq 
nq 
m 
*
33


* 
*- 
-
.
," t-' 
"  
segundo 
•
,
TARJETAS DEL EJÉRCITO CON TABLA DE DATOS DE ENTRADA DE MUESTRA
@ELT,L CARLA*BATCHRUNS.ARMYCARDS
1. 
12 
@RUN,/R JHW,801A8/JXWHITESIDE,FTMOD,5,200/500
2. 
12 
@ELT,L CARLA*BATCHRUNS.ARMYCARDS
3. 
12 
@MSG,W POR FAVOR INTERPRETE LA SALIDA DE LA TARJETA PERFORADA DESDE MESSCD
4. 
12 
@ASG, UN DSDG*GOGPO.
5. 
12 
@AÑADIR DSDG*GOGPO.NBSASG
6. 
16 
@USE MAP$PF., MISD*FORLIB.
7. 
12 
@MAPA, EN V500
8. 
12 
MENTIRA DSDG*VIDBLOCK.,DSDG*TARJETAS.
9. 
12 
EN CARDIN, INDATA, HEXOUT
10. 
12 
@XQTV500
11. 
12 
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
12. 
12 
1 0 4 18 0 205 66
13. 
12 
4 0 4 18 0 246 100
14. 
12 
5 0 4 18 0 244 200
15. 
12 
6 0 4 18 0 144 150
16. 
12 
8 0 4 18 0 244 70
17. 
12 
9 0 4 18 0 242 70
18. 
12 
10 0 4 18 0 243 100
19. 
13 
11 0 4 18 2 197 100
20. 
12 
12 0 4 18 0 139 52
21. 
13 
13 0 4 18 2 198 100
-
22. 
12 
14 0 4 18 0 138 52
23. 
12 
15 0 4 18 0 225 100
24. 
13 
16 0 4 18 0 176 100
25. 
12 
17 0 4 18 0 177 100
26. 
12 
18 0 4 18 0 178 100
27. 
12 
19 0 4 18 0 179 100
28. 
12 
20 0 4 18 0 180 100
29. 
12 
21 0 4 18 0 181 100
.
30. 
12 
22 0 4 18 0 182 100
31. 
12 
23 0 4 18 0 183 100
32. 
12 
24 0 4 18 0 184 100
.
33. 
12 
25 0 4 18 0 185 100
34. 
12 
26 0 4 18 0 204 52
35. 
12 
27 0 4 18 0 140 52
36. 
12 
31 0 4 18 0 141 82
37. 
12 
33 0 4 18 0 193 136
38. 
12 
34 0 4 18 0 194 134
39. 
12 
35 0 4 18 0 195 146
40. 
12 
36 0 4 18 0 196 158
41. 
12 
37 0 4 18 0 197 142
42. 
12 
38 0 4 18 0 198 128
43. 
12 
39 0 4 18 0 199 156
44. 
12 
40 0 4 18 0 200 162
45. 
12 
41 0 4 18 0 201 82
46. 
12 
42 0 4 18 0 209 94
47. 
12 
43 0 4 18 0 210 148
48. 
12 
44 0 4 18 0 211 138
49. 
12 
45 0 4 18 0 212 188
50. 
12 
46 0 4 18 0 213 164
51. 
12 
47 0 4 18 0 214 150
52. 
12 
48 0 4 18 0 215 118
* 
53. 
12 
49 0 4 18 0 216 150
54. 
12 
50 0 4 18 0 217 154
55. 
12 
51 0 4 18 0 226 112
Figura 14
34

MUESTRA DE SALIDA DE TARJETAS DEL EJÉRCITO
1. 
DATOS(MIRARII(I),I- 
1, 180)/
2. 
1 1,5,6,7,11,15,19,20,24,28,
3. 
2 32,34,38,40,44,48,52,56,60,64,
4. 
3 68,72,76,80,84,88,92,96,97,98,
5. 
4 99,-103,103,107,111,115,119,123,127,131,
6. 
5 135.139.143.147.151.155.159.163.167.171,
7. 
6 175,179,183,187,191,195,199,203,207,-208,
8. 
7 208,209,-210,210,211,215,219,223,227,231,
9. 
8 235.239.243.247.251.255.259.263.267.271,
10. 
9 275.279.283.287.291.295.299.303.307.311,
11. 
A 315.316.317,-318,3*0.318.319.320,
12. 
B 323.324.325.326.327.328.331.332.333.334,
13. 
C 335.336,-337,2*0.337.338.339.340.341,
14. 
D 342,343,344,345,346,347,348,349,350,-351,
15. 
E 0.351.352.353.354.355.356.357.358.359,
16. 
F 360.361.362.363.364.365.366.367.368.369,
17. 
G 370.371.372.373.374.375.376.377.378.379,
18. 
H 380,381,382,383,384,385,386,387,-388,0,
19. 
1 388.389.390.391.392,-393,4*0,
20. 
DATOS(LOOKI1(I),Si 181, 410)/
21. 
1 393,394,-395,2*0,395,396,397,398,-399,
22. 
2 3*0,399,400,-401,4*0,
23. 
3 56*0,401,402,403,404,
24. 
4 405.406.407.408.409.410.411.412.413.414,
25. 
5 415,416,417,418,419,420,421,422,423,424,
26. 
6 425.426.427.428.429.430.431.432.433.434,
27. 
7 435.436.437.438.439,-440.441.442.443,
28. 
8 444,-445,8*0,
29. 
9 445.446.447.448.449.450.451.452.453.545,
30. 
Un 455.456.457.460.461.462.463.464,
31. 
B 465.466.467.468.469.470.471.472.473.474,
32. 
C-475,475,-476,0,476,477,478,479,480,481,
33. 
D-482,0,482,483,484,485,486,487,488,489,
34. 
E 490.491.492.493.494.495.496.497.498.499,
-
.35. 
F 500.501.502.503.504.505.506.507,-508.508,
36. 
G 509.510.511.512.513.514.515.516.517.518,
37. 
H 519,520,521,524,525,526,527,-528,2*0,
38. 
Yo 528.529.530.531,-533,2*0.533.534/
39. 
DATOS(LOOKII(I),I- 411, 512)/
.
40. 
1 535.536.537,-538,0,538.539,-540,2*0,
41. 
2 6*0,540,541,-542,0,
42. 
3 10*0,
43. 
4 542,-543,7*0,543,
44. 
5 546,-549,549,550,551,552,553,554,555,556,
45. 
6 557.558.559,-560,-561,3*0,
* 
46. 
7 2*0,561,-562,2*0,562,-563,2*0,
47. 
8 32*0/
48. 
DATOS(ITAB (I),I- 
1, 80)/
49. 
1 6986039920, 7288029840, 8932196640, 7355138720,13429933040,
50. 
2 21038067314,15040447088,15074001552,13496942880,15141110432,
51. 
3 26851541616,26885096080,26918650144,26952204960,18258330224,
52. 
4 19097191056,20204486944,19164299936, 6719013872, 8597832304,
53. 
5 8899822224, 9470247200, 8966931104, 8597865072, 9168290448,
54. 
6 9470279968, 9235399328,13427541362,13463290512,13496844576,
55. 
7 13530399392,15038841458,13495337250, 6983877232, 7017431696,
re 
Figura 15
35
"..................'....'.. 
.- 
.

.° 
-
.
.
c 
r 
.
° 
.
.
.
o .
°
* -  
MUESTRA DE SALIDA DE TARJETAS DEL EJÉRCITO
56. 
8 7050985760, 7084540576,15038874226,13495370018, 6983844464,
57. 
9 7017398928, 7050952992, 7084507808,13429146224,13462700688,
-
58. 
Un 13496254752,13529809568,15038153328,15071707792,13494649120,
59. 
B 15138816672,15038186096,15071740560,13494681888,15138849440,
60. 
C 15038218864,15071773328,13494714656,15138882208,15038251632,
61. 
D 15071806096,13494747424,15138914976,15038284400,15071838864,
62. 
E 13494780192,15138947744,15038317168,15071871632,13494812960,
63. 
F 15138980512,15038906994,15071904400,13494845728,15139013280,
64. 
G 15038382704,15071937168,13494878496,15139046048,15038415472/
65. 
DATOS(ITAB 
(1),yo- 
81.160)/
66. 
1 15071969936,13494911264,15139078816,15038939762,15072002704,
67. 
2 13494944032,15139111584, 6986007152, 7019561616, 7053115680,
68. 
3 7086670496, 6983910000, 7017464464, 7051018528, 7084573344,
69. 
4 26849444848,26849313776,26849412080,13694829168,15338996368,
70. 
5 11077583136,15406105284,17991500400,19367232144,18327044384,
71. 
6 19434341024,17991533168,18830394000,18058641696,18897502880,
72. 
7 18528436848,19098862224,19669287200,19165971104,19065340528,
73. 
8 19367330448,21279932704,19434439328,17454760560,17488315024,
74. 
9 19132481824,17555423904,16381051504,16146170512,17253466400,
75. 
A 16213279392,20676051568,20441170576,21011595552,20508279456,
76. 
B 19333907056,19367461520,21861934688,19434570400, 7254344304,
77. 
C 8361640592,11079549216, 8428749472,13428621936,14804353680,
78. 
D 12690424096,14871462560,17992057456,19367789200,19938214176,
79. 
E 19434898080,15039300208,16415031952,18596069644,16482140832,
80. 
F 22555525744,22320644752,25306988832,22387753632,19602768496,
.
81. 
G 19367887504,22058796128,19434996384,20676543088,20710097552/
82. 
DATOS(ITAB 
(I),I= 161, 240)/
83. 
1 20206780704,20777206432,16918479472,17220469392,15911846176,
84. 
2 17287578272,20676608624,20710163088,20206846240,20777271968,
85. 
3 19334464112,19368081576,20743749920,19435127456,17455710832,
86. 
4 17220829840,15106900256,17287938720,16392001776,16952427152,
87. 
5 17791287584,17019536032,19066389104,19099943568,20744110368,
88. 
6 19167052448,17455809136,18294669968,18596659488,18361778848,
89. 
7 24972934672,25810895504i25844449582,25878004384,17187439216,
90. 
8 18831606416,18328289568,18898715296,17724342896,18026332186,
91. 
9 18328322336,18093441696,16919069296,16415752848,18865226061,
92. 
A 16482861728, 7520977458, 7521010226,13428458864,26848331088,
93. 
B 14768177776,15070167696,13491309024,15137276576,15036646000,
, 
94. 
C 16412377744,13493141792,16479486624,13962936944,15070233232,
95. 
D 11345690912,15135342112,15036711536,16680878736,14566949152,
96. 
E 16747987616,15036744304,15607169680,11345756148,15674278560,
97. 
F 8057455216, 9970057872, 8929870112,10037166752,14768374384,
98. 
G 16412541584,12687999264,16479650464,15036842608,16144138896,
99. 
DATOS(ITAB 
(I),I-241, 320)/
100. 
1 14298644768,16211247776, 5641634416, 7017366160, 7319355680,
101. 
2 7084475040, 5910332016, 7286063760, 6782746912, 7353172640,
102. 
3 13694993008,15070724752,14835843360,15137833632, 6178833008,
103. 
4 7017693840, 7856554272, 7084802720,22284993136,23660724880,
104. 
5 22352101664,23727833760,15037268592,16144564880,14567506208,
105. 
6 16211673760,15305736816,16949904016,12420055328,17017012896,
106. 
7 15037334128,16413065872,12956959008,16480174752,15037366896,
107. 
8 16413098640,12956991776,16480207520, 8863384176,10775986832,
108. 
9 10272669984,10843095712, 13427081840,14534378128, 9467658528,
109.
110. 
ESTE DATO CONTINUA POR UN TIEMPO
.
Figura 15 (Continuación)
36

MUESTRA DE SALIDA DE TARJETAS DEL EJÉRCITO
169. 
DATOS CITAB(I),I- 
567, 
569)/
170. 
DATOS (COMPOS(I),Estoy 
1, 
3)/
171. 
1 2,64096,28768/
172. 
DATOS ICMPRS,NEND / 567, 
569/
173. 
DATOS (PRINCIPALNo (1),1- 
1, 
330)/
174. 
1 52,100,150,112,200,136,50,2*64,100,112,52,112,52,100,
175. 
2 10*112,2*52,3*200,
176. 
3 102,0,2*134,138,142,130,122,154,144,54,100,134,112,168,
177. 
4 146,154,126,154,144,130,122,142,130,186,128,132,126,56,0,
178. 
5 56,100,0,200,110,112,104,2*112,60,110,112,42,44,102,
179. 
6 46,166,112,114,2*112,66,100,60,108,100,144,98,2*96,
180. 
7 3*100,3*0,112,50,7*200,
181. 
8 64,2*200,2*100,2*200,3*0,160,140,150,200,100,
182. 
9 200,76,2*100,5*200,2*0,2*150,100,200,
183. 
Un 142.140.154.148.140.160.140,2*158.152.156.128.134.122.108,
184. 
B90,94,122,112,2*116,132,112,100,142,110,156,104,138,120,
185. 
C 132.142.150,2*0,150,2*200.100,50,5*0,
186. 
D 72,108,3*0,3*200,100,4*0,112,200,60*0,
187. 
E 0,4*164,4*94,4*146,2*94,
188. 
F 2*94,2*80,2*54,2*158,2*110,3*156,2*108,
189. 
G 108.148.100.162.108.200.158,2*110.200,0,200,2*150.200,
190. 
150,9*0,2*150.200.164,94,
191. 
1 158,110,164,94,148,10*104/
192. 
DATOS (MAINO (1),1- 
331.512)/
193. 
1 80,54,80,54,158,110,156,108,0,106,2*0,145,
194. 
2 56,100,110,162,108,2*0,76,2*92,100,2*110,2*108,
195. 
3 2*78,76,66,92,4*94,54,110,2*108,111,94,
196. 
4 54,108,94,0,110,54,200,86,80,78,76,130,138,96,118,
197. 
5 124,98,200,146,84,2*108,3*0,150,4*200,
198. 
6 3*0,5*200,2*0,200,150,3*0,
199. 
7 6*0,2*200,7*0,
200. 
8 5*0,118,8*0,52,
201. 
9 52,0,11*100,2*0,
202. 
Un 148,6*0,118,3*0,146,3*0,
203. 
B 32*0/
204. 
DATOS (PRINCIPAL2 (I),I= 
1.512)/
205. 
1 54,2*0,112,200,142,0,66,68,100,0,52,0,52,100,
4206. 
2 10*112,2*52,3*0,
207. 
3 114,0,144,140,142,144,130,120,152,144,62,110,144,122,166,
208. 
4 144,154,128,154,144,128,126,142,136,192,140,134,122,2*0,
209. 
5 4*0,112,122,112,124,116,74,122,120,52,54,112,
210. 
6 52,176,120,126,2*122,80,108,72,118,112,160,112,114,102,
211. 
7 9*0,200,5*0,
4212. 
8 68,14*0,
213. 
9 272*0,200,12*0,
214. 
Un 44*0,52,
215. 
B 52,14*0,
216. 
C47*0/
217. 
DATOS (t4AIN4 (1),1- 
1.512)/
218. 
1 66,2*0,100,200,150,0,2*70,2*100,52,100,52,100,
219. 
2 10*100,2*52,3*0,
220. 
3 82,0,136,134,146,158,142,128,156,162,82,94,148,138,188,
*221. 
4 164,150,118,150,154,112,132,154,138,192,2*136,140,2*0,
* 
Figura 15 (Continuación)
37


MUESTRA DE SALIDA DE TARJETAS DEL EJÉRCITO
222. 
5 4*0,2*100,84,108,84,66,94,106,54,50,110,
223. 
6 58,166,108,92,2*96,76,70,62,110,82,128,106,90,80,
-,224. 
7 422*0/
225. 
DATOS(NAIH6 
(yo),- 
1.512)/
*226. 
1 54,2*0,112,200,142,0,66,68,100,0,52,0,52,100,
227. 
2 10*112,2*52,3*0,
228. 
3 114,0,144,140,142,144,130,120,152,144,62,110,144,122,166,
229. 
4 144,154,128,154,144,128,126,142,136,192,140,134,122,2*0,
230. 
5 4*0,112,122,112,124,116,74,122,120,52,54,112,
231. 
6 52,176,120,126,2*122,80,108,72,118,112,160,112,114,102,
232. 
7 9*0,200,5*6,
233. 
8 68,14*0,
234. 
9 272*0,200,12*0,
235. 
Un 44*0,52,
236. 
B 52,14*0,
237. 
C47*0/
Figura 15 (Continuación)
38

Nft, b 
eso 
Al 0 
Va 
0- 
norte y 
0V encendido 
0 
00 
00
4#4 
t4 
00 
44 
00 
-A 0 
00 
00 
c0 
0 0
0: 
cc 
444L19 
'84 
cc 0, 
0 
cc 
cc
fu 
4 4 
4hab 
"1, 
V4~I "10'" 
yo 
00 
00 
00 
cc
ccVmw 
.yo 
cc 
teniente 
0 
0 
cc 
cc 
:C 
0
cc 
0044 
00 
MnV 
no 
VIt0 
0000 
00 
00
44 
00 
NVLo-wwi 
ftwzum 
cc cc cc 
c0
yo 
.4 
un 
oh 
un- 
00 
00 
00 
cc 
00 
1
480 
%IWIDG 
CC, 
cc 
.8%p 
n0 
no 
tC 
c 
c
001L dbpw 
hacer 
abajo 
40 
oh 
00 
c 
ao 
D cc 
00
0.w 
V 
0 
NV..Activado 
peso 
4 
00 
00 
00 
un 
a menudo
00 
aiv 
2P un 
4 
CD 
' 
0 
AV w0 
re 
pies
44 
en 
0% 
en 
AVI 
nt- 
000 
cc 
00 
00 
1
94Ww 
un pie, 
DCo- 
yo 
00 pies& 
m@% 
00 
00 
00 
00 
eb
O44 
4 
c4 
Merl 
00 4p. 
cc 
a0 
cc 
V0 
cc 
6e
tambiénO 
ObMP 
%0 
44 
D* 
0 
c 
AMat 
cc 
00 
cc 
ellos
av a 
W. 
VI 
un 
"w 
t 
c 
0 
00 
c0 
00 
00 
00 
96
soy yo 
pies ~ 
0w 
40dos 
0VI 
ai 
00 
California 
c 
lon
noyo 
00v~ 
00w 
410 
0 
00 
009 
00 
00
fm^ 
c 
cc 
f4t yo 
090 
un*% 
00 
0 
00 
00 
1
IV en 
cc 
0 
televisión 
P0#4 
0 
0 0 
0 0 
0 0 
entonces 
1 0
08 0 
0i 
wila'a 
0~@ 
00wbt 
OV 
00 
00 
0C 
0 0-
NVI 
00 
w0 
.0,0 
de- 
c4 
00 
cc 
00 
cc 
1
4V un 
VO 
C9 
00009 
0 
ftanP 
00 
entonces 
c0 
00 
1
.00 
wQ 
ellos 
404 
en 
&V 
00 
la 
co 
CC 
0 0 WI
-.
0 
44 
gramo 
00004do 
00 
V 
00 
00 
b00 
00 
(
.ff 0 
0V% aV 
4.0f4 
f,0 
tp 
0 
c) 
00 
00 
00 
yo
44 un 
yo 
049 
004='; 
00 
00 
a00 
00 
00
@, 
%O 1 
QO 
CC 
finni 0 
pies, W% 
0cI0 
0O 
00C,
z A 
un 
2 
f 
t 
4 
WI 
"un 
0D 
0 
00 
00 
cc 
00 
1
en ftiLI un 
0 
NV 
wP Estoy en 000aCA 
0 
c 
0
co00 
00.6rdo 
00 
un- 
00 
003 
002 
00 
00
orden de compra 
00 
ellos 
.
Ot 
f 
0 0 
ag 
0bft 
0 
CJC 
00 
cc
% 
tj 
~~3 
004 
NV 
4.0 
44 un 
4wV 
0 0 
0n 
00 a 
00
cc4 
cc 
^1 
0 
w- 
CC) 
00 
00 
CA 
VC 
DO0
44 
un 
%0 
00 
ft4n 
oo- 
pies 
m 
0 
00 
00 
00
DOCII"0 
ftmwi 
.00JU 
anuncio 
COa 
CC. 
a00 
00
4LI- 
04LI.w~ 
44 un 
V 
peso 
00j 
00* 
00 
'0
00- 
0, 
wi4 
cca 
c 
00 
00 
0 
' 
re 0 
CAO 
0
1^es 
P4 
00 
cc 
t 0 
0 0 
w-f 
00 
00 
00 
00
orbeLV 
CJmm 
a4 w 
0t6t 
dL 
yo 
tp 
cc 
vv 
0 
cci 
0C
V% 
oh 
#- 
1& 
t-Primera Guerra Mundial 
44M0N 
00 
00 
en 
Q00 
00
C:v 
CA ~ 
00 rublos 
6vi 
00V~ 
0t. 0 
00 
HACER 
00 
c 
c
fy ~ 
~ 
norte 
b4 
4 
dos veces 
f 
r 
.
4 0 
0=0 
0 0 
00 norte 
00'
o0O4'Ja 
0 
0 
40 
ES 
pies 
f 
00 
00 
cc 
00
NVI 
un 
" 
IV 
n' 
unN 
00 
0 
c 
ow0 
C.C. 
) -
CC
0%520 
4 0 
z 
norte 
q 
4 
% en peso 
0V pies 
DT 
000j0 
C.C. 
control de calidad 
0ºC
&,a 
NVI 
DOt 
00 
-S 
IV0t. 
00 
CC 
00 
CC
44 
oh 
"4 
PN 
4N 
yo 
00 
CC 
00 
00 
0. 
*'.
LL 
-
0 
Ij" 
0 
02Qe4% 
ENCENDIDO 
V% 
44 
la 
control de calidad 
CC. 
CC.
c) 
2 millones 44% 
~=b 
pies, 13 
un 
pies 
onzas 
00 
00 
.IO f
voy 
0.- 
DCSU. 
c. 
notario público 
-
c 
c.. 
CC g-
llj 
~ 
0W.~ 
4m 
4 
"Si 
00 
00 
a001 
00 
-1)C.
c, 
f 
f ~ 
CC " 
norte 
4 
w 
". 
0 
t 
V0 
L-1 L. 
c 
C.C. 
TODOS
04 pies 
.
IV 
oh 00 
14~metros 
pies 0. 
00 
00 
00 
-~ 
-l
C-8 .6f% 
t 
V, 
1 y 10 
.6 
dw 
C- 
CC 
Yo C.* 
LLj 
c.
l 
un 
f% 
0 
.,pag 
0 
4.0 
%& W.4 
00W 
OLP 
011 
002 
-1, :
VC 
Nueva York 
1* 
Ocra 
CL, 
os 
jr4 
pag 
C.4 CD 
C-L-1 
CC. 
1 
yo
-ZW% 
ES 
C4 
) 
031 
jir 
f 
ES 
N-,j 
c, 
.3 
0jQ0 
ca.,
ry 
4 
9 
.
C.04 
CA -
44 
4N 
CI C-. 
V, vL 
0r.-
0 
D' 
*o 
-)Yo ;N 
un 
4 
CLL nY u CA, 
NV4 
pies 
0 
-
03 
3'!v A
MO 
yo* f 
.W, 
peluca.. 
ES 
.0 
04 
VOt 
W. 
c 
c 
CC:
entonces 
3VI 
ES 1K 
30 
CA 
na 
ay 
00 
30A 
0.C3 
j 
0 C2 
un-
r-, 
ES C 
ev 
pag 
% NV del OG4 
P.,W 
e 414 
44A 
% en peso 
un 
CAC 
C*U
002 
,30 
00 
En%#- 
OOC3 
,.en4Y 
00 
00 
CA
%W 
ES- 
44 
C-. c 
4 
NP. 
w. 
Ci 
C1Q CQ 
LCaO 
CC
.4 
%b 
.0 
yoIW 
yo" 
r 
pag 
t 
1 
00 
P0 
03C30 
0iD 
un 0
00 
.N CA 
WLV 
vL CA'a 
Pi0 
r 
0b 
re 
tu 
SD 
c 
0 CCA0 
CI
00 
00 
-00 
~A" 00 
.
oh 
t 
-
FLC 
00 
.20 
co 
!130
CC) 
44 
ftb%" 
pag 
c. 
novio 
V 
C.a~ 
CA 
una Q 
c 0 
0 
c) 
CAD 
-,al
W1% 
W. 
w 
0D 
dos 
"w 
44 
V 
pa-a 
00 
03,0 
00 
L 0 
-
04O 
Q40 
C% 
LDfE 
C Ci 
=M 
0 
tN CC 
0ºC 
C- 
RC. 
un
00f 
le 
00 
44 
W.6V 
du 
-
L# 
00 
-
c 
00 
C0 un
HACER 
W. 
ACEITE OUINLDJ4P. 
c 
mc% 
la 
0 
C... 
ClC. 
CL 
0% 
.
.410 
W. 
2 40 
q 
-S. 
CA 
V ~ 
V 
00, soy 0 
00Q 
Z·jO 
O3
NO 4 
%. CC 
.00 
c 
q 
C' 
"Yo-- 
C.LIN 
c 
.
0 
q 
c. 
C,.C
du 
ENCENDIDO 
14.0 
-
4 
% en peso 
P4 bN 
00oI 
00 
=Un 
0 
0nC 
C22 
un
C .yCi a a 
norte 
U- 
pies 
pag 
C, V, 
ftbr 
9C 
CC. 
l. 
(C' C-C C C 
'
00 04 
42

a4 
4@" 
oo3$ 
4 
3Z0 
0. un 
3a 
C 0--
WV LC 
ft0%4 
PC 
.8 LaO 
NP.- 
CC 
CC. 
C) QD 
mentira 
CWIC.C
N4k 
C's 6n 
.0 
Nuevo México 
eso 
) 
10C 
jr. 
00 
44 
0A 
00 
m 
0 
HACER 
=
CC 
un' 
E-C un 
norte 
un 
W. 
&"C' PIC..aj-ft 
W. 
C,.
co c 
CC 
C C. a&
li 
Yo* 4p4 
4 0 
planear 
0 0 
NP..., 
00 
00 
C3L) 
CA 0 
03 
CU
0- 
CL- 
c 0 
CC, 
pies W, 
LC 
-
r-. 
cc 
DC. 
CL.. 
CC-r 
.'
0.
0 
RD 
0 
.
C.C. 
c, 
c 
! I.C-.. 
c. 
California 
l
5% 
5% 5% 
5% 
5% 
% 
% 
5 
% 
% 
5. 
P*


,pag 
en 
F9 en " 
'. 
-
-
.
.
.
.
un
"d 
' 
" ._ 
.
* .. 
' 
-. 
.
.
-. 
* 
S 
" 
-
.. 
.
.
"-4 
.
CORRECCIONES DE DIBUJO DE LÍNEA PARA EL ANCHO DE LÍNEA
LÍNEA A
W.-" 
LE 
Y(X
2,YI) ORIGEN DE LA LÍNEA VERTICAL
IP 
(LÍNEA 
LONGITUD (X)
(:.XIY 
1 ORIGEN DE LA LÍNEA HORIZONTAL
LONGITUD DE LÍNEA
(Y)
un
PASO 1. ELEVAR EL ORIGEN DE LA LÍNEA VERTICAL POR EL ANCHO DE LA LÍNEA HORIZONTAL, LUEGO
AUMENTAR SU LONGITUD EN ESA CANTIDAD.
yo( 
2 YI + AY) NUEVA LÍNEA VERTICAL
S 
l 
ai 
Y 
21ORIGEN
W-..- 
LONGITUD DE LÍNEA (X)
(X1,Y1 ORIGEN DE LA LÍNEA HORIZONTAL 
LONGITUD DE LÍNEA (Y + AY)
yo 
-. 
yo
-HACHA 
j- ANCHO DE LÍNEA
PASO 2. AUMENTAR LA LONGITUD DE LA LÍNEA HORIZONTAL POR EL ANCHO DE LA LÍNEA VERTICAL.
-.,- 
PESO YLNELNTXL 
yo 
ORIGEN DE LA LÍNEA VERTICAL (X2 ,Y + 
Y)
! ',.LÍNEA 
LONGITUD (X + AX)
(XI,YI) ORIGEN DE LA LÍNEA HORIZONTAL 
LONGITUD DE LÍNEA (Y + -Y)
SAXO 
ANCHO DE LÍNEA
*'." 
Figura 17 
40
.1*


DIAGRAMA DE ESPACIADO DE CARACTERES
.5z
,.'-
ui
' 
Ud.
'"n
%Ln
lln
" 
Figura 18
{ 
41
"" 
.... _ 
-,J
yo"yo*
". .','-..o .
Yo._ 
yo.... 
iY 
......
yo
'S..,,.,. 
.
.
.
, 
- .. 
-. 
, 
.
.. 
-
.,. 
.•, 
, 
,'% 
,",-.. 
.: 
:, 
:, 
,,,,,,,".'...r,'-


k 
x
k 
21 
25 
30 
35 
4.0 '5 
5C 
!5 
a 
t .
7C 
79, 
CE 
y
k
k 
x 
k
10x 
101
k 
k
k 
k 
k
k 
k 
k
x 
k 
k
zc2C 
2C
25 
2., 
25
30 
30 
30
3535 
35
4.0 
40 
.
'.SKOXXKOXKKKOKKKKOKKKOKKKOKKKOKKOKKXOXKKKOKKKKXXCXXCXXKKOKKKKCXXXKCK
k 
20 
25 
30 
35 
4,0 4,5 5c 
55 
ce 
65 
7C 
75 
00 
1
50 
50 
5 ºC
55 
5
60 
60 
a
65 
65 
t
*70 
7c 
7C
7575 
75
k 
k
k 
k 
k
x 
x
k 
k 
y
00 
ko 
k
x0 
x
k 
k 
k
k 
k 
k
k 20 
25 
30 
35 
4C 
'.5 
5c 
55 
60 
65, 
71 
7! 
e0 
k
COORDENADAS ABSOLUTAS DE PÁGINA EN ESPACIOS
Figura 19
4 
42


MODIFICACIONES I9 TIEMPOS ROMANOS, BODONI Y GÓTICO
BODONI
Banderas de composición tipográfica
Tipo 
para conseguir
en rojo
facebook 
mantener la cara
Fi,Fd 
cara cursiva
ff 
negrita cursiva
Fa 
caracteres de tamaño más pequeño (usar en lugar de fuente en minúsculas)
Las fuentes Fc, Fe y Fg se deben utilizar sólo después
consulta
fe 
0
fe 
fuentes
fg 
cara monowidti
fn 
volver a la cara normal
TIEMPOS ROMANOS
Tipo 
T gettipografía 
Banderas
en rojo
*Fb 
cara audaz
Fi,Fd 
cara cursiva
ff 
negrita cursiva
Fa 
caracteres de tamaño más pequeño (usar en lugar de fuente en minúsculas)
Las fuentes Fc, Fe y Fg se deben utilizar sólo después
consulta
fc 
0
fe 
fuente.9
fg 
cara monoancho
fn 
volver a la cara normal
GÓTICO
banderas de composición tipográfica
Tipo 
para conseguir
en rojo
facebook 
cara audaz
Fi,Fd 
cara cursiva
pies 
negrita cursiva
Fa 
caracteres de tamaño más pequeño (usar en lugar de fuente en minúsculas)
Las fuentes Fc, Fe y Fg se deben utilizar sólo después
4. 
consulta
fc
fe
fg 
fuente 
gramo
fn 
volver a la cara normal
Figura 20
4 
43

UNA PÁGINA DE MUESTRA DE LA PUBLICACIÓN ESPECIAL 480-3 DE NBS
Sntltifil ailon 
una eacrie alternativa$
Tipos de departamento 
Región geográfica de la LEAA
policía estatal 
, = Connecticut. Maine. Masa.. N.H.. RI.. Vt.
Policía y alguaciles del condado 
2 = Nueva Jersey, Nueva York
Ciudad con 1,9 agentes 
3 = Del.. Maryland, Pensilvania, Virginia, .
Virginia, D.C.
Ciudad con 10-49 oficiales 
4 = Alabama, Fla.. Ga., K).. Mi.s.. N.C.. S.C., Tenn
Ciudad con 50 o más oficiales 
5 = III., Indiana, Michigan, Ohio. Wisconsin, Minnesota.
Las 50 ciudades más grandes de Estados Unidos" 
6 = Arca.. La., N. Mex.. Okla.. Tex.
departamentos del municipio 
7 = Iowa, Kansas, Missouri. Nebr.
8 = Colorado, Mont., N. Dak.. S. Dak., Utah. Wyoming.
9 = Arizona, California. Nevada, Hawái
10 = Alaska. Idaho, Oregón, Washington.
I Fluyendo al Wo lartt,
R, población. yo soy 
1970 cen...
T4Bt.F 1.2.2. Número de departamentos de policía b.N región y tipo
Región LEAA
Tipo de departamento 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
totales
Estado 
6 
2 
5 
8 
6 
5 
4 
6 
4 
4 
50'
Condado 
66 
84 
257 
764 
536 
.506 
413 
288 
103 
120 
3.137
Ciudad (1-9 oficiales) 
27 
348 
713 
979 
1:470 
703 
611 
283 
135 
217 
5.486
Ciudad (10-49 oficiales) 
40 
237 
166 
344 
508 
230 
142 
71 
168 
79 
1.985
Ciudad (SO- funcionarios) 
60 
64 
36 
83 
119 
46 
23 
19 
87 
17 
554
50 ciudades más grandes 
1 
4 
5 
8 
10 
8 
3 
1 
8 
2 
50
.
Municipio 
629 
349 
362 
234 
1.574
totales 
829 
1.088 
1.544 
2.186 
2.883 
1.498 
1,196 
668 505 
439 
12.836
*" ---
~ue 
ar 
donde......... donde 
ac.tt, enviado a 56 departamentos de stote potece desde entonces 
.
el 
eran 6 .t.e 
departamento.
h,h 
lited 2 patte agnc 
o. h-...
referencia a una agencia central común 
Sin embargo. solamente) se aceptará un juego de queitonairen 
cada uno de estos nit stale- a% descrito en el volumen I.
aplicación B. pág 8-2
T Bt.E 1.2-3. Número de departamentos seleccionados t) reciben el
Cuestionario Detallado: Sirenas y luces-b. región y departamento t.pe
oh 
Región geográfica de la LEAA
Tipo de departamento 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
totales
Estado' 
6 
2 
5 
8 
6 
5 
4 
6 
4 
4 
50
-" 
Condado 
10 
10 
10 
10 
10 
10 
10 
10 
10 
10 
100
Ciudad 11,9 agentes) 
9 
10 
10 
10 
10 
10 
10 
10 
10 
10 
99
0 
Ciudad (10-49 oficiales) 
10 
10 
10 
10 
10 
10 
10 
10 
10 
10 
100
- mi 
Ciudad (más de 50 oficiales) 
10 
10 
10 
10 
10 
10 
7 
6 
10 
6 
89
50 ciudades más grandes 
1 
4 
5 
8 
10 
8 
3 
1 
8 
2 
50
Municipio 2  
10 
10 
10 
10 
40
culo 
totales 
56 
56 
60 
56 
66 
53 
44 
43 
52 
42 
528
ioesiinnaireo fueron actusil 
enviado a 56 departamentos de policía de stiae % desde allí .ee IS st 
departamento 
wh, h litrd 2 agencias policiales 
niltos
ieleresce a una central común después) Sin embargo. solos 
ne 
et ot cuestionario% -a 
aceptado de cada uno de ellos% rancio
Los departamentos de T-wsshtp existen solo en retsns I. 2..3. y 5
Figura 21
44
,V.
fácil


EJECUTAR FORMAS DE TRANSMISIÓN UTILIZADOS PARA PROCESAR UN ARCHIVO ASCII
CON GPSDC PARA TIPOGRAFÍA
@RUN,M/R AAAAYY, 10000-CHARMS,AAAAXXXYY,5O. 10000,D1850
@MSG,N AA XXX AAAA FECHA FUENTE ASC*FILE.ELEMENT
@ELT, L AAAA* CORRE. ASCGPSXXX
@ASO, T 8.
@BORRAR ,C AAAA*GPS-XXX.
@ED,UNQ ASC*ARCHIVO .ELEMENTO, 8.
SALIR
@ARCHIVO ASC*GRATUITO.
@ASG,ARRIBA AAAA*GPS-XXX.
@USE I., AAAA*GPS-~XXX.
@NBS*PARA .PARA. W DSDXJVIDBLOCK. WVFONT,WVTABLE
@AÑADIR DSDG*GOGPO. SDFGpsDC
*PAL4)4 2=1
*MISC 1 82054 2
*PESTAÑA 3 10 1520 3040 100
ARCHIVO I NUEVO 
AAAA*GPS-XXX. FECHA FUENTE ASC*ELEMENTO.ARCHIVO
*CORRER
@START AAAA*EJECUTA .GPSGPOXXX
@EJECUTAR,N/R 
AAAAYY,10000-CHARMS,AAAAGPOYY,45,1000,D1840 
.Gps 
A GPO
@MSG,N AA,XXX,VVV,FUENTE,FECHA AAAA
@ELT,L AAAA*RUNS.GPSGPOXXX
@ASG,A 
AAAA*GPS-XXX. 
.NOMBRE 
EL ARCHIVO GPSDC
@USE 
1. 
,AAAA*GPS-XXX.
@ASG,A 
DSDG*GOGPO.
@AGREGAR, P 
DSDG*GOGPO. NBSASG
@MSG,W 
10000-ENCANTOS 
PLS ESCRIBIR HABILITAR VVV
@ASG,TJ 
2.,U9H,VVVW 
.CINTA 
PARA GPO
@REBOBINAR 
2.
@ADD, P DSDG*VIDBLOCK. SETFONT
VIDEOCOMP 500 
AAAA*GPS-XXX. 
FUENTE 
FECHA
@EOF
AAAAA 
es calificador de operadores
AA 
es la bandera de ejecución actual
XXX 
bandera de trabajo actual
VVV 
es una cinta de controlador directo para dispositivo de composición tipográfica
FECHA 
fecha actual
FUENTE 
nombre de fuente deseado
ASC*ARCHIVO. ELEMENTO
dirección del expediente a tramitar
* 
Figura 22
45

. ., 
.. , 
.... . .
-. 
, .
-
.i 
.. 
.
.> 
.
EJEMPLOS DE LISTADOS DE PAÍSES DE UNA TABLA DE NOMBRES DE LUGARES INTERNACIONALES
TU 
TURQUÍA 
máquina virtual 
VIETNAM 
SA 
ARABIA SAUDITA
provincia/ili 
provincia 
emirato/min~aqat
" 
TU0I 
Адана 
VMO1 
An Giang 
VI 
'afif
, 
TU02 
Adnyaman 
VM02 
Bac Thii 
SA02 
Al Bil/ah
TU03 
Afyón 
VM03 
Be'n Tre 
SA03 
Jawf IA
TU04 
agricultura 
VM04 
Binh Tri Thin~n 
SA04 
Al Khi$irah
TU05 
amasia 
VM05 
cao bang 
SA05 
Medina
TU06 
ankara 
VM06 
Cuu Long 
SA08 
Al Qa~im
TU07 
Antalya 
VM07 
Dac Lc 
SA09 
Al Qurayyit
.
TU08 
artvin 
VM08 
Dong Nai 
VI0 
Ar Riyfi
TU09 
Aydin 
VM09 
D'ng Thfp 
SA06 
Ash Sharqiyah
TUIO 
Balikesir 
VMI 
Giro de Gia Lai-Cng 
SALI 
'Asir
TUI1 
Bilecik 
VM11 
Hola B~ac 
SA15 
Al lJudfid ash Shamdlivah
TU12 
Bing6l 
VM12 
Hai Hung 
SA07 
Al Muqita'ah ash Shamiliyah
TU13 
Bitlis 
VM13 
Hola Phbng 
SA12 
Bisha
TUI4 
bolú 
VMI4 
Hola Nam Ninh 
EFS3 
Yo-yo
TU15 
burdur 
VM15 
Ha N6i 
EFS4 
La Meca
TU16 
bolsa 
VMI6 
Ha Son Binh 
SA16 
Najrín.
TU17 
Çanakkale 
VM 17 
Ha Tuy~n 
SA17 
Qizin
" -
TUI8 
Cankin 
VM18 
Hhu Giang 
SA18 
Ranya
% 
TUI9 
(Córum 
VM19 
Hoing Li~n Hijo
TU20 
Denizli 
VM20 
Hb Chi Minh
TU21 
Diyarbakır 
VM21 
Kie'n Giahg
iTU22 
Edirne 
VM22 
Lai Chitu
TU23 
Elazig 
VM23 
Lrm Dong
TU24 
Erzincan 
VM24 
largo un
TU25 
Erzurum 
VM25 
Minh Hai
TU26 
eski~ehir 
VM26 
Nghe Tinh
TU27 
Gaziantep 
VM27 
Nghia Binh
TU28 
Giresun 
VM28 
Phi Khinh
TU29 
gimiihane 
VM29 
Quang Nam-Di Nang
TU30 
Hakkiri 
VM30 
Qu~ng Ninh
TU31 
Hatay 
VM31 
Canto B6
TU32 
igel 
VM32 
Son La
TU33 
isparta 
VM33 
Tiy Ninh
VM34 
Thanh H6a
-
VM35 
Thii Binh
VM36 
Thuin Hai
VM37 
Tien Giang
VM38 
Vinh Phi6
Figura 23
46


Un ~ ~ 
~ ~ ~ ~ ~ ~ ~ ~ 
-
-* -~ -. -
-
-
-
' 
.
-
-
-
-- 
-
-
-
-
-
-
-
-
-
-
-
EJEMPLOS DE LISTADOS DE PAÍSES DE UNA TABLA DE NOMBRES DE LUGARES INTERNACIONALES
CI 
ISLANDIA 
HU 
HUNGRÍA
condado/sistema 
condado/megye
ciudad independiente/* kaupstabir 
división urbana/* fbviros
división urbana/* megyei viros
ICOI 
Akranes
1C02 
Akureyri 
*HU01 
Bacs-Kiskun
IC03 
Arnessysla 
HU02 
Baranya
IC04 
Austur-Barbastrandarsysla 
HU03 
bekes
IC05 
Austur-Hunavatnssysla 
HU04 
Borsod-Abafij-Zemp]6n
IC06 
Austur-Skaftafelissysla 
HU05 
budapest
IC07 
Borgarfjarbarsysla 
HU06 
Csongrid
IC08 
Dalasisla 
HU07 
Debrecen
IC09 
Eyjafjartarsysla 
.HU08 
fej~r
ICIO 
Gullbringusysla 
HU25 
Gybr
ic 11 
Hafnarfjbrbur *HU09 
Gybr-Sopron
IC12 
Hiisavík 
HUIO 
Hajdí-Bibar
IC13 
1safjorbur 
*Casco 
heves
IC14 
Keflavík 
*HU12 
Comírom
1C15 
Kjosarsysla 
HU13 
Miskolc
CI 16 
Kópavogur *HU 
14 
N6grid
IC17 
Myras~sla 
HU15 
pectorales 
*
IC18 
Neskaupstabur 
*HU16 
plaga
IC19 
Norbur-fsafjarbarsysla 
HU17 
somogía
IC20 
Norbur-Mfilasysla 
HU 18 
Szabolcs-Szatmir
IC21 
Norbur-I'ingeyjarsysla 
HU19 
Szeged 
*
IC22 
61afsfjdrbur * 
HU20 
Szolnok
IC23 
Rangirvallas~sla 
HU2 1 
Tolná
IC24 
Reikiavik 
*HU22 
vas
IC25 
Saubirkr6kur aHU23 
Veszprém
IC26 
Sey~isfjdrbur 
aHU24 
Zala
IC27 
Siglufjbr'6ur
IC28 
Skagafjartarssla
IC29 
SnamfelIsnes- og Hanppadalsssla
IC30 
Strandasysla
IC31I 
Subur-Mulasysla
IC32 
Subur-ingeyjarsla
IC33 
Vestmannaeyjar 
$
IC34 
Vestur-Babhastrandars~sla
IC35 
Vestur-Hu1navatnssysla
IC36 
Chaleco ur-Isafjarbarsysla
IC37 
Vestur-Skaftafelissysla
Fiue23.otiud
44

-~~ 
7 
77-
AV4
oh 
t- 
r_
'4 
CL
LL. 
C-
un, 
C- 
4.
W. 
0 
c, 
'4
-j 
un 
IR 
t- 
Cco
LsJ 
cc 
0cc 
un 
Yo.-. 
"- 
un 
'4 
m 
c 
1 
L..0
un 
c 
c 
=~VV. 
4 
un 
-l 
0fr
wj 
&4 (Ud. 
r. 
ci- 
L- 
A4
CZC-) 
O4 a. 
un- 
C2 
un
t-~ 
co 
00 X4t 
c 
...
f 
) 
0
~ CA 
.
444 
baño 
0'. 
(V- 
un 
-
4) DO 
%0'.ff-, 
Av. 
v 
l. 
Congreso Nacional Africano 
un 
Lu 
00
-24A 
l. 
000.0 
.- 
00-4 
4 
AL 
t- 
A C
c) 
.'~. 
'4 
c 
3 
oh 
( 
z 
c un 
au 
00
%. 
r- 
.0 
J5. 
4 
c.. 
co 
o 
4 0 
) 
.ACr
0 
0 
AV4 
0 ~- 
c a4 
un 
-
-0 
=
un 
A. 
=Aa 
v- 
N4C 
4 CV. 
U.. EN
A-(D 
CC 
c 0 
w4. 
ONA 
V4-1t
CL 
--
4 
( A-AZ 
W. 
GRAMO 
oh t- 
ir 
'40 
IV 
4 
cc
CC m 
-J 
C00 
sobredosis 
c 
4Ac4 
C4 
4.
4A 
A4 
un 
-44 
cz. co 
c
llja 
06cl 
.
AVA 4L 
00' 
-I)&C 
VA ~ 
r) 
4 mi 
-4 
c
ir a 
aff 
un 
=4 
(U4 
mA(~C. 
La. 
-V; 
c 
c
c. 
-
vc 
3C 
EN~ Ir 
'4 4 
0 
*r.
un 
un 
c- 
'4)
LL. 
r4. W. 
'4' 
UC 
, 
..
'' 
=~ 
c. 
c. A0. 
l 
0 
w 
mamá
CCD 44 A 
4 
LC 
r_ 
*.4 
C(VA) 
noviembre 
=.4 V4... 
0f 
m 
(UC 
oa
un 
0-1cca 
un 00 
aire cu =' 
(Ud. 
(r 
fkc 
.
un 
44 
0 
0
C)a 
-: 
r4'4 
z 
un 
ODC 
(w) 
*. 
0AC, 
c.
CPIL. 
r_ 
co&0
4 
-D% 
ls 
cca 
cC~ 
.P. 
CA 
C.00 
c 
C-ffl 
l 
t
VAL~ 
un( 
4 
07 
w 
00 
f)U 
l 
l. 
f*41'c 
4( 
AL 
CC 
cy 
UL
(UvwC 
aa 
c) 
ff.0L. 
-
VIff 
() 
Uy) 
W [L. 
A4c) 
ir 
soy, 
;MV
CtOnCOU A4 LL. 
4L..0 
ev' 
aire acondicionado, 
AA 
'4 
0 
0' 
v -
AL 
mira
'o0' 
un 
CIOa. 
M*m 
0 
4 0 
Arv 
4 
CA COC 
0 
C- 
CO 
.X
LL 0.4 
Ir co 0 A .0 
un 
R.4 
''4 
X4 0e, 
f 
un 
un 
CC 
7
C-.4 
Ud. 
'LL. 
un 
vehículo eléctrico 
.
z..-Lz.. 
a.0 
-V)4 Cr U 
co. 
*Un 
e~e. 
-LA.
w 
4 
0 (30 
l. 
.0 C.. 
a Ar9'.('. 
W. 
=rv 
c 
V 
c 
ULz 
un 
c 
(30 
AA 
0
>- 
( 
(Una oZ 
X es soy 
0AA0 
A0 
=L 
1" 
A00 
-A 
0'O 
c 
AAif 
q 
(, 
Ud. 
control de calidad 
0%
C4Am- 
=( 
'0 
CVC~200 
un 
4-0 
0 
(.AA 
%0 G 
un 
%0 L* 
ZA 
'4 
r 
c
5'.- 
0 
0.0 
4--A'4 
2-- 
1 
oh 
4* 
soy 
*0 
x 
A1. 
, 
'4
UE 4, A4 
; 
-Q A Ak0 
.AMA 
A u -* %-4( 
ma& 
4 
A0 
-4 
AA1 
6 
0
%0AI- 
ar 
llc 
cua 
4'-'4i' 
un* 
CLA 0) 
0o- 
.
.
M MA W4 W 0L 
C-ff. m
WW 
WW 
yo 
LU 
A'AM,.0%AA0 
(w- 00 A0*. AC LL. 
un 
...
yl 
= 
AD% 4j
AACU. 
tú 
-0 
4 
4-A4~ 
c 
A. 
GRAMO 
0 4 
OL AA- 
m 
41C 
Cri.> 
-
un 
muchacho 
Ud. 
, 
m*4 
4 
4 
r 
44sI-dCM. .
.OV o&4 X.0 
MA W = 
*
w 
AL 4 A4 0 X. JZAM 
rama 
AfXAACM 
un 
(V A CV.*C'C 
M-MZ..-O 
.4A C) CA- 
ANUNCIO
oC 
'4 
m 
un 
x 
Mj M, M~ 
-
(Ud. 
m 
m 
0 0 
-H 
'4 
m' 
(U ~ 
0 cm wu 
A (U 
2 
z 
-'4-
Li..~ 
~ 
0 
(Ud. 
-3. 
(U' 
j 
00 
zU~ 
z 
'lv 
Z'IY. 
CL 
H4'E'
0 
0- 
C0 A 
0 
Un, 
un 
.' 
0v 
nv n 
mV N'~ N 
,~ 
norte 
norte 
.8j Aire Ar 
metro (V, (W 
c 
mu- 
un 
( 
.
AW
6'0 
yo 
+U 
* 
AA 
un 
( 
AW 
v 
4 
aire acondicionado 
+U( 
un 
un 
U( 
z 
)
z 
I-I48

EJEMPLOS DE USOS DE LOS COMANDOS TIPOGRAFÍAS INTERNOS f80, f81, f83 Y f86
03100 Benjamín Fraklin ................................ 00 
Distrito de Columbia. B 20044 
50000 ................ 9
Parte B. Diacríticos
macron extendido
AB 
un
C04/12 
macron extendido a continuación
D07/06
AB 
ab
*. 
Prueba de línea inferior
Prueba de sobre puntuación
20 
30 
40 
50 
60 
70
C.f. 
C(0) 
C2(o)
Prueba de puntuación inferior y superior.
Teta de mder lir, sobre puntuación ad sade
En cualquier momento dado durante la ejecución de un programa ejecutable, el
La definición de cada variable, elemento de matriz o subcadena es
defrmedor unldefi nd (Sección 7).
-
Alcance de los nombres simbólicos y 
Etiquetas de estados de cuenta
FIPS 55 
Códigos para lugares poblados nombrados,
,,% 
Divisiones primarias del condado y otras entidades locales
Distrito de Columbia 
Página 
yo
Código: 11 Abrev Postal: K
Código postal 
Parte Otro
Lugar 
Condado 
Código postal de clase 
de 
Nombre GSA MIRF 
SMSA
Código 
Entrada 
Código Condado Código equivalente Código Rango Código CodL Código Código Código CD CD CD
00100 Anacostia................................. 
......... 
..
001 Distrito de Columbia. U4 20020 .. 50000 ......
00600 Anacostia Junction................................... 001 Distrito de Colombia. S.... .. 50000..... ... .
01100 Arcade ................................................ 001 Distrito de Columbia. X.... .. 50000 ..... .
.
.
01600 Barnaby Terrace................................. 001 Distrito de Colmlbia. U4....... 50000...
02100 Barnaby Woods ......................................... 001 Distrito de Columbia. 14 ...... .. 50000 ....... .... ....
02600 Bellevue ................................................ 001 Distrito de Columbia. U4.... .. 50000... . ..
03100 Benjamín Franklin ................................ 001 Distrito de Colombia. B 20044 
50000.
03600 Benning ................................................ 001 Distrito de Colombia. U4 20019 
50000 
.
4
04100 Alturas de Benning ................................ 0 
001 Distrito de Colombia. U4 ...... 50000 ................
4.
,' 
Los números misteriosos son 
válido 
entrada 
desde el 
terminales. 
ellos son
creado por un dígito 
(1-9) signo de interrogación de retroceso. Se ven de la siguiente manera
1, 2. 3, etc. 
Los números misteriosos se pueden utilizar sólo después 
acuerdo
con el 
publicación 
sección. 
Otros personajes pueden ser creados por el 
usar
de un rojo 
f6 como sigue V, m., 0. M.
v.
Figura 25
49


4.4-.
4..o4.yo
.7o4 
-
q 
'Nueva Jersey
3 
-'Z)
gramo
c 
oh 
" 
" 
'% 
: -0 
0 
P "yo 
. ,
.
l 
s 
3
* " 
44 
-4+.. 
-
-
, 
.
. , 
: 
-
4. 
.. 
yo. 
_ 
-4
le) 
4P 
t
61 
IV 
yo 
.
L;'.3
00 
-o 
r-
%. 
V)
40' 
r 
-. 
7
ir 
co 
4) 
4 
7 
4
tu 
oh
• 
* 
*
lo 04( 
43 
41 
jo
AP 
.1 
? 
-
t 
30 )'
0C 
V 
4V 
-74 
r- 
4
00 
a 
I0 
t 
oh
6. 
f 
O-
^ 
" 
.
-
-
1
AD4 
yo 
0 
0 
4DAVA 
RJal 
0 
V4 
9 
0 
c 
03 
Un,
5004 
3


'4)
2
w 0
cco
C., 
s 
0.
.1 
'oh 
4 
0 
.
t 
! 
.
z 
2 
-.
0 10 .0 
metros 2 
0 
.
061 
c 
q 
000
c, 
a' 
a0 0 
'0 
0 
0
j 
3 
.3 
Ud. 
LJ 
l
L'i ~ 
41 
1 -
.
.
.1 -
CL~ 
C m
(1 02' 
entonces 0))S~~C
01. 
'30 
.4A 
££ 
£
L-4 0000-D 
2
C' 
c 
003000z03
zl. 
-
-~ 
AP 
f.. 
-34.- 
-
C.~ 
.
C. ANUNCIO)
l 
06 W. 
XUUCJC3VI
13 
m 
6V) 2C, 
P) 
*0C. 
~ 
l
V 
124 
0 
4o-Cos~ 
.
un 
:., 
*fl-44.4C44.4y
-
4) 
U0 
0'
CC.~~j 
4 
C'14." 
~ .
jefe 
-o 
'0* 
B.
ANUNCIO. 
2.C. 
9 
c
IV 
a0 
.0 
£0 
*0&0 
17
5.. 
4) 
130 
-ZV 
V ( 
' 0
-0.C. 
01r
a1 
C". 4)') 
', 
l 
0 
6CaL 
,P
+ 
c, 
c) 
.
un 
re 
4) ANUNCIO EN 'o0 
.
.0

... 
... 
PAG, 
.
wL 
.7 
& 
.
.. 
* 
' 
-'------;- -- ;-- 
" • 
--
mi 
" .,o 
. 
W.
'
t
l 
"  
yo
REGLAS SOBRE REGLAS Y TAMAÑOS DE PUNTOS
4.
4. 
Tamaños de puntos
Tipo 
para conseguir
.-.. 
en rojo
M5ed 
Tipo de puente Fe
s. 
16Si 
Tipo de punto
f07 
Tipo de siete puntos
lleno 
Tipo de ocho puntos
)f09 
Tipo de nueve puntos
fl0 
Tipo de diez puntos
f12 
Tipo de doce puntos
f14 
Tipo de catorce puntos
f18 
Tipo de dieciocho puntos
f24 
Tipo de veinticuatro puntos
REGLAS
Las reglas nunca deben estar centradas ni justificadas. Las reglas están hechas por una serie de
desventajas seguidas. Las reglas aparecen en el centro de la línea y no en la parte inferior de la misma.
línea como en subrayado.
regla normal
Regla de la luz (Fa Rojo)
Regla pesada (Fb rojo)
Regla extra pesada (rojo Ff)
Regla doble (Fi roja)
normales 
Luz 
pesado 
-
Extrapesado 
-
doble
,.
Figura 27
52
.s.
* 
* 
.
--
",


EXTRACTOS DEL MANUAL DE ESTILO DE ENERO DE 1973
Extractos del Manual de estilo GPO de enero de 1973
Términos científicos y técnicos.
6. PALABRAS COMPUESTAS
6.42. No escriba un guión en términos científicos (nombres de sustancias químicas,
enfermedades, animales, insectos, plantas) utiliza modificadores de unidad si no aparece ningún guión
en su forma original. (Ver lista de nombres de plantas, p. 277, y nombres de insectos, p.
284.)
envenenamiento por monóxido de carbono 
contenido de uranio equivalente
crianza de conejillos de indias 
remedio para la tos ferina
suero de cólera porcino 
pero 
levantamiento de gusanos barrenadores
solución de bromuro de metilo 
Plantaciones de olivos rusos
control de oxidación del tallo 
gorgojo del pino blanco
Abeto de Douglas
6.43. Los elementos químicos utilizados en combinación con figuras utilizan un guión,
excepto con cifras superiores.
polonio-210 
uranio-235; pero U2'5; Srw; 2U2U. 
Freón-12
6.44. Tenga en cuenta el uso de guiones y puntuación de primer plano en fórmulas químicas.
9-nit roanthra(1,9,4,10)bis(I)oxatiazona-2,7-bisdióxido
Cr-Ni-Mo
2,4-D
6.45. Imprime un guión entre los elementos de las unidades técnicas compuestas de
medición.
hora de la vela 
año luz
hora de caballos de fuerza 
milla-pasajero
kilowaitt-hora
10. SIGNOS Y SÍMBOLOS
10.1. El creciente uso de signos y símbolos y su importancia en
técnico 
y 
científico 
trabajo 
tener 
enfatizado 
el 
necesidad 
de
normalización a nivel nacional y del uso coherente de la norma
formas.
.
pag
Figura 28
* 
53

EXTRACTOS DEL MANUAL DE ESTILO DE ENERO DE 1973
10.2. Ciertos símbolos son símbolos numéricos bien estandarizados (los dígitos,
0, 1, 2, 3, 4, 5, 6, 7, 8, 9); símbolos de letras (las letras del alfabeto, a, b, c,
d, etc.); y símbolos gráficos (los signos matemáticos +, -, 
, x,
10.3. La Imprenta del Gobierno proporcionará al costo nueva oferta especial
símbolos para cuestiones técnicas cuando sea necesario.
10.4. los signos 
x, 
-, -, × y -, 
etc., están cerrados contra el acceso a
Figuras y símbolos de paning. Cuando la X se utiliza para indicar "cruzado
con" (en la cría de plantas o animales) o ampliación, se separará
de las palabras que las acompañan por un espacio.
i-viii+ 1-288 páginas 
20.000±5.000
La ecuación A+ B 
Principios de junio X Bright (cruzado con)
El resultado es 4x4 
X 4 (aumento)
Símbolos con figuras.
10.5. La marca de grado siempre se utiliza en lugar de la palabra grado después
una cifra que denota la medida.
Ij.6. Cualquier símbolo que se establezca cerca de cifras como la marca de grado,
Mu griego, marco de dólar o c comercial (*, 
p, $, v), se usa antes o después
cada figura en un grupo o serie.
45* a 65' F., no 45 a 65' F. 
3g a 5o (sin espacios)
30k y 50p 
±2 a ±7; 2 ±1"; 3 ohmios ±1
Rango de precios de $5 a $8 
pero 
§ 12 (espacio reducido)
5-7' de largo. no mide 5-7' de largo 
del 15 al 25 por ciento
Símbolos de letras
10.7. Los símbolos de letras están en cursiva sin puntos y en mayúscula.
sólo si así se muestra en copia, ya que la forma en mayúscula puede tener un significado
., 
significado diferente. Sin embargo, algunos símbolos están escritos en romano si así se indica.
en copia.
Ecuaciones
10.8. En ecuaciones matemáticas, utilice cursiva para todos los símbolos de letras: mayúsculas,
minúsculas, versalitas y superiores e inferiores (exponentes y
subíndices); Utilice el romano para figuras, incluidos superiores e inferiores.
10.9. Si es necesario dividir una ecuación o una expresión matemática,
romper antes de +, -, =, etc. Sin embargo, el signo igual debe borrarse a la izquierda de
otros signos matemáticos iniciales. (Ver ejemplo (6), p. 170.)
Figura 28 (Continuación)
* 
54
.'J-
S... . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
k* 
.

EXTRACTOS DEL MANUAL DE ESTILO DE ENERO DE 1973
10.10. Una ecuación breve en un texto no debe dividirse al final de una línea.
Separe la línea para que la ecuación comience en la siguiente línea; o mejor,
centrar la ecuación en una recta sola.
10.11. Una ecuación demasiado larga para una línea se coloca al ras a la izquierda, la segunda
La mitad de la ecuación está al mismo nivel a la derecha y las dos partes están equilibradas.
, "como 
casi lo más posible.
10.12. Dos o más ecuaciones en serie están alineadas con los signos iguales y
centrado en la ecuación más larga del grupo.
10.13, Palabras explicativas de conexión, como por lo tanto, por lo tanto, y
De manera similar, se colocan al ras ya sea en la misma línea con la ecuación o en una
línea separada.
10.14. Si una fracción acumulada ocurre en una parte de una ecuación, todas las demás
las fracciones en esa línea deben acumularse.
10.15. Paréntesis, llaves, corchetes, signos integrales y signos de suma
deben tener la misma altura que las expresiones matemáticas que incluyen.
10.16. Los inferiores preceden a los superiores si aparecen juntos; pero si cualquiera
inferior o superior es demasiado largo, los dos están alineados a la izquierda.
Símbolos químicos
10.17. Los elementos químicos se designan con la letra inicial o una
forma abreviada del nombre inglés o latino. Están ambientados en romano,
sin puntos. (Para el tratamiento de los símbolos, ver la regla 6.44.)
2(KHCH 4O6)+ CaC0 3 = CaC4H4O+ K2C 4H4O+ H,O+CO.,
Símbolos estandarizados
10.18. Símbolos debidamente estandarizados por cualquier autoridad científica, profesional o
grupo técnico son aceptadas como formas preferentes dentro del ámbito de la
4 
grupo. La oficina emisora que desee o requiera el uso de dichos documentos normalizados
Los símbolos deberían comprobar que la copia se prepara en consecuencia.
Nombres científicos
11.9. Los nombres científicos de géneros, subgéneros, especies y subespecies.
-" .. 
(variedades) están en cursiva, pero en cursiva en formato romano; los nombres de
.4 
grupos de rango superior a los géneros (filos, clases, órdenes, familias, tribus,
etc.) están impresos en romano.
Como. perpálido
¿Dorotia? sp. (romano "?')
Tsuga canadiense
Cypripedium parviflorum var. pubescente
los géneros Quercus y Liriodendron
la familia Leguminosae
Mediciones de ejemplares de Cyanoderma erythroptera neocara
Figura 28 (Continuación)
55
.% 
-
-
-


EXTRACTOS DEL MANUAL DE ESTILO DE ENERO DE 1973
11.10. En el caso científico, se deben utilizar comillas en lugar de cursiva.
nombres que aparecen en líneas escritas en mayúsculas, minúsculas y mayúsculas, o en negrita, incluso
-; 
si hay letra cursiva disponible en la serie.
11.12. Todas las letras (mayúsculas, versales, minúsculas, superiores e inferiores)
utilizados como símbolos están en cursiva (excepto según lo dispuesto por la regla 8.122), pero en
Se utilizan letras romanas en cursiva. Símbolos químicos (incluso en cursiva)
materia) y algunos otros símbolos estandarizados están escritos en romano. (Ver también
-
reglas 6.44 y 10.8.)
enésimo grado; x dólares
D-0,025 V,'. 
0,042 
,.
G-1
5Cu:S.2(Cu,Fe,Zn)S2Sb2S0
4
11.13. Designaciones de letras en materia matemática y científica, excepto
Los símbolos químicos están en cursiva.
.'p
-.
'"
Figura 28 (Continuación)
56
-..-
* 
'' EN


LLII
-5-q
1en
.5..
centímetros 
c
facebook 1 
'-4
oh 
a
Ud. 
4)
;~ 
'= 
= 
9c
~-I0.
yo= 
.0 
Ai.
LA4 
-r 
0.
l)) 
0.V
c.a. 
060
.9- 
'.0 
0t
'U 
-yo
CC
04
00 
0D 
0
LU 
..-4 
-'-
.8 4
identificación 
-4
.0 
M..0 
M JO W Ad A M 
..0 A 
Anuncio0. M4* 
044AD A
57


06.0
-r44
c 
eso)
r-44
0 0
4:3. 
-4-
(Ud.
oh 
:.. C..4
(Ud.
~. 
0
z) 
m4 c4*~ 
00
norte; 
0 
44~' 
bo 
(.
v S.0 
rw 
yo 14 
0 
0
00 
0 
''' 
4
r~ 
+~ 
0) 
*\Ic
(y 
M-44--I 
02-4j 
8 
L.41
4cm 
02 
t ~ o 
ChoA 
4 
00
AdA.LV1 
0Avanzado 
MA 
VXA
580


A'-,
2: 
0 
0.En
-.
C Al
% 
V7
V 
w44
44 
U'%
0n 
48" 
Los Ángeles. 
q 
0;4
.~ >1. 
v) 0 
4 
r 
-
* 
)44 
c 
~ 
0. 
1. 
"oh 
v 
'A4 
4 
0
U)J 0 
+4AL)-
*t 
CU 
0 
1.0 
.
00 
:3m) 
.un ~ AN 
.
0) 
ALI CI
c 
%0A
oh 
C-CI
=~~~ 
4)-4 
0 
)
0) 
c 
en c. 
0oc
*- 
c00
1.- 
4) 
C).- 
4)
LU*0 
*m).
.JCi 
4).).8 
-
un 
un
-4~~~- 
aa 
" 
a0 
l
3 
pi 
12 
.

-
.*t~ 
* 
~*b~*. 
.
-
.. 
.-
COMO
0z
.5 
c
0 
0) 
4
.5V
q 
v 
cr
l.
4) 
un 
~A H8
0e P-4 
0L
t- 
4J
0 
0
I'.9) 
4) 
4 
4-..
0).
L.. 
-(0 
-
0
J9 
-4 
,0e4
segundo 
4) 
A) 
(Dq
-4 
4.4 
oh
LL 
0 
0. 
r. 
c 
oh
La. 
9, 
4 
wo 
9.n-a
"44 
'-.4 
-1 
"-'( 
0) 
F3 
-
)4-4 
4- 
C4C
8 
43 
2~ 8'
'Z0 
Wr4 
0 
.- 
-4 
00
H ~ 
.94i0c
LI 
=)-4 
43 
4), 
dos) 
0 
+ yo
l 
norte 
4 
4 
s. 
4 3 
0~ UN 
-4 
0o 
'D.. 
4
c~w 
l 
41-4
%~~~~~~~ 
0- 
-
-
14c 
44 
un
0~ )0 
-- 0S
aff 
4)a4) 
0) 
P). 
)un
*4) 
f'u 
' 
.
s. 
8 
S.4, 
yo
o'- 
C; 
O*4) 
00 
0 
C;O
Anuncio 
.i0f( 
0qL 
Anuncio 
N.aM 
da
60


6*Z
CA 
c
En4 
un.
enr 
*4 
z0 
-
4 
w. 
j 
Un, 
0
Un, 
un 
l 
b
c.,0
~4m~A 
un 
f-zV 
.* 
0 
C(
~~yo 
como 
.
01 
0).
LAJaa
0,4 
0. 
4.)4
tu 
SI 
V
c. 
.41 " 
41~
AZ 
yo 
"Un 
0,4.
~4 
1
0.' 
un 
I0 
-
'
m 
t
LAJr 
Ud. 
01"1
91 
a-yo 
cu
:9 
41 
)ff
ual 
04H 
.0 un 
yo 
CL
L4 
~ 
A 4.)IJ 
M& 
j 
4 
h
040 
: -
t. 
~a~
c 
0
52 
contra .9 
q 
4)
V4-
~~ 
"1 
-
ANUNCIO 
44.P 
pp..AJ.ArA.Ap.A.A-.A.. 
~ 
.


777.
norte
00)
P.-
* 
~L
oh 
un 
un%
I-VI
01-4
4! 
4-H
n-.. 
CM 
4)
w 
C6
LL 
8 
2L
LL 
.JJ
V 
j 
~
oh 
5.
w~
ua
llj 
a 
-4
+4 
La)4 
en 
el %.0-4
La) 
-3 
-V 
jMMm4) 
4 
3 
4
a0I L & I t V 
AV 
un 
- y 
(
*6
o--A


x 
EJEMPLO DE TABLA TOTAL 
x
CARGAR 
TABLA A 
FT 8 AGREGAR-G 1
IG
ELEVACIÓN DEL CUADRANTE 
PROYECTO, ÉL, M509A1
Espoleta, MTSO, M577
1 
2 
3 
4 
5 
6 
7 
8
CORRECCIONES A 
CORR 
CORR A
CUADRANTE 
CORR A 
QUAD ELEV 
PARA BAJO 
DEFL
ELEVACIÓN QUAD ELEV PARA UN INC DE 
NIVEL 
TIEMPO 
GAMA I 
PARA
PARA PROY. 
PARA PROY. 
50 millones 
VIENTO DE 100 M DE 
DE 
A 
PROYECTO,
M509A1 
M509A1 
EN HGT 
EN RG YO NUDO 
VUELO 
MPACTO 
509A1
MILLAS, 
MILLAS 
MILLAS 
MIL METROS 
SEC 
METROS 
MILLAS
45 
1025 
36,4 -126,9 
11.1 
25,7 
4627 
OA.5
50 
947 
45,0-136,6 
10.7 
24.7 
4979 
OA.4
55 
863 
55,8-146,5 
10.3 
23.6 
5243 
LO.3
60 
774 
69,2 -154,0 
9.7 
22.3 
5394 
OA.2
65 
680 
85,1-153,5 
9.0 
20.9 
5403 
OA.1
70 
585 
101,5-139,8 
8.3 
19.4 
5253 
OA.1
75 
494 
114.1 
-115,4 
7.5 
18.0 
4966 
0.0
80 
417 
118,4 
-89.0 
6.9 
16.8 
4617 
0.0
85 
355 
114,9 
-66,8 
6.4 
16.0 
4279 
0.0
90 
308 
107.0 
-50,3 
5.9 
15.4 
3989 
0.0
95 
271 
97,9 
-38,3 
5.6 
15.0 
3752 
0.0
100 
242 
89.2 
-29,6 
5.3 
14.8 
3563 
0.0
105 
219 
81,4 
-23.0 
5.1 
14.6 
3411 
0.0
110 
200 
74,7 
-18.0 
5.0 
14.5 
3291 
0.0
115 
184 
68,9 
-14.) 
4.8 
14.5 
3195 
0.0
120 
170 
64.0 
-11.0 
4.7 
14.5 
3119 
0.0
125 
159 
59,7 
-8,5 
4.6 
14.6 
3058 
0.0
130 
148 
56.0 
-6.4 
4.5 
14.6 
3012 
0.0
135 
140 
52,7 
-4,7 
4.4 
14.7 
2976 
0.0
140 
132 
49,8 
-3.2 
4.3 
14.8 
2949 
0.0
145 
125 
47.3 
-1,8 
4.2 
14.9 
2930 
0.0
150 
120 
45.0 
-0,6 
4.1 
15.0 
2917 
0.0
155 
115 
42,9 
0,4 
4.0 
15.2 
2909 
0.0
160 
110 
40,9 
1.2 
4.0 
15.3 
2907 
0.0
165 
105 
39.1 
1.9 
3.9 
15.5 
2911 
0.0
170 
99 
37,5 
2.4 
3.9 
15.7 
2921 
yo 
0.0
175 
95 
36.1 
2.9 
3.9 
15.8 
2931 
0.0
180 
91 
34,9 
3.5 
3.8 
16.0 
2944 
0 0
185 
88 
33,9 
4.0 
3.8 
16.2 
2959 
0.0
190 
85 
33.0 
4.4 
3.7 
16.4 
2977 
0.0
195 
82 
32.0 
4.8 
3.7 
16.5 
2997 
OA.1
200 
79 
31.1 
5.2 
3.7 
16.7 
3019 
OA.1
205 
77 
30.2 
5.6 
3.6 
16.9 
3042 
LO 1
210 
74 
29.4 
5.9 
3.6 
17.1 
3066 
OA.1
215 
72 
28,7 
6.2 
3.6 
17.3 
3092 
t.0.1
220 
70 
28.0 
6.5 
3.5 
17,5 
3119 
LO 1
l 
225 
69 
27.3 
6.8 
3.5 
17.7 
3147 
OA.1
Figura 30
J6.
x 
63X
un
.1

x 
EJEMPLO DE MESA NEGRA 
x
CARGAR 
TABLA A 
FT 8 ADD-G-1
iG
ELEVACIÓN DEL CUADRANTE 
PROYECTO, ÉL, M509A1
Espoleta, MTSQ, M577
1 
2 
3 
4 
1 
5 
6 
7 
8
CORRECCIONES A 
CORR 
yo 
CORR A
CUADRANTE 
CORR A 
QUAD ELEV 
PARA BAJO 
DEFL
ELEVACIÓN QUAD ELEV PARA UN INC DE 
NIVEL 
TIEMPO 
GAMA 
PARA
PARA PROYECTO, PARA PROYECTO, 
50 millones 
VIENTO DE 100 M DE 
DE 
A 
PROYECTO,
M509A1 
M509A1 
EN HGT 
EN RG 1 NUDO 
VUELO 
IMPACTO 
M509A1l
MILLAS 
MILLAS 
MILLAS 
MIL METROS 
SEC 
METROS 
MILLAS
45 
1025 
36.4 
11.1 
25,7 
4627 
OA.5
50 
947 
45.0 
10.7 
24.7 
4979 
OA.4
55 
863 
55,8 
10.3 
23.6 
5243 
LO.3
60 
774 
69.2 
9.7 
22.3 
5394 
L0.2
65 
680 
85.1 
9.0 
20.9 
5403 
OA.1
70 
585 
101,5 
8.3 
19,4 
5253 
OA.1
75 
494 
114.1 
7.5 
18.0 
4966 
0.0
80 
417 
118,4 
6.9 
16.8 
4617 
0.0
85 
355 
114,9 
6.4 
16.0 
4279 
0.0
90 
308 
107.0 
5.9 
15.4 
3989 
0.0
95 
271 
97,9 
5.6 
15.0 
3752 
0.0
1 
100 
242 
89.2 
5.3 
14.8 
3563 
0.0
105 
219 
81,4 
5.1 
14.6 
3411 
0.0
110 
200 
74,7 
5.0 
14.5 
3291 
0.0
115 
184 
68,9 
4.8 
14.5 
3195 
0.0
120 
170 
64.0 
4.7 
14.5 
3119 
0.0
125 
159 
59,7 
4.6 
14.6 
3058 
0.0
130 
148 
56.0 
4.5 
14.6 
3012 
0.0
135 
140 
52,7 
4.4 
14.7 
2976 
0.0
140 
132 
49,8 
4.3 
14.8 
2949 
0.0
145 
125 
47.3 
4.2 
14.9 
2930 
0.0
150 
120 
45.0 
4.1 
15.0 
2917 
0.0
155 
115 
42,94 
0 
15.2 
2909 
0.0
160 
110 
40,9 
1.21 
4.0 
15.3 
2907 
0.0
165 
105 
39.1 
1.9 
3.9 
15.5 
2911 
0.0
170 
yo 
99 
1 37,5 
2.4 
3.9 
15.7 
2921 
0.0
170 
-
9 
15. 
2921
175 
95 
36.13.9 
15.8 
_ 
_2931 
0.0
180 
91 
34,9 
3.5 
3.8 
16.0 
2944 
0.0
185 
88 
33,9 
4.0 
3.8 
16.2 Yo 2959 
0.0
190 
85 
33.0, 
4.4 
3.7 
16.4 
2977 
0.0
195 
82 
32.0 
4.8 
3.1 
16.5 
2997 
OA.1
200 
79 
31.1 
5.2 
3.7 
16.7 
3019 
OA.1
205 
1 
77 
30,2 rublos 
5.6 
3.6 
16.9 
3042 
OA.1
210 
74 
29.4 
5.9 
3.6 
17.1 
3066 
OA.1
215 
72 
28,7 
6.2 
3.6 
17.3 
3092 
OA.1
220 
70 
28.0 
6,5 yo 
3.5 
17,5 
3119 
OA.1
* 
225 
69 
27.3 
6.8 
3.5 
17.7 
3147 
OA.1
Figura 31
64
yo 
x 
x1


6x 
EJEMPLO DE TABLA TOTAL 
x
CARGAR 
TABLA A 
FT 8 AÑADIR G 1
1G
ELEVACIÓN DEL CUADRANTE 
PROYECTO, ÉL, M509A1
_FUZE, 
MTSQ, M577
1 
2 
3 
4 
5 
6 
7 
8
.
URCORRECCIONES 
A 
CORR 
CORR A
CUADRANTE 
CORR A 
QUAD ELEV 
PARA BAJO 
DEFL
ELEVACIÓN QUAD ELEV PARA UN INC DE 
NIVEL 
TIEMPO 
GAMA 
PARA
PARA PROY. 
PARA PROYECTO, 
50 millones 
VIENTO DE 100 M DE 
DE 
A 
PROY.
-M509A1 
M509A1 
EN HGT 
EN RG 1 NUDO 
VUELO 
IMPACTO 
M509A1
MILLAS 
MILLAS 
MILLAS 
MIL METROS 
SEC 
METROS 
MILLAS
45 
1025 
36,4 -126,9 
11.1 
25,7 
4627 
OA.5
50 
947 
45,0-136,6 
10.7 
24.7 
4979 
OA.4
55 
863 
55,8-146,5 
10.3 
23.6 
5243 
LO.3
60 
774 
69,2 -154,0 
9.7 
22.3 
5394 
OA.2
65 
680 
85.1 
-153,5 
9.0 
20.9 
5403 
OA.1
70 
585 
101,5-139,8 
8.3 
19.4 
5253 
OA.1
75 
494 
114.1 
-115,4 
7.5 
18.0 
4966 
0.0
80 
417 
118,4 
-89.0 
6.9 
16.8 
4617 
0.0
.7" 
85 
355 
114,9 
-66,8 
6.4 
16.0 
4279 
0.0
90 
308 
107.0 
-50,3 
5.9 
15.4 
3989 
0.0
95 
271 
97,9 
-38,3 
5.6 
15.0 
3752 
0.0
* 
100 
242 
89.2 
-29,6 
5.3 
14.8 
3563 
0.0
105 
219 
81,4 
-23.0 
5.1 
14.6 
3411 
0.0
110 
200 
74,7 
-18.0 
5.0 
14.5 
3291 
0.0
115 
184 
68,9 
-14.1 
4.8 
14.5 
3195 
0.0
120 
170 
64.0 
-11.0 
4.7 
14.5 
3119 
0.0
125 
159 
59,7 
--8.5 
4.6 
14.6 
3058 
0.0
130 
148 
56.0 
-6.4 
4.5 
14.6 
3012 
0.0
135 
140 
52,7 
-4,7 
4.4 
14.7 
2976 
0.0
140 
132 
49,8 
-3.2 
4.3 
14.8 
2949 
0.0
145 
125 
47.3 
-1,8 
4.2 
14.9 
2930 
0.0
150 
120 
45.0 
-0,6 
4.1 
15.0 
2917 
0.0
155 
115 
42,9 
0,4 
4.0 
15.2 
2909 
0.0
160 
110 
40,9 
1.2 
4.0 
15.3 
2907 
0.0
165 
105 
39.1 
1.9 
3.9 
15.5 
2911 
0.0
170 
99 
37,5 
2.4 
3.9 
15.7 
2921 
yo 
0.0
175 
95 
36.1 
2.9 
3.9 
15.8 
2931 
0.0
180 
91 
3.5 
3.8 
16.0 
2944 
0.0
185 
88 
33,9 
4.0 
3.8 
16.2 
2959 
0.0
190 
85 
33.0 
4.4 
3.7 
16.4 
2977 
0.0
195 
82 
32.0 
4.8 
3.7 
16,5 yo 2997 
1LO.1
200 
79 
31.1 
5.2 
3.7 
16.7 
3019 
OA.1
205 
77 
30.2 
5.6 
3.6 
16.9 
3042 
LO 1
210 
74 
29.4 
5.9 
3.6 
17.1 
3066 
OA.1
215 
72 
28,7 
6.2 
3.6 
17.3 
3092 
L0.1
220 
70 
28.0 
6.5 
3.5 
17,5 
3119 
LO 1
225 
t 
-69 
27.3 
6.8 
3.5 
17.7 
3147 
OA.1
Figura 3

0
44 
4
x 
63 
x
% 
-..-. 
-* 
.
• 
J- 
-


* 
x
EJEMPLO DE MESA ROJA
-126,9
-136,6
-146,5
-154.0
-153,5
-139,8
-115,4
-89. 0
-66,8
-50,3
-38,3
-29. 6
-23.0
-18.0
-14.)
-11.0
-8,5
-6.4
-4. 7
-3.2
-1,8
-0,6
|''
1-.
.'.
Figura 32
65
x 
x


TABLA 1
COMANDOS DE CONTROL DE FUENTES
Según lo publicado por el Programa Combinado de Edición y Manuscrito:
Introduzca fuente normal: 
%
Introduzca una fuente neutra: _G 
(Los caracteres que siguen a este comando son
ni negro ni rojo)
Como entrada al programa de composición tipográfica:
Introduzca fuente normal: 
Esn
Introduzca fuente en cursiva: 
esi
Introduzca una fuente neutra: 
esg
9. 
NOTA: 
La letra utilizada en el comando debe estar en minúscula.
ES es el carácter ASCII "ESCAPE"
o.
.6
66


x x
EJEMPLO DE MESA ROJA
-126. 9
-136,6
-146,5
-154. 0
-153,5
-139,8
-115,4
-89.0
-66,8
4. ~ 
-50,3
'N 
-38,3
* 
-29,6
-23.0
-18.0
* 
-8,5
-6.4
-4. 7
-3.2
-1,8
-0. 6
Figura 32
65
x 
x


TABLA 2
CARACTERES NEGATIVOS QUE NO ESTÁN EN CURSIVA
1. NÚMERO DE DOBLE ENTRADA 
EJEMPLO: -12+
Estos se encuentran en las Tablas D y H.
2. SIGNO MENOS USADO COMO GUIÓN 
EJEMPLO: 
Pie 8-J-4
Estos se encuentran en las Tablas A, H y I más los
encabezado de identificación para todas las tablas.
3. SIGNO MENOS SEGUIDO DE MÁS DE 5 CARACTERES
EJEMPLO: 
Consulte la última línea de la columna QE de la Tabla A.
4. CASO ESPECIAL: -1 MIL del encabezado de la columna de la Tabla G.
*J
~S. 
67
%
'...
:: .:4, 
*. 
~ 
* 
4 .
44 
V ~ ~ ~ 
.
* .
~ .
.


TABLA 3
EDICIÓN DE TRANSFORMACIONES EN CARLA*BATCHRUNS.ASCGPSARMY
PERSONAJE(S) DE 
PERSONAJES TRANSFORMADOS PARA
PROGRAMA DE MANUSCRITO 
PROGRAMA DE COMPOSICIÓN 
PROPÓSITO
1 (en la columna 1) 
Avance de formulario (ASCII ADE 12) 
Para asegurar el tipo
(línea 1) 
programa de configuración
comienza una nueva página
ESCAPAR (ASCII ADE 27) 
Para asegurar el "Escape"
o 
el personaje está en
formato de máquina adecuado
4 
2 
Esn (ESCAPE n minúscula) 
Introduzca fuente normal
%S
LÍNEA ARRIBA 
Es3fhuE s4 
Levantar la base de impresión
hasta media línea en el
tamaño de punto actual
LÍNEAS UP5 
Es3fhufhufhufhufhufhufhufhufhufhuEs4 
Levantar la base de impresión
hasta 5 líneas en el
tamaño de punto actual
UP2LINES 
E53fhufhufhufhuEs4 
Levantar la base de impresión
hasta 2 líneas en el
tamaño de punto actual
UPILINE 
Es3fhufhuEs4 
Levantar la base de impresión
arriba 1 línea ii el
tamaño de punto actual
FP 
libra S 
fps 
Letras minúsculas
son necesarios para
comando de composición tipográfica
FP lbV 
Fpv 
Letras minúsculas
son requeridos
68
4-', 
_''.> 
" 
z 
%%%% 
W.


P. °•.
TABLA 3 (Continuación)
PERSONAJE(S) DE 
PERSONAJES TRANSFORMADOS PARA
PROGRAMA DE MANUSCRITO 
PROGRAMA DE COMPOSICIÓN 
PROPÓSITO
FP lb H 
fph 
Letras minúsculas
son requeridos
-GX 
ESgXESn 
Ponga el fiduciario "X" en
fuente neutra y
volver a la normalidad
fuente
F05 
f05 
Letras minúsculas
tamaño de punto requerido
cambiar
F08 
f08 
Letras minúsculas
tamaño de punto requerido
cambiar
F18 
f18 
Letras minúsculas
tamaño de punto requerido
cambiar
donde: 
lb significa un espacio en blanco
NOTA: 
Los comandos de composición tipográfica en minúsculas cuando
precedidos por "ESCAPE 3" están codificados en
GPSDC como fps, fpv o fph "rojo"
".6
ql
" 
69
,-yo


-V 
.
7 
-
7717.%, 
-W
0" 
TABLA 4
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
No.
1 
yo 
! 
exclamación
2 
" 
doble prima
3 .
número o rasguño
4 
$ 
$ 
signo de dolar
5 
% 
signo de porcentaje
6 
& 
& 
signo comercial
7 
apóstrofe o prima
8 
' 
( 
paréntesis izquierdo
9 
paréntesis derecho
10 
.
asterisco
11 
+ 
más
12 
, 
coma
13 
-
-
menos
14 
.
período
15 
/yo 
inclinar/cortar
16 
0 
0 
número cero
17 
1 
1 
numeral uno
18 
2 
2 
numeral dos
19 
3 
3 
numeral tres
20 
4 
4 
numeral cuatro
21 
5 
5 
numeral cinco
22 
6 
6 
numeral seis
23 
7 
7 
numeral siete
24 
8 
8 
numeral ocho
25 
9 
9 
numeral nueve
26 
dos puntos
27 
; 
punto y coma
28 
< 
< 
signo menor que
29 
: 
= 
signo igual
30 
>> 
signo mayor que
31 
? 
? 
signo de interrogación
32 
acento grave
33 
un 
un 
mayúscula a
34 
B 
B 
b mayúscula
35 
c 
c 
c mayúscula
36 
re 
re 
d mayúscula
37 
mi 
mi 
e mayúscula
38 
f 
f 
mayúscula f
39 
GRAMO 
GRAMO 
g mayúscula
4 
10 
h 
h 
h mayúscula
41 
yo 
yo 
yo mayúscula
42 
j 
j 
j mayúscula
43 
k 
k 
k mayúscula
44 
l 
l 
mayúscula 1
45 
m 
m 
m mayúscula
46 
norte 
norte 
uopercase sustantivo, masculino—
47 
0 
0 
o mayúscula
48 
pag 
pag 
p mayúscula
49 
0 
q 
q mayúscula
70
PL-L.

TABLA 4 (Continuación)
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
No.
50 
R 
R 
r mayúscula
51 
S 
S 
mayúscula a
52 
t 
t 
t mayúscula
53 
Ud. 
Ud. 
u mayúscula
54 
V 
V 
mayúscula v
55 
W. 
W. 
mayúscula
56 
x 
x 
x mayúscula
57 
Y 
Y 
y mayúscula
58 
z 
z 
z mayúscula
59 
[ 
[ 
soporte izquierdo
60 
inclinación inversa
61 
] 
] 
soporte derecho
62 
circunflejo
63 
subrayar
641 
comercial en
65 
un 
un 
minúscula a
66 
segundo 
segundo 
b minúscula
67 
c 
c 
minúscula 0
68 
re 
re 
d minúscula
69 
mi 
* 
e minúscula
70 
f 
f 
minúscula f
71 
un 
9 g minúsculas
72 
h 
h 
h minúscula
73 
1 
yo 
yo minúscula
74 
j 
J minúscula
75 
k 
k 
k minúscula
76 
1 
! 
minúscula 1
77 
m 
m 
minúscula m
78 
norte 
norte 
minúscula sustantivo, femenino—
79 
0 
0 
minúscula o
80 
pag 
pag 
p minúscula
81 
q 
q 
q minúscula
82 
r 
r 
r minúscula
* 
83 
3 
un 
minúscula
841 
t 
t minúscula
85 
tu 
tu 
U minúscula
86 
v 
v 
minúscula v
87 
w 
w 
minúscula w
88 
x 
yo 
x minúscula
89 
y 
Y 
y minúscula
90 
z 
z 
z minúscula
91 
{ 
c 
llave izquierda
92 
yo 
barra vertical
93 
j 
} 
aparato ortopédico derecho
94 
" 
-
tilde
97 
rojo! 
barra única izquierda
98 
rojo
"  
' 
media barra izquierda
99 
rojo 
0 
bar sinale riaht
71
|-o-
9,,, 
; 
?. 
, 
.
,. 
.
' 
'- 
,-":""-,".. 
"7...,, 
": 
"" 
'?" 
"'' 
' 
'
" 
""


TABLA 4 (Continuación)
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
No.
100 
rojo $ 
-
guión grueso
101 
rojo% 
yo 
barra completa izquierda
103 
rojo y 
doble enlace a la izquierda
104 
rojo ' 
doble enlace derecho
106 
rojo -
-
guión
107 
rojo ( 
r) intersección
108 
rojo) 
Unión en U de dos conjuntos.
109 
f 
< esquina izquierda/arranque medio izquierdo
109 
rojo [ 
"
110 
) 
> 
> esquina derecha/arranque medio derecho
110 
rojo j
111 
rojo.. 
D implica
112 
rojo 
c 
C implicado por
113 
mi rojo 
3 existe
114 
rojo f 
control de fuente
115 
rojo f 
control de composición tipográfica
116 
rojo b 
11 
símbolo del producto
117 
rojo C 
yo 
símbolo de suma
118 
rojo sustantivo, masculino— 
V 
del/nabla
119 
X roja 
X multiplicado por
120 
rojo Z 
j 
marca de sección
121 
rojo e 
c 
infinito
122 
rojo * 
grado
• 
123 
rojo V 
daga
123 
par S 
rojo m 
t 
"
124 
par 4 
rojo = 
t doble daga
125 
rojo R 
varía directamente como
126 
rojo 8 
flecha hacia arriba
127 
rojo 7 
-- flecha hacia la derecha
128 
rojo 9 
4 
flecha hacia abajo
129 
rojo 6 
.- 
flecha hacia la izquierda
.
130 
rojo h 
una pastilla
131 
rojo 
" 
lógico no
132 
¿rojo? 
* 
gran punto central
133 
rojo yo 
integral
134 
rojo C 
* 
diferencial
135 
rojo 0 
9 
raíz cuadrada
' 
136 
sol rojo 
r 
gamma mayúscula
137 
rojo D 
un 
delta mayúscula
138 
9 
0 
mi 
theta uopercase
139 
rojo l 
un 
lambda mayúscula
140 
rojo j 
-
xi mayúscula
141 
rojo P 
n pi mayúscula
142 
rojo S 
Y 
sigma mayúscula
* 
143 
U roja 
y 
uosilon mayúscula
1144 
0 
0 
0 
phi mayúscula
V', 
145 
rojo Y 
W. 
psi mayúscula
7.
,. 
72
oh 
_. 
..... 
............... 
.
.
.. 
.
.
.. 
.
.
.

TABLA 4 (Continuación)
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
No.
146 
rojo V 
l 
omega mayúscula
147 
rojo un 
un 
alfa minúscula
148 
rojo b 
pag 
beta minúscula
149 
g rojo 
-
gamma minúscula
150 
rojo d 
8 
delta minúscula
151 
rojo e 
mi 
épsilon minúscula
152 
z roja 
C zeta minúscula
153 
h rojo 
'1 
eta minúscula
154 
q rojo 
9 
theta
155 
rojo k 
un 
kappa minúscula
156 
rojo 1 
un 
lambda minúscula
157 
rojo m 
tu 
mu minúscula
158 
rojo sustantivo, masculino— 
V 
nu minúscula
159 
rojo j 
f 
xi minúscula
160 
redp 
ir 
pi minúscula
161 
rojo r 
pag 
rho minúscula
162 
rojo 3 
0 
sigma minúscula
163 
t roja, 
tau minúscula
164 
4 
oh 
phi minúscula
165 
rojo x 
x 
chi minúscula
166 
rojo y 
psi minúscula
167 
rojo w 
oh 
omega minúscula
168 
rojo _ 
0 
caja abierta/metaespacio
170 
rojo m 
no usar
171 
rojo un 
diamante
172 
rojo 1 
doble enlace vertical
173 
rojo = 
aproximadamente igual
174 
T roja 
breve
175 
rojo 2 
• 
punto central
176 
rojo 3 
punto noroeste
177 
rojo 4 
punto norte, este
178 
rojo.
.
punto suroeste
179 
rojo 5 
. punto sureste
180 
rojo + 
diereses/líder de dos puntos
181 
rojo yo 
' 
jota minúscula
182 
rojo tu 
Y 
upsilon minúscula
183 
rojo 0 
-
barra horizontal derecha
184 
rojo: 
-
barra horizontal izquierda
185 
rojo; 
' 
barra vertical alta derecha
186 
un 
un 
esquina superior
186 
rojo <
187 
v 
v 
.
-
esquina inferior
187 
rojo >
188 
K roja 
en reacción reversible
189 
Q roja 
yo 
marca de párrafo
190 
rojo -
macron
191 
rojo 0 
no usar
73


* 
TABLA 4 (Continuación)
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
No.
193 
rojo 
caja con esquinas redondeadas
194 
rojo 
o elipse
.' 
195 
rojo v 
-
equivalente/similar a
257 
par A 
un 
rojo 
A-angstrom
258 
un 
un 
" 
un 
mayúscula un circunflejo
259 
un 
un 
" 
un 
mayúscula una tumba
260 
un 
un 
un 
mayúscula una diéresis
261 
par i 
un 
rojo 
un 
angstrom minúscula
262 
un 
yo 
, 
minúscula un circunflejo
263 
un 
un 
minúscula una tumba
264 
un 
un 
yo 
minúscula una diéresis
265 
mi 
e mayúscula aguda
266 
mi 
£ 
mayúscula e circunfleja
267 
9 
mi 
£ 
e mayúscula grave
268 
mi 
mi 
mayúscula y diéresis
269 
& 
• 
, 
e minúscula aguda
270 
mi 
minúscula e circunfleja
271 
mi 
" 
e minúscula tumba
272 
mi 
mi 
minúscula y diéresis
273 
yo 
yo 
yo 
mayúscula i circunfleja
274 
yo 
[ mayúscula 1 diéresis
275 
£ 
yo 
yo minúscula yo circunflejo
276 
1 
yo 
diéresis i minúscula
277 
0 
0 
mayúscula o circunfleja
278 
un 
0 
0 
mayúscula o diéresis
279 
un 
oh 
un 
minúscula o circunfleja
280 
ao 
minúscula o diéresis
281 
un 
Ud. 
0 
u mayúscula circunfleja
282 
0 
Ud. 
0 
tumba mayúscula u
283 
Ud. 
Ud. 
" 
diéresis u mayúscula
284 
tu 
tu 
minúscula u circunfleja
285 
tu 
tu 
" 
U minúscula u tumba
0 
286 
0 
tu 
" 
1 diéresis u minúscula
287 
c 
c 
c mayúscula cedilla
288 
c 
c minúscula cedilla
--:. 
289 
norte 
norte 
-
R mayúscula y tilda
290 
5 
norte 
-
f 
minúscula y tilda
291 
t 
+ 
± 
más o menos
292 
0 
0 
/ 
0 
danés mayúscula o
293 
6 
0 
o danés minúscula o
294 
re 
c 
/ 
centavo
295 
1 
-
/ 
" 
no igual
297 
-
+ 
dividido por
298 
4 
= 
1 
menor o igual
299 
> 
x 
mayor o igual
300 
yo 
-
es identico
301 
-
-
es congruente
74

TABLA 4 (Continuación)
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
No.
307 
norte- 
quedan tres bonos
308 
4 
-
tres bonos a la derecha
311 
< 
< 
no menos que
312 
> 
> 
no mayor que
313 
$ 
= 
yo 
"no es igual
314 
x 
un 
-
j mayúscula una tilda
315 
un 
un 
-
minúscula una tilda
316 
un 
0 
-
0 mayúscula o tilda
317 
un 
oh 
.9 minúscula o tilda
318 
un 
un 
Una mayúscula una aguda
319 
un 
un 
minúscula y aguda
320 
par e 
c 
rojo 
c mayúscula breve
321 
par 7 
1 
rojo -
un macron
322 
par 2 
2 
rojo 
dos macrones
323 
par 3 
3 
rojo -
tres macrones
324 
par 4 
4 
rojo 
f 
cuatro macrones
325 
par 5 
5 
rojo 
f 
cinco macrones
326 
par 
6 
r" 
. seis macrones
327 
par 7 
7 
rojo -
siete macrones
328 
par 8 
8 
rojo -
ocho macrones
329 
par 9 
9 
rojo -
nueve macrones
330 
par 0 
0 
rojo -
macron cero
331 
yo 
yo 
mayúscula i aguda
332 
11 
yo minúscula yo agudo
333 
1 
yo 
" 
mayúscula i tumba
334 
1 
" 
minúscula i tumba
335 
0 
0 mayúscula o aguda
336 
6 
0 
6 minúsculas o agudas
337 
0 
0 
0. 
mayúscula o grave
338 
6 
oh 
6 minúscula o grave
339 
un 
Ud. 
' 
mayúscula u aguda
340 
6 
tu 
u minúscula u aguda
341 
k 
k mayúscula cedilla
342 
V 
k 
, 
k minúscula cedilla
343 
1 
1 
1 minúscula 1 aguda
3411 
par 1 
1 
rojo * 
| minúscula 1 breve
345 
1 
l 
/ 
L pulido de mayúsculas I
, 
346 
z 
1 
/ 
Yo minúsculas pulimento 1
347 
6 
c 
6 c minúscula aguda
348 
gramo 
-
g minúscula tilda
349 
R 
norte 
N mayúscula aguda
350 
un 
ai 
minúscula n aguda
* 
353 
. cedilla minúscula 3
35 
par i 
z 
rojo " 
punto z minúscula/grado z
-.- 
355 
1 
z 
j minúscula z aguda
356 
par e 
c 
rojo 
Z minúscula c breve
357 
par 1 
gramo 
rojo' 
minúscula q breve
75


TABLA 4 (Continuación)
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
.4" 
No.
358 
9 
k 
tumba g minúscula
359 
pag 
norte 
, 
minúscula n cedilla
360 
par A 
norte 
rojo ' 
Yo minúscula n breve
361 
r 
r minúscula r cedilla
362 
parte 
7 
rojo 
f 
f minúscula r breve
363 
par A 
s 
rojo ' 
yo 
minúscula y breve
364 
t 
, 
t minúscula cedilla
365 
par yo 
z 
rojo ' 
yo 
minúscula z breve
366 
par A 
un 
rojo ' 
£ minúscula a breve
367 
par 6 
mi 
rojo 
. minúsculas y breves
368 
par yo 
un 
rojo -
.1 minúscula un macron
369 
par 8 
mi 
rojo 
yo 
Yo minúscula y macron
370 
par yo 
yo 
rojo- 
Yo minúscula £ macron
'" 
371 
par 6 
oh 
rojo ' 
6 minúsculas o breves
372 
par 0 
tu 
rojo 
un macron u minúscula
373 
parte z 
tu 
rojo " 
grado u minúscula
374 
9 
y 
y minúscula y aguda
375 
0 
un 
4 minúsculas un gancho
"376 
j 
yo 
.Una minúscula que engancho
377 
tu 
m1 gancho u minúscula
376 
mi 
t minúscula e gancho
379 
5 
m 
-
yo 
minúscula m tilda
380 
par 5 
oh 
rojo -
6 minúsculas o macron
381 
yo 
yo 
.rojo 
yo yo minúscula yo breve
382 
par X 
+ 
rojo -
P menos o más
383 
par 6 
rojo e 
j 
épsilon agudo/épsilon principal
384 
par yo 
yo 
rojo 
f 
.i mayúscula grado
385 
t 
r 
r minúscula aguda
386 
un 
un 
d minúscula s aguda
387 
par G 
GRAMO 
rojo " 
macron g mayúscula
388 
parte H 
h 
rojo 
h 
R 
macron h mayúscula
389 
par S 
S 
rojo -
macron con s mayúsculas
390 
parte C 
c 
rojo -
macron c mayúscula
391 
par X 
x 
rojo -
f 
macron x mayúscula
392 
par pies 
norte 
rojo 
un 
minúscula n macron
393 
rojo 5 
rojo 
rojo 5 
... 
diéresis/líder de tres puntos
394 
par E 
mi 
rojo -
, 
mayúscula y macron
395 
par yo 
x 
rojo -
minúscula x macron
396 
parte C 
l 
rojo 
l 
l 
mayúscula 1 macron
397 
parte F 
f 
rojo -
macron f mayúscula
401 
rojo yo 
rojo yo 
rojo 
f 
integral de contorno
402 
par yo 
rojo 
4 
no es un subconjunto de
403 
par yo 
/ 
rojo} 
re 
no está contenido como un subconjunto de
4104 
par 4 
-
rojo ( 
E es un elemento de
405 
par i 
-
rojo 
un 
tal que
106 
parte V 
V 
rojo -
V lógico para todos
yo 
109 
rojo 3 
rojo 3 
rojo \ 
, 
flecha noroeste
76
.
.
.e.e, 
.. 
-"" 
-
'' .
"." 
-',' 
.
"'""""" ," 
.
. "' 
-

TABLA 4 (Continuación)
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
No.
410 
rojo 5 
rojo 5 
rojo \ 
flecha sureste
411 
rojo sustantivo, masculino— 
rojo 4 
rojo / 
? flecha noreste
412 
rojo yo 
rojo.
rojo / 
e flecha suroeste
413 
rojo S 
rojo 8 
rojo 9 
t flecha arriba-abajo
416 
rojo S 
rojo 6 
rojo 7 
'flecha izquierda-derecha
417 
par | 
rojo 1 
triple enlace vertical fU
427 
un 
R 
# 
® 
registrado
428 
1 
c 
# 
derechos de autor
441 
h 
l 
= 
£ 
libra
442 
un 
x 
oh 
moneda
443 
par i 
rojo 
/ 
no idénticamente igual
* 
450 
'abierto 
citar
451 
' 
' 
cerrar cita
452 
par 2 
2 
rojo -
yo bloqueo la mitad
453 
2 
1 
2 
la mitad
454 
14 
1 
4 
V un cuarto
4 
455 
9 
3 
4 
% tres cuartos
456 
3 
1 
3 
% un tercio
457 
un 
2 
3 
% dos tercios
458 
8 
1 
8 
% un octavo
459 
53 
8 
tres octavos
460 
B5 
8 
% cinco octavos
461 
7 
8 
?A siete octavos
462 
1 
6 
una sexta parte
463 
6 
5 
6 
cinco sextos
465 
4 
A. 
un 
mayúscula una cedillaAC
466 
c 
' 
_ 
C mayúscula aguda
467 
mi 
mi 
" 
£ mayúscula y tilda
468 
mi 
mayúscula y cedilla
4 69 
5 
mi 
f 6 minúscula y tilda
470 
par 6 
GRAMO 
rojo' 
0 g mayúscula breve
471 
yo 
yo 
i mayúscula tilda
472 
1 
yo 
-
minúscula i tilda
4 
-
173 
3 
S 
s mayúscula
474 
4 
S 
, 
cedilla mayúscula
475 
un 
Ud. 
" 
mayúscula u tilda
476 
un 
tu 
" 
- minúscula u tilda
477 
z 
z 
z mayúscula aguda
478 
2 
Z2 
tumba con z mayúscula
481 
7 
1 
? 
misterio número uno
82 
2 
2 
? 
misterio número dos
483 
3 
3 
? 
misterio número tres
484 
1 
4 
? 
misterio número cuatro
T..7
t_ 
77
",
.5' .. 
.
.
.
.
. .....


L°77"
-
TABLA 4 (Continuación)
r\-,
Tabla de caracteres del SISTEMA GPSDC
Usando una terminal ASCII extendida 1/77
Símbolo GPSDC 
Piezas 
Nombre
No.
485 
9 
5 
? 
misterio número cinco
486 
6? 
misterio número seis
487 
77 
?misterio 
numero siete
488 
? 
misterio número ocho
489 
? 
9 
? 
misterio número nueve
Los caracteres ASCII con la palabra rojo están precedidos por un escape tres y
seguido de un escape cuatro en un terminal ASCII extendido. 
Símbolos precedidos
por la palabra par se componen de un carácter rojo y uno negro.
Utilice los siguientes caracteres de sobreimpresión sólo con GPSDC.
501 
6 
c
502 
par 2 
? 
rojo
78
,;. 
.*. 
.
". 
.
..
°-b. 
-WM


_ 
yo 
_ 
Yo$.. 
... 
* 
.. 
• 
.
.'. 
-
-
TABLA 5
COMANDOS DE DIBUJO DE LINEAS Y SOMBRA
Según lo publicado por el Programa Combinado de Edición y Manuscrito:
m 
Línea horizontal: 
Es3FP (Ib) H (Ib) ES4 (IB) X,Y; (ii) Espesor; (lb) Longitud
C-
Línea vertical: 
Es3FP (ib) V (1b) ES4 (Ib) X,Y; (1b) Espesor; (libras) Longitud
-
Sombra: 
Es3FP (Ib) S (Ib) FS4 (Ib) X,Y; (1b) Ancho; (ib) Extensión vertical
donde: 
ES es el carácter ASCII "ESCAPE"
X es la horizontal] 
Coordenada del origen de la línea.
Y es la vertical 
medido en 1/10 de punto
"ESPESOR" es el espesor de la línea en 1/10 de punto
"LARGO" 
es la longitud de la línea en 1/10 de un punto
"ANCHO" 
es el ancho de una columna que se va a sombrear
1/10 de punto
"EXTENSIÓN VERTICAL" es la altura de una columna que se va a sombrear
en 1/10 de punto
Como entrada de comandos editados al programa de composición tipográfica:
Línea horizontal: 
ES3 (Ib) fph (Ib) ES4 
Más parámetros anteriores
Línea vertical: 
ES3 (1b) fpv (1b) ES4
* 
Sombra: 
ES3 (1b) fps (Ib) ES4
NOTA: 
En este punto se deben utilizar letras minúsculas.
79
c.
**'qo 
, 
.
.
oh 
-
.- 
.. 
oh 
•. 
.- 
.. 
.c 
.* 
..
•

-
5 
.
-
.
.
* 
*
PV
TABLA 6
5,-:
SECUENCIAS DE ESCAPE ASCII
PERSONAJE SIGUIENTE
'-" 
ACCIÓN TOMADA
ASCII "ESCAPE"
1 
Establecer tabulación horizontal
2 
Borrar tabulación horizontal
3 
Ingrese el carácter gráfico extendido (rojo)
conjunto
-
4 
Dejar carácter gráfico extendido (rojo)
conjunto
5 
Borrar pestaña vertical
6 
Establecer pestaña vertical
7Reversa 
avance de línea (retroceder una línea)
8 
Avance de media línea inverso (haga marcha atrás una
media línea)
9 
Avance de media línea (avanzar media línea)
un 
Ingrese la modificación 1 - caso pequeño
segundo 
Ingrese la modificación 2 - negrita
c 
Ingrese la modificación 3: caracteres elegantes
d o yo 
Introduzca la modificación 4: cursiva
mi 
Ingrese la modificación 5: fuente del encabezado
f 
Introduzca la modificación 6: negrita cursiva
gramo 
Ingrese la modificación 7 - monoancho
h 
Volver a la modificación cero
norte 
Introduzca cara normal (modificación 0)
.
.8
-'. 
80
O0


TABLA 7
PALABRAS DE COMANDO DE FLUJO DE TRABAJO Y SU SIGNIFICADO
PALABRA DE COMANDO 
SIGNIFICADO
DETENER 
Esta es la última carta de un mazo de comandos de edición de formato libre.
para EDBOSS: un editor de archivos GPSDC. "STOP" significa detener la lectura.
ing datos de forma libre. También se reconoce una RUN o EOF.
ARCHIVO 
Esto se utiliza para etiquetar un archivo con un número de identificación.
como en "ARCHIVO" y para indicar si es un archivo "NUEVO"
(uno en el que se escribirán los datos GPSDC), un "VIEJO"
archivo (uno desde el cual se leerán los datos GPSDC), o "ADDON"
(uno al que se pueden agregar datos GPSDC pieza por pieza a lo largo
un período de tiempo). 
Los datos se colocan en la tarjeta de la siguiente manera:
ARCHIVO # NUEVO 
-
Columnas 1-12
Número de identificación -
Columnas 13-16 no requeridas
espacios en blanco 
-
Columnas 19-24
Observaciones 
-
Columnas 25-76
SvMBOL 
Esto cambia el símbolo de comando. 
en EDCARD, EDCHK o en
TARJETAS.
PGOPT 
Opción de programa: el uso depende del programador y del
programa que se está ejecutando. 
Consulte los resúmenes del programa para ver si hay par-
programa particular.
DMPOPT 
Opción de volcado: utilizada por GPSDC*DICX8.BCDUMP. cuando la tarjeta
se lee BCDUMP lee el archivo GPSDC que se está procesando,
convierte cada línea en datos de campo y los imprime.
Las modificaciones de caracteres, es decir, negrita o cursiva, son
no indicado. 
Se anotan los superíndices y subíndices.
si se utiliza la opción de 3 líneas.
Las opciones son: 
0 = Sin volcado
I = Volcado de una línea en la impresora
"" 
2 = volcado con formato FORTRAN activado
unidad de cinta magnética 9
4 = Tarjetas perforadas
0 
8 = Volcado de tres líneas (superíndices
y subíndices indicados)
Los números de las opciones son aditivos, por lo que la opción 9 significaría
Haga ambas opciones, la opción 1 y la opción 8.
81
'Z<


.--.- 
.
.
' 
-
.
: 
.
< 
< 
.
.
* 
: 
.
.: 
.
-,
TABLA 7 (Continuación)
PALABRAS DE COMANDO DE FLUJO DE TRABAJO Y SU SIGNIFICADO
PALABRA DE COMANDO 
SIGNIFICADO
..J-.
CMPDIC 
Permite un cambio en el diccionario de caracteres compuestos en
la mosca. El nombre del diccionario se da seguido de tres
números. Los dos primeros números especifican la primitiva GPSDC.
personajes que se combinarán para crear el nuevo personaje.
El último número proporciona la ubicación del diccionario compuesto de
el personaje a reemplazar.
-
DMPDIC 
Esto permite sustituir un carácter GPSDC por
otro para un volcado de 3 líneas.
LM 
Cambie el valor de Margen izquierdo establecido por el valor en PGLN a un
nuevo valor.
Pestaña 
Establezca tabulaciones en las posiciones indicadas. Hasta 15 separados
Se pueden especificar tabulaciones. Los que no están configurados se colocan
en el margen derecho. Ejemplo: TAB 
5 
10 
15 
20 
25
ALIMENTACIÓN 
Proporciona el número de avances de 1/2 línea por carácter de avance de línea.
Esto establece el número de 1/2 líneas/"línea" impresa. Si no
especificado, el número predeterminado es 3. Esto deja espacio para
subíndices y superíndices.
PGLENG 
Establece la longitud de la página en 1/2 líneas. Un máximo de 239 medias líneas.
se puede utilizar para una página. El formato es: 
PGLENG 1 = 239
o la longitud de las páginas del ARCHIVO 1 es 239 medias líneas.
RTMARG 
Cambia el margen derecho establecido por PGLN a un nuevo valor.
*Ejemplo: 
RM 150: el margen derecho del archivo actual es
150 espacios de caracteres a la derecha del margen izquierdo.
UNIDAD 
Actualmente no se utiliza.
-
RM 
Mismo significado que "RTMARG".
LF 
Configure el avance de línea en 1/2 líneas para cada archivo individual. 
puede
utilizarse al copiar de un archivo GPSDC a otro.
Ejemplo: 
LF 1-2 -el 
El avance de línea para el ARCHIVO 1 es igual a
Oh, 
dos medias líneas.
82
-4--p-.
;

[pag. 
-o- 
.
.
.
....
*.
TABLA 7 (Continuación)
PALABRAS DE COMANDO DE FLUJO DE TRABAJO Y SU SIGNIFICADO
PALABRA DE COMANDO 
SIGNIFICADO
PGWDTH 
Ancho de página especificado por número de caracteres horizontales
espacios. El ancho máximo es 230. Ejemplo: 
PGWDTH 1=150 -
el ancho de página para el ARCHIVO 1 es de 150 espacios. 
el fisico
El tamaño de la página se establecerá según el tamaño en puntos del
personajes.
NUEVO 
Se utiliza con la tarjeta FILE para designar un archivo vacío en el que
Se escribirá la información del GPSDC.
VIEJO 
Se utiliza con la tarjeta FILE para designar un archivo GPSDC existente.
hace que se compare el título del archivo en la tarjeta
el título del archivo real.
0
COMPLEMENTO 
Se utiliza con la tarjeta FILE para designar un archivo GPSDC existente para
qué nuevos datos GPSDC se pueden agregar - el programa en realidad
lo copia en un nuevo archivo y luego agrega los nuevos datos GPSDC.
ENTRADA 
Designa el archivo de entrada que está activo. Hasta 4 entradas
Se pueden designar archivos, pero sólo uno puede estar activo a la vez.
tiempo dado. Se utiliza para cambiar un activo existente (predeterminado)
designación del archivo.
FUERA 
No usado.
ARCHIVO 
Mismo significado que ENTRADA.
OTFILE 
Designa el número del archivo de salida -
el archivo del cual
Se leen los datos GPSDC
CORRER 
Esta tarjeta marca el final del mazo de datos de formato libre. encendido
Univac una tarjeta @EOF tiene el mismo efecto.
DOMFIL 
Esto designa la lima dominante, es decir, aquella cuyo
0* 
Se utilizarán los parámetros. Se utiliza cuando hay más
más de un archivo GPSDC y permite que los parámetros de un archivo
aplicarse a un archivo diferente. Por lo tanto, el ARCHIVO 1 podría ser
activo pero si DOMFIL 2, entonces los parámetros del archivo 2 serían
ser utilizado para el ARCHIVO 1.
83
1 
-
1
" 
.
II
yo 
yo 
-
.
"1 
yo 
yo
!
yo 
1
1
1 
-
'.= 
' 
-, 
-
norte 
.
* 
.
-.
- " 
. * 
=N,%yo


TABLA 7 (Continuación)
PALABRAS DE COMANDO DE FLUJO DE TRABAJO Y SU SIGNIFICADO
PALABRA DE COMANDO 
SIGNIFICADO
PGNUM 
Establece el número de la primera página del archivo GPSDC.
BBNUM 
Establece el número de bloque de libro predeterminado. 
(Nota: 
esto no puede
exceder los 244 libros.)
glutamato monosódico 
Esto imprime un mensaje.
MISC 
Una tarjeta de "elección del programador" para composición tipográfica. el uso en
CARLA*BATCHRUNS. STRIPLINEOT es:
1. Número de archivos de entrada
2. Tamaño del punto
3. Ancho en caracteres o picas
4. Profundidad en personajes o picas
5. Espaciado entre líneas (conductor delta). 
debe ser
presente cuando 4. no es cero.
PARAM 
Tarjeta de parametrización cuyo significado varía según el
gramo con el que se usa. Tal como se utiliza en el programa de composición tipográfica:
PARAM 2=1. 
El registro de entrada ASCII debe tener un carro
-. 
retorno, avance de línea insertado al final de cada
registro.
PARAM 2=0 
Archivo EDTEXT
84
c.
c.
co.o
C- 
-- 
-
o° 
CC 
.--.- 
.--


.
.
.
.
.
.
.
.
.. -
.
, 
.
-
•  
, 
°
.ov
TABLA 8
SECUENCIAS DE COMANDOS DE FLUJO DE TRABAJO UTILIZADAS POR EL PROGRAMA DE COMPOSICIÓN
SECUENCIA 1 
UBICACIÓN: CARLA*BATCHRUNS.ASCGPSARMY
.
*MISC 
0 8 
39 
60 
0
*OTARCHIVO 1 
*PARÁMETRO 2=0
%" 
*ARCHIVO 1 NUEVO 
ARCHIVO ASCII UNIVAC TRANSFORMADO EN GPSDC
*TABLAS 
5 
10 
15 
20 
30 
40 
50 
60 
80 
100
ARCHIVO 1 NUEVO 
EJÉRCITO DE MESSIN 30-12-81 
CARLA*BTEXTO.
*PARÁMETRO 2=1
*CORRER
EXPLICACIÓN: 
Los números de tarjeta varios (MISC) son leídos por
DSDG*GOGPO.STRIPLINEOT. El primer número es el número.
de archivos de entrada
el segundo es el tamaño en puntos de la impresión
el tercero es el ancho de página en PICAS
el cuarto es la profundidad de la página en PICAS
el quinto es el espaciado entre líneas
..- 
SECUENCIA 2 
UBICACIÓN: 
DSDG*VIDBLOCK.SETHELVTIMES
*INFILE 1 
*DMPOPT 0
*CORRER
8 8 
60 
200 
2 
112 
1 1 
8000 
0 
112
EXPLICACIÓN: 
*INFILE 1 - DATOS LEÍDOS DEL GPSDC FILE1
*DMPOPT 0 - NO HACER UN VOLCADO DE BCD (PROGRAMA: GPSDC*DICX8S.BCDUMP)
*CORRER 
- ESTO TERMINA LA DECK DE DATOS DE FORMATO LIBRE
-,
.
85
4 
m

TABLA 8 (Continuación)
SECUENCIAS DE COMANDOS DE FLUJO DE TRABAJO UTILIZADAS POR EL PROGRAMA DE COMPOSICIÓN
* 
TARJETA DE DATOS: 
DATOS LEÍDOS POR GPSDC*DICX8S.CARDS Y PASADOS A
DSDG*VIDBLOCK.VID500MAIN EN FORMATO 1615
POSICIÓN DE DATOS 
USO
1 
Tamaño de puntos de carácter
2 
Tamaño de la mina en puntos (tamaño del cuadro en el que cabe el personaje)
3 
Espacio mínimo entre caracteres (en unidades)
4 
Espaciado máximo (unidades). Si se llama un personaje
que no está en los diccionarios, un espacio de este ancho
reemplaza al personaje.
.
5 
Número de espacios consecutivos que configuran una tabulación.
6 
Ancho de carácter (unidades)
7 
Conmutador de opción para DSDG*VIDBLOCK.VIDPRT
Significado: 1 - Imprimir el primer y último registro en GPSDC
archivar y hacer una cinta
0 - Imprime todos los registros y crea una cinta.
-1 - Imprime todos los registros y no graba ninguna cinta.
" 
8 
Número de la primera página impresa
9 
Número de la última página posible (hacer más grande que la última)
número de página real previsto)
10 
Puede usarse para identificación de trabajo. Normalmente no se utiliza.
e. 
11 
Monoancho (unidades). 
Si está presente, esto causa que todos
los caracteres serán monoancho con el ancho especificado.
o.
s. 
86


.
TABLA 9
LA ESTRUCTURA DEL PGLN
Está definido el uso de casi la totalidad de las 120 celdas del PGLN. son usados
para aquellos elementos que PARCHK y EDCHEK no pueden configurar directamente. uno importante
La restricción es que los parámetros del archivo no se pueden cargar en ISTATE hasta después de
se ha abierto un archivo. Las rutinas de apertura eliminan ISTATE.
UBICACIÓN 
USO
1-40 
Editar la página del programa y los números de línea
4. 
41-55 
Números varios - para cualquier uso
56-59 
Iniciar archivos de números de bloque de libros 1-4 (para archivos de salida).
Normalmente se establece en 1. El programa de apertura del archivo de salida también
-* 
suministra 1, en ISTATE (3,ARCHIVO).
61 
Editar programa, EDKTRL. Almacena el número correspondiente a un
comando de edición específico: 
subs, escribir, etc.
62 
Editar programa, MULT. El número de pares de números de línea de página.
para este comando. 50 = "A TRAVÉS"
63 
Editar programa, cambio de comando. 
Comando = 0, Texto = 1
66-69 
Números de página inicial, archivos 1-4 (para archivos de salida).
Normalmente se establece en cero aquí y también por la apertura del archivo.
programa. Corresponde a ISTATE (2,ARCHIVO).
70 
Editar programa. Interruptor de salida de usuario.
71-74 
Avance de línea, archivos 1-4. 
Se deben proporcionar los valores predeterminados.
Transferir a ISTATE (19,ARCHIVO).
75 
Editar programa - control de paginación. 
SEGUIR = 1,
IGNORAR = 0. Sólo es necesario durante la fase de mazo de datos de orden aleatorio.
76-79 
Parámetros 1 a 4. Cualquier uso permitido.
* 
• 
80 
Entrada de máquina de escribir: 
margen izquierdo (Normalmente = 1)
81-95 
Entrada de máquina de escribir: 
Tabulaciones
96 
Entrada de máquina de escribir, margen derecho (valor de anulación de suministro
aquí!)
87


-
° 
oh 
-*
TABLA 9 (Continuación)
LA ESTRUCTURA DEL PGLN
UBICACIÓN 
USO
-
97 
Entrada de máquina de escribir: 
cambiar = 1 si alguna palabra 80-96 es
cambiado.
100 
Cambio de mensaje = 1 si el mensaje BCD está construido
101 
Archivo de entrada: 
valor actual
102 
Archivo de salida: 
valor actual
103 
Opción de programa
104 
Interruptor END = 1 si PARCHK reconoce "RUN" o "STOP"
105 
Cambio de comando = 1 si se ha cargado un valor en PGLN
que no sea un comando Editar programa (1-40, 61-63), un
entrada de máquina de escribir (80-97) o un mensaje (100).
106-9 
"Archivo dominante". 
Establecer = 1 para un archivo de entrada que se va a
-
controlar el ancho de la página de salida. Utilizado por PREPLN.
Normalmente establecido = 0.
111-114 
Archivos de ancho de página 1-4 (archivos de salida). 
Suministro predeterminado
valor.
116-119 
Archivos de longitud de página 1-4 (archivos de salida). Suministro predeterminado
valor.
8
l88

TABLA 10
MATRIZ DE PARÁMETROS DE LÍNEA DE CÓDIGO DE IMAGEN DEL DOCUMENTO (ESTADO)
La matriz ISTATE (24, 5) es una matriz maestra en la que los parámetros de un
Se almacenan las líneas del DIC. La segunda variable es ARCHIVO, por lo que se pro-
proporcionado. Los cuatro primeros normalmente están asociados a unidades de entrada-salida. 
el
La quinta columna es una columna de almacenamiento temporal; su contenido puede cambiarse mediante
cualquier subrutina. Un programador no debe esperar que sean iguales después de haber
transfiere el control a alguna rutina que no ha escrito.
El uso de varias palabras en cada columna está prescrito
1. Estado del archivo (establecido por rutinas de entrada/salida. Debe ser examinado por
rutinas que llaman a las rutinas de E/S).
2. Número de página
3. Número de bloque de libros
4. Ancho de página (coordenada X máxima)
5. Longitud de página (coordenada Y máxima, en medias líneas)
6. Tipo de línea (presencia de superíndices, subíndices, modificación y
líder resumido aquí para texto de línea. Modo de texto esquemático
indicado si aplica.
7. Longitud del texto en biframes (bytes de 16 bits). 
esta es la corriente
longitud. 
Cambia si los espacios en blanco se comprimen mediante una rutina.
8. Número de línea
9. Coordenada Y "antigua"
-salida. Siguiente intervalo de media línea disponible
-entrada. Valor asociado con la línea anterior leída
10. 
Coordenada Y "nueva"
-salida. Ese valor asignado a esta línea.
-entrada. Ese valor encontrado asignado a esta línea.
-
11. 
Señal de sufijo de línea
Registra el número de biframes en la línea además del texto,
según estas reglas:
0 sin material adicional
2 si uno (o ambos) el biframe de edición (12) o el diagnóstico
biframe (13) no son nulos y no hay otros bytes presentes
89


TABLA 10 (Continuación)
MATRIZ DE PARÁMETROS DE LÍNEA DE CÓDIGO DE IMAGEN DEL DOCUMENTO (ESTADO)
>2 Si un sufijo no estándar, es decir, material distinto del
byte de edición y diagnóstico, está presente, entonces el valor es
la longitud del sufijo no estándar más 2.
12. 
EDITAR BYTE
Valor nulo 255/255
Este biframe es utilizado por programas de edición para indicar que el
Se editó una línea en particular. Pueden aparecer dos símbolos DIC primitivos.
almacenado. Se prefieren las letras mayúsculas -ase.
13. BYTE de diagnóstico
Valor nulo 127/127
un. 
Esta es una palabra de almacenamiento de bits, cada bit transmite cierta información.
sobre problemas de entrada/salida. Los bits se derriban para indicar su uso.
El programador ocasional no debe utilizar este byte.
14. 
Soporte derecho
15. 
Longitud de la cuerda
Esta palabra tiene varios significados en diferentes puntos de un programa. eso
puede registrar la longitud total de la línea, incluidos todos los corchetes, texto y
sufijo, como en la salida. Puede totalizar el texto y lo no estándar.
sufijo, como para una línea devuelta por el programa de entrada. Su valor
después de una llamada a CMPRS es la longitud del texto que se ajustará al
ancho de página deseado (4, arriba).
16. 
Indicador de verificación de operación
Esta es una palabra de error de entrada/salida, cada bit del cual almacena errores
información de un tipo particular. Está determinado por las rutinas que
* 
leer y escribir registros DIC.
17. 
Interruptor de uso general
Este es un cambio poco a poco. Cambie sólo la broca en cuestión.
Bit 1. Cero si no hay espacios en blanco comprimidos en línea. 1 si está comprimido
hay espacios en blanco. Configurado por entrada/salida. debería ser
establecer si las líneas son generadas por un programa.
Bit 2. Cero si la línea está dentro de una página. 1 si la línea
debe escribirse como la última línea de una página. 
(Fuerzas
.
paginación por programa de salida).
90
-
-- 
w-
ir-- 
-- 
-- 
-
-
-
-
--- 
-. 
-
--- 
-.- 
-
-
'b 
y 
-
.
.
... 
.

TABLA 10 (Continuación)
MATRIZ DE PARÁMETROS DE LÍNEA DE CÓDIGO DE IMAGEN DEL DOCUMENTO (ESTADO)
Descripción de ISTATE (1, Archivo)
un 
b 
c
A. Posición en una página. Indica lo que hizo la acción de E/S anterior.
0 indefinido
1 en un espacio entre páginas
2 corchetes de página de inicio reconocidos
3 indefinido
4 en un espacio entre líneas de una página (pero no después de la primera línea)
5 después de la última línea de una página
6 en el espacio después de la primera línea de una página
7 solo una línea en la página (combinación de 1, 2 y 4)
B. Archivos de salida
0 cerrado o inexistente
,: 
1 extremo del remolque del carrete detectado (cabezal de escritura colocado después)
" .2 
después de una etiqueta de avance de fin de archivo
3 después de un final de marca media
* 
4 abrir y procesar
'Yo..
"-'" 
C. Archivos de entrada
0 cerrado o inexistente
1 extremo del remolque del carrete detectado (es necesario colocar el cabezal más allá)
.4 
2 lectura del final del archivo (es necesario colocar el cabezal más allá)
* 
3 en (después) de la marca de la cinta
4 abrir y procesar
.4 .
-"" 
91
-. 
' 
%.. 
4 
1 
'Un.. 
..
TA 
V2. 
~ 
~ 
, 
% 
% 
4 
4a* 
~ 
.
~. 
4
4. 
Yo.* 
k'~%~ 
''ah..


TABLA 10 (Continuación)
MATRIZ DE PARÁMETROS DE LÍNEA DE CÓDIGO DE IMAGEN DEL DOCUMENTO (ESTADO)
". 
18. 
No usado
19. 
Avance de línea
Almacena el interlineado normal actual de un archivo, medido en 1/2
líneas de línea principal a línea principal. 
"Doble espacio" = 4, etc.
20. Reservado para uso de CMPRS
Registra el ancho de página requerido para manejar la línea de texto proporcionada.
a CMPRS. Compara 15.
21. 
Unidad lógica utilizada para este archivo.
22. Conmutador de tipo de línea anterior, anteriormente conocido como KSBSW.
Es =1 si había un subíndice o un inicio en la línea anterior y
=0 si no. 
(Este cambio influye en la ubicación de la siguiente línea. 
Ver
discusión sobre las coordenadas Y.)
rw..
4.
.
' :" 
92


-q, 
.
.
... 
j 
.
~.*~~. 
W -
..
TABLA 11
CÓDIGOS GPSDC ESPECIALES PARA TIPOGRAFÍA
m 
Especial (;Códigos PSDC para composición tipográfica
l 
La palabra GPSDC se divide en ocho bits superiores e inferiores llamados LOFRNI y HIFRM. cuando el
LOFRM es 
tampoco. 96. 250 o 253, el HIFRM contiene comandos de composición tipográfica específicos.
HIFRM 
LOFRM
yo 
96 
espacio sin ancho en la tipografía.
n>2 
96 
espacio de tamaño n en unidades tipográficas.
1 
250 
espacio de DSPACE 
en unidades tipográficas.
X>2 
250 
hace que la siguiente información aparezca en pestañas
_, 
.
para posicionar CONTAR+X. Posición
es CHARID*PTSIZE* (COL'NTL+X)
desde el margen izquierdo.
yo a 36 
253 
establezca el tamaño del punto en este número.-'.
83 
253 
establecer una pestaña en esta posición en la tipografía
84 
253 
cursor de tabulación a la posición establecida por (83-253)
85 
253 
mueve el cursor hacia arriba en la página la mitad de la actual
que conduce hacia la parte superior de la página.
86 
253 
centrar el personaje que sigue sobre el
personaje precedente.
87 
253 
disminuir el contador COUNTL 
por uno.
Se utiliza para crear personajes COMPUESTOS.
88 
253 
mueve el cursor hacia abajo en la página a
distancia de un cuarto del tamaño del punto.
89 
253 
mueve el cursor hacia arriba en la página a
distancia de un cuarto del tamaño del punto.
90 
253 
rotar la página para que la página sea más ancha
que largo.
91 
253 
restaurar la página a la rotación adecuada. es decir
la página es más larga que ancha.
92 a 99 
253 
el número de puntos del espacio 
(0-7)
para colocar entre líneas. línea de 8 puntos en
La ventaja espacial de 10 puntos tiene 2 puntos de
espacio entre líneas.
.
151 a 199 
253 
cambio temporal en el número de puntos de
espacio (0-48) que se colocará entre líneas.
Para insertar un GPSDC 253 en un archivo ASCII para ser procesado. el tablero del operador, iESC3)fxx(ESC4)
donde xx es un número entero de dos dígitos. Entonces el 0-86-253 de la tabla COMPOSITE se convierte en 1ESC3)f86(ESC4. en un formato ASCII
terminales. El ESC es el código de escape ASCII.
,93
'pag
piK.. 
%5.-.%55**.., 
.-
*.~**** 
S

-) 
0 01 
r
0) 
(o 
0 
di*'-
U) 
za 
4-) 
.4- 
Ud.
o4. 
UU. 
centímetros
4- 
a) 
o 0 
S
I-4- 
OWQ 
4-
'S4.) 
0 o- 
un 
00
t 
4.- 
lui 
=yo 
di 
-
U)~( 
.CU 
c
yo 
lui 
d) 
4-) 
4.) 
TV4J 4-)
cmer 
-
r_ 
P)
lui 
.0 
c 
S -
0) 4J 0
gato 
a 
_tu 
_ r 
tío
Ud. 
~ D4..T2-0 
4.
tú 
tu 
CL 
-r- 
tu
V)yo 
IA 
11C)
S- 
_ 
.4-3
a) 
LU 
0 
'- 
Ud. 
4-3U 
re 
c 
4.)
4.) 
CD 
un 
P)4) 
-
-
.
d.
LM 
ro 
LU 
c 
c 
4- 
4-)3Wd
S 
S.- 
cc 
-0u 
-
Ud.
r o 
-~ Yo.- 
) 
a 
*.- 
UIC.
4C) 
.
/ 
4-1 
CA 
c 
4) 
S.. 
-d4- 
centímetros 
x
Ud. 
c 
4-3 
r o 
03- 
a 
re
CU 
re 
Li.. 
s. 
)- 
1=04-- 
0 
4.)
4- 
di 
a) 
S 
yo- 
LC) 
S 
r_
4- 
.0 
o) 
a 
.0 
0 
-(di 
0 
+.3
V 
0 
4-) 
0. 
.0 
4- 
0C- 
c.. 
(1
4LUJ 
4- 
CC) w.. 
CA 
a 
>) 
c 
0 
0 
U) 
0L
2: 
0 
F-I- 
0 
(0 
4-' 
0 
todia) 
du 
mi
'S-144.) 
$- 
c 
*-dto 
.c 
-0 
Los Ángeles 
0
CAU) 
0- 
a 
ra 
r_ 
4o 
Ud. 
-) 
>) 
tu
-0 
OCV) 
a) 
_r_ 
:0 
w 
yo 
~ 
t 
0
c) 
.j 
-CD 
S.. 
Ud. 
4.) 
S.. 
4-) 
c 
-
r_ 
a)
-4 
LUJ 
a) 
(un 
qo 
(1) 
1 4 
m 
D- 
4-) 
4.)
(0 
4-3 
(Un 
tu 
0- 
U) 
o-F
*LU 
yo- 
4- 
CA( 
tu 
0) 
U) 
:" 
U)' 
'U 
4 
S..
..J 
LU- 
LUJ 
ES. 
S.. 
a 
0 
4-)-0 
*o 
cr 
-e- 
yo
L* 
1- 
LU 
a) 
X< 
a) 
& 
'4.) 
.1- 
.1- 
4- 
c
uC F 
)- 
4-' 
4-) 
r_ 
CC.") 
.) 
0L S- 
(A-
(1 
C) Ud. 
Ud. 
0 
Ud. 
.
) 
~ 
Ud. 
oh 
0- 
4- 
chi 
4-'
tu- 
m 
w ' 
tz 
M: 
uj 
di ( 
..j 
0 
m~C 
Ud.
4-' 
r5di 
a 
tú 
~-- 
yo 
M. 
0D. 
UA 
G.J.
co- 
c 
.
C-- 
0. 
l 
-4)yo 
4)
C~~ 
m ~ 
Ud. 
LAUU) 
Ud. 
C- 
4.) 
0CL~
-.-
4 .3 
4-) LLJ 
-
toC 
r_ 
0 
(C
dU) 
c 
.- 
re 
z 
C.-d 
di 
0S-.
4'~(2 
r- 
yo- 
a) 
-ea 
-
c 
-
c
C o 
LUC./) 
4-) 
> 
di 
(2 
L- 
3W 
-03 
4-) 
0 
-0 
-C
01). 
C/LUJ 
c 
34-) 
centímetros 
CC 
(1) 
Ud.
CD) 
4-) 
c..) 
4) 
S- 
4. 
-
~ 
14-' 
a ' 
4-' 
--
CD 
C_ 
'c 
norte 
a) 
2E 
Ud. 
re 
0 
du 
a 
-- 
u)3
di) 
CL0 
.
c-di 
0 
0 
di 
4-)c: 
4 4-4)0 
m 
"
lui 
:3 
-C)U 
Ud. 
U- 
uro 
mi 
t
4. 
)d 
0 
c 
a 
0 
~4-3 
a) 
t--
yo- 
a) 
U- 
di) 
01 
--.
' 
4-' 
0 
4-' 
4-
U)a 
4- 
(un 
~ 
a- 
ta 4- a 
c 
:3 
0
yo- 
Ud. 
0 
l 
0. 
r_ 
VC 
) 
S.-
.0
c 
j 
.
j 
:-:p 
4- 
udi) 
tod 
yo 
(3 
1 -
a)
=D 
re 
-) 
a) 
oye 
di 
0- 
0..C4-) 
0. 
.3 
un 
4-J
4.3 
L.- 
c 
0~~*. 
-
~ 
Ud. 
-
1 
)
S 
luc/ 
(Un 
CL 
0 
a 
0) 
c 
W4-3 
a) 
r_~
0 
c 
-- 
04-' 
a ti 
Cr_
yo 
d) 
CrN_ 
4-' 
~ .- 
-
mi 
x 
4-) 
ci
un. 
a) 
S-aA 
a 
C0>-o~
a 
.'JCA.cr
U) LU0 
ciu
-
~ 
4- 
V) 
uj
4tuo 
CLU 
a 
LUJ 
LU 
cc
tu 
<-PCC 
4.) 
C: 
tu- 
Cu 
m-C.
televisión 
.. jV) 
-0 
LO 
LUJ 
C-) 
0 
a0- 
-
LU J
4J 
t 
r-4 
LUJ 
< 
V) 
Los Ángeles 
:9 
CD-
a 
4- 
LI.. 
-. 
r14 
Q- 
LU 
V) 
< 
LU 
yo
* 
-
0 
V) 
-4 
V 
-
a_ 
yo-0- 
o.
~LUL 
CC 
V) 
LUJ 
U- 
<C
di 
-
m ~ 
yo- 
V) 
CC 
un 
un 
c 
0yo 
-
>- 
m
Yo- 0- 
-
c 
-
norte 
CC 
... 
L.) 
zC 
c)
C- 
0 
CC 
LU 
LU- 
California 
< 
-
><C
a0- 
en 
c) 
c 
-
C- 
Ud. 
mi
5' 
94
% 
.
.
.


RD-A147 588 
MANUAL DEL PROGRAMADOR DEL PROGRAMA DE COMPOSICIÓN ELECTRÓNICA 
2/ 2 .
~(U) 
CENTRO DE INVESTIGACIÓN Y DESARROLLO DE ARMAMENTO DEL EJÉRCITO
PROVIN DE RBERDEEN.- 
JH WHITESIDE ET AL. AGO 84
SIN CLASIFICAR ARBRL-R- 
79 OSE-D-F388 488 
F/G 14/5 
Países Bajos
zammmaaaa/z


L-0
ll 
Lm0 
111l202
11111.!2 
1111J
enfermo1.
un, 
MICROCOPIA 
RESOLUCIÓN 
PRUEBA 
GRÁFICO
NACIONAL 
OFICINA DE NORMAS- 
1963-A
.
.
.,.
.1*.

* 
TABLA 13
LISTADO DE CARLA*BATCHRUNS.CUTMARK
CARLA*BATCHRUNS(L)I.CUTMARK( 1)
@FOR, S DSDG*VIDBLOQUE. VID500MAIN, VIDSOOMAIN
-8
DATOS (ROJO(I),I-1,17)/183.172.175.176.177.179.129.127.126.128.150,
1 115.153.156.169.161.182/
PARCHE C PARA AÑADIR VIÑETAS PARA FACILITAR EL CORTE AUTOMÁTICO DE PAPEL EN GPO
CARLA MESSINA MAYO 1978
-105,111
C MUEVE EL BORDE DE LA PÁGINA DE GIRO A 24 PUNTOS DE LA PARTE SUPERIOR DE LA PELÍCULA PARA FACILITAR EL CORTE DEL PAPEL
SI (ITURN .EQ. 0) VAYA A 157
CI(M-4)-52
TEMPERATURA-0
CI(M-2)-24
157 
LLAMADA HEXBYT(TEMPIC(M-1),IC(M))
-123
C PON DOS GRANDES BALAS ENTRE LAS PÁGINAS PARA AYUDAR AL CORTADOR DE PAPEL AUTOMÁTICO
LA PÁGINA DE PASO C NO TENDRÁ VIÑETAS
SI (ITURN .EQ. 
1) IR A 156
C PÁGINA DE SALIDA NORMAL
* 
PT-PTSIZE
TAMAÑO-18
MODFI-;7
SINFRN-132
TEMPLI 
10*ANCHO-160
TEMP- 50*PLENG -800
M=M+3
C ESPACIO ADELANTE HASTA EL FINAL DE LA PÁGINA
CI(M-2)-70
LLAMADA HEXBYT(TEMPIC(M-1),IC(M))
LLAMAR A CARCAL
C AVANCE HASTA EL FINAL DE LA PÁGINA
M-M+3
CI(M-2)-76
4" 
LLAMADA HEXBYT(TEMP1, IC(M-1), IC(M))
M-M+3
CI(M-2)-70
LLAMADA HEXBYT(TEMPIC(M-1),IC(M))
0 
LLAMAR A CARCAL
C Pestaña VOLVER A LA ESQUINA SUPERIOR IZQUIERDA
M-M+2
- "-
IC(M-1)-81
IC(M)-O
• • 
M=M+ 2
CI(M-1)-85
0 
IC(M)-O
PTSIZE-PT
156 
CONTINUAR
"-' 
-129
C PESTAÑA AL INICIO DE LA PÁGINA
M-M+2
CI(M-1)-85
IC(M)-O
C AVANZAR 10 PUNTOS
MM+3
CI(M-2)-76
95
A. 
o.A 
~ 
J.~h 
un 
.
.


-.
,. 
°. 
* 
.
*- 
4
TABLA 14
Códigos de comando Videocomp 500
maleficio 
decimales 
Nombre 
bytes 
une 
Observaciones
10 
16 
ID de trabajo 
2
11 
17 
Fin del registro 
ninguno
12 
18 
ignorar
13 
19 
considerar
14 
20 
Seleccionar directorio de fuentes 
3
15 
21 
Seleccione el directorio de cadenas 3
18 
24 
RADRU 
8
.\ 
24 
36 
Recuperación de fuentes 
2 
ID de fuente (0-999) Subconjunto (0-5)
+2 
Tamaño de punto de 1/10 puntos
25 
37 
Ancho del conjunto de fuentes 
2 
1/10 punto
26 
38 
romano 
ninguno
27 
39 
oblicuo 
1 
grados 
ángulos de 617.
28 
40 
monofuente 
ninguno 
todos los espacios = 1 em
29 
41 
Microfuente 
ninguno 
todos los espacios = 
tamaño
2C 
44 
Guardar cadena 
1 
número de cadena = 0-3
+n 
cadena a guardar, termina con
extremo de la cuerda
2D 
45 
Ejecutar cadena 
yo
-
2F 
47 
Cadena final 
ninguno
30 
48 
Definir página 
2 
puntos 
Ancho diagonal <81 picas
cara completa 
+2 
puntos 
Largo diagonal< 81 picas
31 
49 
Definir página 
2 
puntos 
Ancho< 70 picas
-. 
línea por línea 
+2 
puntos 
Largo <124 picas
33 
51 
Página final 
ninguno 
Requerido
oh 
34 
52 
Definir área Ubicación 
2 
puntos
" 
35 
53 
Definir área Ubicación 
2 
puntos
y girar 900 
+2 
puntos
36 
54 
Definir área Ubicación 
2 
puntos
y rotar 1800 
+2 
puntos
• 
37 
55 
Definir área Ubicación 
2 
puntos
a., rotar 2700 
+2 
puntos
96
"J' 
'' 
, ,""" , ";. 
" 
,-"" 
-
-
""""" 
-
.*' 
.-
~ .
" 
S." "; -. .','. 
". .-- ',','-2, 
"" 
'.


*1
2
TABLA 14 (Continuación)
Códigos de comando Videocomp 500
* 
maleficio 
decimales 
Nombre 
bytes 
une 
Observaciones
-
40 
64 
Espacio Básico 
ninguno 
36/100 de em actuales
41 
65 
em espacio 
ninguno 
Función del conjunto de fuentes actual wdt
-
42 
66 
en el espacio 
ninguno 
de una em
* 
43 
67 
Espacio delgado 
ninguno 
h de una em
44 
68 
Ejecutar espacio de usuario 
ninguno
.
46 
70 
Espacio hacia adelante 
2 
1/50 punto
47 
71 
Espacio hacia atrás 
2 
1/50 punto
48 
72 
Definir espacio de usuario 
2 
1/50 punto
49 
73 
Espacio entre letras 
2 
1/50 punto puesto a cero después del final de cada
linea
4C 
76 
avance 
2 
1/10 punto
4D 
77 
revertir 
2 
1/10 punto uso solo en modo cara completa
4E 
78 
arriba 
2 
1/10 punto < 72 puntos
4F 
79 
abajo 
2 
1/10 punto < 72 puntos
50 
80 
Definir horizontal 
1 
Pestaña no. 
0-256
pestaña N 
+2 
1/50 punto con respecto al límite izquierdo
* 
51 
81 
Mover a horizontal 
1 
'Ficha no.
pestaña N
52 
82 
Guardar pestaña horizontal N 
1 
Pestaña no. 
posición horizontal actual
54 
84 
Definir pestaña vertical N 
1 
Pestaña no. 
0-256
+2 
1/10 punto respecto al inicio de la página
55 
85 
Mover a la pestaña vertical N 
1 
Pestaña no.
55 
85 
Guardar 
pestaña vertical N 
1 
Pestaña no.
•56 
86 
Guardar pestaña vertical N 
1 
Pestaña no.
* 
60 
96 
Definir horizontal 
1 
identificación
regla norte 
+2 
1/10 punto 
altura de la regla
+2 
1/10 punto 
duración de la regla
yo 
9
••• 
97
4.
soy

TABLA 14 (Continuación)
Códigos de comando Videocomp 500
maleficio 
decimales 
Nombre 
BT 
Unidades 
Observaciones
.1 
97 
Establecer regla horizontal N 
1 
a
-2 
98 
Definir vertical 
1 
identificación
regla norte 
+2 
1/10 punto de altura de la regla
+2 
1/10 punto de ancho de regla
63 
99 
Establecer regla vertical N 
1 
I0
64 
100 
Establecer regla 
2 
1/10 punto de altura de la regla
+2 
1/10 punto de ancho de regla
70 
112 
Llenar un personaje 
1 
identificación
a pestaña horizontal N 
+1 
Char.
72 
114 
Llenar un personaje 
2 
1/50 punto
a posición intermedia +1 
carbón
74 
116 
Llenar dos personajes 
1 
identificación
a pestaña horizontal N 
+2 
Caracteres.
76 
118 
Llenar dos personajes 
2 
1/50 punto
a posición intermedia +2 
Caracteres.
98


TABLA 15
UNIDADES DE MEDIDA TIPOGRAFÍA Y VIDEOCOMP
ESPECIFICACIONES DE LA PÁGINA
.1 
UNIDADES DE MEDIDA:
un. UNIDADES VIDEOCOMP (FOTOGRAFÍA) -
Unidades adimensionales utilizadas
para expresar los tamaños relativos de los caracteres
B. PUNTOS 
72 puntos = 1 pulgada
c. PICAS 
1 pica 
= 12 puntos
TAMAÑOS DE PÁGINA DEL VIDEOCOMP: 
Tamaño de página estándar (42 PICAS de ancho x 62 PICAS de alto)
o 504 puntos x 744 puntos)
Tamaño máximo de página 
550 puntos de ancho x 790 puntos de alto
FÓRMULAS PARA EL TAMAÑO DE LOS CARACTERES:
2400 x (PICAS/LÍNEA)
NÚMERO DE CARACTERES/LÍNEA = (TAMAÑO DEL PUNTO) X (ANCHO DEL CONJUNTO DE ENTEROS)(UNIDADES)
ANCHO DE CARÁCTER (UNIDADES)
PUNTOS/CARACTER 
= AVANCE (EN PUNTOS) X 
200
'99
re
ot
," 
99
-S


oh 
4-) 
4
interfaz de usuario 
U- 
x 
oh 
un 
t
0-4 
< 
4- 
0)
(AZI 
(1
-.
=Z0 
cu
LU 3LI0 
0 
CA 
(un
ECL 
%- 
4-)
w 
LI
03 
Lu 
re
6- 
0 
0
LU0 
codi 
>.C..
= 
loco 
un
es 
03. 
o.
LL. 
CDL.) 
mi
06 
II 
ser 
-0 
4-JF
....3 
Ud. 
yo 
0- 
LA-
0
-JO 
.
co 
CD
yo- 
l 
41. 
4-) 
identificación 
0 
(
) 
.
0 
ci 
0
co 
cou( 
x0 
1
C~ 
P4.. = 
oh 
) 
G0O 
.
0t 
4.. 
4J COL. 
Ud.
LL 
S- 
c 
-
cmW tu
CDL 
LI 
ll.l 
r_ 
r_. cu 
C-
zZf 
LI 
4-0 
X0J- 
r
UE 
0 
tu tu 
c 
.. 
C- 
4- 
.0
-
CVX 
yo.. 
(. 
.
0 
CD 
a- 
.CL 
.
CD 
*tú( 
S -
0 televisión
llj 
4 
oC 
-
0 
4- 
r_() 
'
.
oh 
4- 
LI 
r= 
c 
.03 0)
CL 
03 
un ~ 
0 
~ 
3:C
o 0,1- 
baño 
S.- 
r-~ 
0 
C0 
C4-
IJ 
0 
4- 
M. 
P) 
S- 
CC 
SU
U-3 
o4 
yo 
00- 
4-) 
Ud. 
a)-r_0
r-0 
.r' 
.,-.a 
c 
S 
4-)C.
2c'4 
0A 
4- 
0- 
(un- 
C0
c) 
03 
CL 
un 
como
.0t 
0 
yo- 
0 
3 
-
4..)
Los Ángeles. 
a 
s. 
4J 
Ud. 
un 
4
*L 
4) 
0r4- 
4-) 
.QL) 
0JC1)
.Q 
L)CO 
=4r 
1 
0 
l 
0'0 
LIC
Un.. 
=) 
tú 
o) 
LI 
0a 
c 
r 
Ud.
GRAMO 
c) 
.j 
0~r 
4)- 4.-) 
1 
4) 
LI- 
O4-
~~L4 
c 
)Yo'- 
0 
0 
0 
CL
educación física 
0 
0 
5 
5
OL 
MC 
LI 
.0 
..
oh 
-l
-zr* 
4- 
4 
l 
CO 
.c 
.
un. 
La.J 
CA 
L")yo 
yo
LI 
41X 
0P 
0 
z
Z~4 
LI 
.
Ud.
C)~L 
a 
l
% 
LII 
c 
P-4 
LI 
CD
%~~ 
~Un 
UEUU 
:< 
t 
li 
L- 
U-
metro-Z: 
< 
c
c 
U0. 
-j 
0 
0-CL 
un 
LIJ
LA- 
LJ 
LU) 
(D 
LODCD 0 
l
100


TABLA 17
CAMBIOS REQUERIDOS EN LA SALIDA DE ARMYCARDS
1. Retire la línea: 
DATOS (COMPOS(I), I = 1, 3)/ y su continuación en
la siguiente línea. Esto se encuentra debajo de la parte inferior del último ITAB.
mesa.
2. Elimine todas las líneas siguientes: DATA ICMPRS, NEND / 567, 569/.
3. Convierta las tablas LOOK1 en tablas bidimensionales. No alteres el
Declaraciones LOOK(2,1) o LOOK(3,I) DATOS. Las tablas LOOKI se convierten
buscando cada instrucción DATA (LOOK11(I) y cambiándola a DATA
(MIRAR(1,I). El saldo de estas líneas de DATOS permanece inalterado.
4. La salida ARMYCARDS modificada se coloca en un archivo llamado DSDG*VIDBLOCK.
HELVTIMES.
5. Se coloca una declaración END al final de HELVTIMES.
6. Compile HELVTIMES y guárdelo como DSDG*VIDBLOCK.HELVTIMES.
101

0 
.
TABLA 18
LA TABLA DE DATOS DSDG*VIDBLOCK.HELVTIMES
JUAN BLANCO
1:C 
LABORATORIO DE INVESTIGACIÓN BALÍSTICA CAMPO DE PRUEBAS DE ABERDEEN
2:CARLA MESSINA NOV 1979 HELVETICA CON PÚAS ROMANAS CURSIVAS ROMA(NUEVE)
3:C 
NO SE NECESITA UNA TABLA WV YA QUE TODO EL TRABAJO DEL EJÉRCITO ES DE MONANCHO
4: 
BLOQUEAR DATOS
5: 
COMÚN /VID500/ ICFPRS,NEND,LOOK(3512),ITAB(1500)
6: 
DATOS (MIRAR(2,I),I-I,512)/512*O/
7: 
DATOS (MIRAR(3,I),I-1,512)/512*0/
8: 
DATOS (MIRAR(1,I),I-1,180)
9: 
1 1,5,6,7,11,15,19,20,24,28,
10: 
2 32,34,38,40,44,48,52,56,60,64,
11: 
3 68,72,76,80,84,88,92,96,97,98,
12: 
4 99,-103,103,107,111,115,119,123,127,131,
13: 
5 135.139.143.147.151.155.159.163.167.171,
14: 
6 175,179,183,187,191,195,199,203,207,-208,
15: 
7 208,209,-210,210,211,215,219,223,227,231,
16: 
8 235.239.243.247.251.255.259.263.267.271,
17: 
9 275.279.283.287.291.295.299.303.307.311,
18: 
A 315.316.317,-318,3*0.318.319.320,
19: 
B 323.324.325.326.327.328.331.332.333.334,
20: 
C 335.336,-337,2*0.337.338.339.340.341,
21: 
D 342,343,344,345,346,347,348,349,350,-351,
22: 
E 0.351.352.353.354.355.356.357.358.359,
23: 
F 360.361.362.363.364.365.366.367.368.369,
24: 
G 370.371.372.373.374.375.376.377.378.379,
25: 
H 380,381,382,383,384,385,386,387,-388,0,
26: 
1 388.389.390.391.392,-393,4*0,
27: 
DATOS(MIRAR(1,I),I- 181, 410)/
28: 
1 393,394,-395,2*0,395,396,397,398",-399,
29: 
2 3*0,399,400,-401,4*0,
30: 
3 56*0,401,402,403,404,
31: 
4 405.406.407.408.409.410.411.412.413.414,
32: 
5 415,416,417,418,419,420,421,422,423,424,
33: 
6 425.426.427.428.429.430.431.432.433.434,
34: 
7 435.436.437.438.439,-440.441.442.443,
35: 
8 444,-445,8*0,
36: 
9 445.446.447.448.449.450.451.452.453.545,
37: 
Un 455.456.457.460.461.462.463.464,
38: 
B 465.466.467.468.469.470.471.472.473.474,
39: 
C-475,475,-476,0,476,477,478,479,480,481,
40: 
D-482,0,482,483,484,485,486,487,488,489,
41: 
E 490.491.492.493.494.495.496.497.498.499,
42: 
F 500.501.502.503.504.505.506.507,-508.508,
43: 
G 509.510.511.512.513.514.515.516.517.518,
44: 
H 519,520,521,524,525,526,527,-528,2*0,
45: 
Yo 528.529.530.531,-533,2*0.533.534/
46: 
DATOS(MIRAR(1,I),I- 411, 512)/
47: 
1 535.536.537,-538,0,538.539,-540,2*0,
48: 
2 6*0,540,541,-542,0,
49: 
3 10*0,
50: 
4 542,-543,7*0,543,
51: 
5 546,-549,549,550,551,552,553,554,555,556,
52: 
6 557.558.559,-560,-561,3*0,
53: 
7 2*0,561,-562,2*0,562,-563,2*0,
54: 
8 32*0/
102

TABLA 18 (Continuación)
LA TABLA DE DATOS DSDG*VICBLOCK.HELVTIMES
55: 
DATOS(ITAB (1),1- 
1, 80)/
56: 
1 6986039920, 7288029840, 8932196640, 7355138720,13429933040,
57: 
2 21038067314,15040447088,15074001552,13496942880,15141110432,
58: 
3 26851541616,26885096080,26918650144,26952204960,18258330224,
" 
59: 
4 19097191056,20204486944,19164299936, 6719013872, 8597832304,
60: 
5 8899822224, 9470247200, 8966931104, 8597865072, 9168290448,
61: 
6 9470279968, 9235399328,13427541362,13463290512,13496844576,
62: 
7 13530399392,15038841458,13495337250, 6983877232, 7017431696,
63: 
8 7017398928, 7050952992, 7084507808,13429146224,13462700688,
64: 
9 7017398928, 7050952992, 7084507808,13429146224,13462700688,
65: 
Un 13496254752,13529809568,15038153328,15071707792,13494649120,
66: 
B 15138816672,15038186096,15071740560,13494681888,15138849440,
67: 
C 15038218864,15071773328,13494714656,15138882208,15038251632,
68: 
D 15071806096,13494747424,15138914976,15038284400,15071838864,
69: 
E 13494780192,15138947744,15038317168,15071871632,13494812960,
70: 
F 15138980512,15038906994,15071904400,13494845728,15139013280,
71: 
G 15038382704,15071937168,13494878496,15139046048,15038415472/
72: 
DATOS(ITAB 
(yo),- 
81.160)/
73: 
1 15071969936,13494911264,15139078816,15038939762,15072002704,
74: 
2 13494944032,15139111584, 6986007152, 7019561616, 7053115680,
75: 
3 7086670496, 6983910000, 7017464464, 7051018528, 7084573344,
76: 
4 26849444848,26849313776,26849412080,13694829168,15338996368,
77: 
5 11077583136,15406105284,17991500400,19367232144,18327044384,
78: 
6 19434341024,17991533168,18830394000,18058641696,18897502880,
79: 
7 18528436848,19098862224,19669287200,19165971104,19065340528,
80: 
8 19367330448,21279932704,19434439328,17454760560,17488315024,
81: 
9 19132481824,17555423904,16381051504,16146170512,17253466400,
82: 
A 16213279392,20676051568,20441170576,21011595552,20508279456,
83: 
B 19333907056,19367461520,21861934688,19434570400, 7254344304,
84: 
C 8361640592,11079549216, 8428749472,13428621936,14804353680,
85: 
D 12690424096,14871462560,17992057456,19367789200,19938214176,
86: 
E 19434898080,15039300208,16415031952,18596069644,16482140832,
87: 
F 22555525744,22320644752,25306988832,22387753632,19602768496,
88: 
G 19367887504,22058796128,19434996384,20676543088,20710097552/
89: 
DATOS(ITAB 
(1),1- 161, 240)/
90: 
1 20206780704,20777206432,16918479472,17220469392,15911846176,
91: 
2 17287578272,20676608624,20710163088,20206846240,20777271968,
92: 
3 19334464112,19368081576,20743749920,19435127456,17455710832,
93: 
4 17220829840,15106900256,17287938720,16392001776,16952427152,
S 
94: 
5 17791287584,17019536032,19066389104,19099943568,20744110368,
95: 
6 19167052448,17455809136,18294669968,18596659488,18361778848,
96: 
7 24972934672,25810895504,25844449582,25878004384,17187439216,
97: 
8 18831606416,18328289568,18898715296,17724342896,18026332186,
98: 
9 18328322336,18093441696,16919069296,16415752848,18865226061,
99: 
A 16482861728, 7520977458, 7521010226,13428458864,26848331088,
* 
100: 
B 14768177776,15070167696,13491309024,15137276576,15036646000,
101: 
C 16412377744,13493141792,16479486624,13962936944,15070233232,
102: 
D 11345690912,15135342112,15036711536,16680878736,14566949152,
.
103: 
E 16747987616,15036744304,15607169680,11345756448,15674278560,
104: 
F 8057455216, 9970057872, 8929870112,10037166752,14768374384,
105: 
G 16412541584,12687999264,16479650464,15036842608,16144138896,
* 
106: 
DATOS(ITAB 
(I),1-241, 320)/
107: 
1 14298644768,16211247776, 5641634416, 7017366160, 7319355680,
108: 
2 7084475040, 5910332016, 7286063760, 6782746912, 7353172640,
109: 
3 13694993008,15070724752,14835843360,15137833632, 6178833008,
103
.
.
-
,. 
, 
.. 
.'....'.',. 
,** 
.' 
, 
.
.%- 
V 
V......%.% 
*-% 
-
.• 
_-%, 
-, 
,*' 
. " 
-' 
"

TABLA 18 (Continuación)
LA TABLA DE DATOS DSDG*VIDBLOCK.HELVTIMES
110: 
4 701769384j, 7856554272, 7084802720,22284993136,23660724880,
111: 
5 22352101664,23727833760,15037268592,16144564880,14567506208,
U112: 
6 16211673760,15305736816,16949904016,12420055328,17017012896,
113: 
7 15037334128,16413065872,12956959008,16480174752,15037366896,
114: 
8 16413098640,12956991776,16480207520, 8863384176,10775986832,
115: 
9 10272669984,10843095712,13427081840,14534378128, 9467658528,
116:
117: 
ESTE DATO CONTINUA POR UN TIEMPO
118:
171: 
DATOS (ITAB(I),1- 
567, 
569)/
'V172: 
DATOS ICNP&S,NEND /567, 
569/
174: 
FINAL
DSDG*VIDBLOCK(1) .HELVTIMES( 1)
.10


TABLA 19
ARCHIVOS NECESARIOS PARA EJECUTAR EL PROGRAMA DE COMPOSICIÓN
CARLA*BATCHRUNS.
GPSDC*DICX8.
GPSDC*DICX8S.
DSDG*GOGPO.
TARJETAS DSDGk.
DSDG*V BLOQUE ID.
EXP*RLIB$.
PROCESO DE TEXTO*L IB.
5105


TABLA 20
COMANDOS PARA CAMBIAR EL TAMAÑO DEL PUNTO Y REPOSICIÓN DEL CURSOR
Cambio de tamaño de punto:
A. Deje el tamaño de puntos INICIO para el comando NUEVO tamaño de puntos como lo publicó
Programa combinado de edición y manuscrito.
Es3FNNEs4
donde: 
ES es el CARÁCTER ASCII "ESCAPE"
NN es el tamaño en puntos al que cambiar. 
Se deben llenar ambas N.
pulg. El tipo de ocho puntos sería "08".
Comando como entrada al programa de composición tipográfica
Es3fNNEs4 -
La transformación de "Es3F" a "Es3f" lleva
colocar en CARLA*BATCHRUNS.ASCGPSARMY
Ejemplo: 
Es3F18E 4 - Cambiar al tipo de 18 puntos
B. Regresar al tamaño de puntos de INICIO
E 3FXXE 4 - donde "XX" es el tamaño en puntos de INICIO
S 
S
NOTA: 
Al regresar al tamaño de puntos INICIO desde el tamaño de puntos NUEVO, el
El cursor baja una línea en el tamaño de punto NUEVO. esto debe
ser compensado.
C. Movimiento del cursor horizontal:
*- 
Cuando se vayan a colocar NUEVOS caracteres de tamaño en puntos en una línea, muévase hacia arriba
desde las marcas fiduciales inferiores (o la línea inferior en tamaño de punto INICIO)
usando los comandos de movimiento vertical. 
Cambiar al NUEVO tamaño de puntos
y luego espacie horizontalmente hasta la ubicación del primer personaje; poner
ese personaje y seguir adelante. 
Cuando todos los caracteres en la línea tienen
apagado, cambie nuevamente al tamaño de puntos HOME. No olvides con-
Pensar en la caída vertical del cursor de una línea después de volver a
CASA. Recuerda también que los espacios se miden en la nueva mina.
tamaño (si el tamaño del punto y el tamaño de la mina son diferentes).
-.
0
!z 
.]'.106
yo"
', 
-"_ 
-. -. "- 
* .'"A~m 
-
* 
V 
,V, 
'V2"' , - ;'' 
,' '.- 
* 
' ' 
.'C .
... .
'.... ""'- 
"""""""€"""' " 
, - :'


TABLA 20 (Continuación)
COMANDOS PARA CAMBIAR EL TAMAÑO DEL PUNTO Y REPOSICIÓN DEL CURSOR
Ejemplo: 
Es3F18Es4 lob 0 13b 1UP1LINEEs3FO8Es4
donde: 
b significa espacios físicos en blanco que quedan en la imagen de la tarjeta
de la línea.
Explicación: 
El tamaño del punto HOME en el ejemplo es 08. Al principio
Al finalizar la línea, cambie al tipo de 18 puntos. Espacio terminado
10 espacios en blanco de 18 puntos desde el margen izquierdo y sacar uno
18 puntos cero. 
Mueva 13 espacios en blanco más de 18 puntos y
saca un "uno". 
Compensar el movimiento vertical del cursor.
luego regrese al tamaño de puntos de INICIO.
D. Movimiento vertical del cursor:
LÍNEA ARRIBA -
Mueva el cursor hacia arriba media línea según lo medido en la corriente
tamaño de plomo.
UPILINE 
-Mover el cursor hacia arriba una línea completa en el tamaño actual del cliente potencial.
UP2LINES 
- Mueva el cursor hacia arriba dos líneas completas en el tamaño actual del cable.
LÍNEAS UP5 
- Mueva el cursor hacia arriba cinco líneas completas en el tamaño actual del cliente potencial.
Ejemplo: 
Mueva el cursor hacia arriba 81 líneas en el tamaño de cliente potencial actual
UP5LINESUP2LINESUP1LINEUPHALFLINE
NOTA: 
NO se permiten espacios entre los comandos o dentro
ellos.
E. Estrategia:
Cuando se van a utilizar dos tamaños de puntos en una página, escriba la página completa
en el tamaño de cable HOME. Subir desde la parte inferior de la página en tamaño INICIO,
cambie al NUEVO tamaño de puntos para la línea en cuestión, apague el carácter
actores requeridos, corregir el movimiento vertical del cursor, cambiar a
tamaño HOME y muévase verticalmente nuevamente.
NOTA: 
Los comandos de cambio de tamaño de puntos y los comandos de movimiento del cursor deben
ser el último dato en una página, incluso después de la línea y la sombra
comandos.
También al planificar la ubicación de personajes de gran tamaño, tenga en cuenta que
el ancho en monoancho de un carácter de 18 puntos es 10,08 puntos
horizontalmente. Para localizar la posición horizontal de un tamaño grande
107

TABLA 20 (Continuación)
COMANDOS PARA CAMBIAR EL TAMAÑO DEL PUNTO Y REPOSICIÓN DEL CURSOR
carácter, encuentre el número de espacios de 8 puntos desde la izquierda
borde de la mano será, luego multiplique por 4.48/10.08 = .4444 para
obtenga el número de espacios de monoancho de 18 puntos para espaciar.
Elimina fracciones de un punto, no redondees. 
Recuerda también
que el borde izquierdo de la mesa está a 16 espacios de 8 puntos de
borde izquierdo de la página.
FÓRMULA: 
Para calcular el número de caracteres (espacios en blanco) a espacio,
También se puede utilizar la siguiente fórmula:
-O-F HRCTR:[DISTANCIA DE PÁGINA (PULGADAS)][200]
.- '*,iNO. 
DE PERSONAJES:
[PILOTO (PUNTOS)][ANCHO DE CARACTERES (UNIDADES)]
72
108
4'-
.- 
-
'. 
--
, 
.'. 
entonces
c. 
* 
*' 
** 
oh


REFERENCIAS
1. Blanton C. Duncan, "Representación completa en texto claro de datos científicos
Documentos en formato legible por máquina", Oficina Nacional de Normas Técnicas.
cal Note 820, Departamento de Comercio de Estados Unidos, febrero de 1974.
2. "Catálogo de colores de impresión estándar para cartografía, gráficos y geodésicos
Datos y productos relacionados", Agencia de Cartografía de Defensa, Centro Topográfico,
Washington, DC, julio de 1972.
3. Robert C. Thompson, "Código de usuario de documento científico de uso general".
norte: 
Manual." Oficina Nacional de Normas, inédito, diciembre de 1981.
4. Robert C. Thompson, "Programador de códigos de documentos científicos de uso general".
Manual", Oficina Nacional de Normas, inédito, abril de 1982.
109
Maul"Ntoa ueuo0tnadupbihd 
pi 
92


5'.
0
.4'
~. 
..-
.5
* .4--
.4-..
5,
5'."
un
APÉNDICE A
ENTRADA DE TECLADO DE ENTRADA DE COMPOSICIÓN
55.4.4*
*~.1
S
-. 5
0.
5'.
.4.
111
.4,
.1
.5.
-
-'. 
....................
~ 
-
~


CONTENIDO DEL APÉNDICE:
A. Introducción
B. Entrada de caracteres
1. Entrada
2. Conjunto de caracteres
3. Visualización de caracteres
C. Formato de prueba
1. Introducción
2. Centrar texto
3. Enrasado a la derecha
4. Párrafo
5. Espaciado
6. paginación
D. Formato de tabla
1. Configuración de la mesa
2. Tabulación
E. Controles de composición tipográfica
1. Antecedentes
2. Parámetros de formato
3. Comandos internos de composición tipográfica
F. Ejemplo de texto complejo
S1',
-0
.


TECLADO 
APÉNDICE A
ENTRADA DE TECLADO DE ENTRADA DE COMPOSICIÓN
A. INTRODUCCIÓN
Aunque el Programa de composición tipográfica electrónica está especialmente configurado para procesar formatos fijos
entrada para tablas de disparo, conserva la capacidad de procesar entradas de formato libre heredadas de la NBS
Sistema tipográfico. Los métodos para hacer esto se detallan en las siguientes secciones.
B. ENTRADA DE CARÁCTER
1. Entrada
El archivo de entrada Typesetting ASCII puede estar en formato fijo o en formato libre. un fijo
archivo de formato, como el creado por el Programa Combinado de Edición y Manuscrito, sólo
requiere que el Programa de composición tipográfica electrónica traduzca los datos de entrada a formato tipográfico
comandos. La entrada en formato libre requiere que el Programa coloque la entrada en un estado final editado
antes de traducirlo a comandos de composición tipográfica.
La forma más flexible de crear un archivo de entrada de formato libre es con una impresión ASCII.
terminal con desplazamiento de cinta roja y negra, medio espacio hacia adelante y rotación de plataforma inversa.
Sin embargo, cualquier terminal ASCII que permita un retroceso sin eliminación y la entrada de
Se pueden utilizar secuencias de escape.
2. Conjunto de caracteres
aa. 
Personajes básicos
El carácter de escape ASCII se representará como 9. Hay noventa y cinco caracteres.
agregado imprimiendo el conjunto original con cinta roja. La secuencia 03 indica un cambio a
cinta roja, y 04 un cambio a cinta negra. Los caracteres rojos normales son GPSDC.
números 97-195 con las excepciones indicadas en la Tabla 4. No es necesario que haya un
desplazamiento de la cinta, pero ayuda a facilitar la comprobación de la entrada.
Ejemplo: una alfa griega (a) es 03aO4.
B. Personajes sintéticos
Se pueden crear caracteres tipográficos adicionales colocando un carácter ASCII (rojo
o negro) encima de otro usando un retroceso (1).
Ejemplo: un signo de división (-) es :b- o -14: El orden no es importante.
Los caracteres que no se utilizaron cuando se diseñó GPSDC se agregaron con el uso de un
conjunto de caracteres "elegantes". Este conjunto de caracteres se ingresa con ic. Un On vuelve a la fuente normal.
La combinación de estos métodos de extensión de caracteres genera aún más caracteres.
.
Ejemplo: mayor o igual que (

) es > = pero oc> b=On da .
115


,'0
3. Visualización de caracteres
Todos los caracteres se pueden cambiar de tres formas básicas: modificación, nivel de línea y
sustitución.
a. Modificación
V..
v. 
Cualquier carácter GPSDC se puede modificar para su visualización de una de ocho maneras. un personaje
no se puede modificar de dos maneras simultáneamente, es decir, negrita y monoancho
Las modificaciones no se pueden utilizar para el mismo personaje al mismo tiempo. las modificaciones
disponibles son:
Modificación 
Ejemplo
Normal (romano) 
un
Personajes pequeños 
un
Negrita 
un
fantasía 
Q(
cursiva 
un
Encabezado en negrita 
un
Negrita cursiva 
un
monoancho 
un
Ejemplos de estas modificaciones en tres tipos de letra diferentes (Times Roman, Bodoni,
y gótico) se muestran en la Figura 20. Estas modificaciones no deben confundirse con una
fuente tipográfica. Una vez que se elige una fuente en particular, sus ocho modificaciones son
disponible para su uso. Las dos formas de provocar un cambio en la modificación se muestran a continuación:
Modificación 
Comando 
Comando alternativo
Normal (romano) 
13Fn04 
0n
Personajes pequeños 
03Fa4 
oa
Negrita 
f3Fb4 
segundo
fantasía 
63Fc04 
oc
cursiva 
63FiW4 
li
63FdL4 
re
Encabezado en negrita 
03Fe&4 
e,
monoancho 
03Fg,4 
1g
La modificación de cursiva también se puede invocar subrayando el texto y la negrita.
modificación sobreimprimiendo el texto con circunflejos rojos. Estos dos últimos métodos
funcionan sólo cuando el texto básico está en modificación normal.
116


B. Nivel de línea
.A-
El nivel de línea es literalmente el nivel de una línea donde se muestra un carácter. esto es
llevado como una de las tres partes de un personaje GPSDC: el personaje en sí, el
modificación y el nivel. Los cuatro niveles disponibles son:
Código 
Descripción
0 
línea principal (carácter de tamaño completo)
yo 
superíndice (2/3 del tamaño del carácter de la línea principal)
2 
subíndice (2/3 del tamaño del carácter de la línea principal)
3 
subíndice bajo superíndice
Nota: nunca se permite que el tamaño en puntos sea inferior a 5
El código supone que el primer carácter imprimible es un carácter de línea principal.
Los caracteres subsiguientes pueden ser línea principal, superíndice o subíndice. Los comandos para
alterar el nivel de línea son:
Comando 
acción
08 
Mover el siguiente carácter hacia arriba 1/2 línea desde la posición actual
09 
Mover el siguiente carácter hacia abajo 1/2 línea desde la posición actual
Ejemplos: 
Crear comandos tipo C9: C69908
Crear C.' escriba comandos: - CO9a8081+ 0
o: C08 +16099a08
Nota: todas las modificaciones pueden estar presentes en cualquier nivel.
c. Sustitución de personajes
El juego de caracteres sofisticado se puede utilizar para introducir caracteres que no se encuentran en el modo normal.
conjunto de caracteres. Esto se hace redefiniendo los caracteres GPSDC en términos de fuente Videocomp.
personajes. Este proceso se trata en el apartado V.D. de este informe. Un GPSDC "L" para
El ejemplo podría definirse como el símbolo del rayo en la fuente Fancy. Entonces, cada vez
Se necesitaba este símbolo, un cambio a una modificación Fancy, una "L". y un regreso a la normalidad
la modificación lo apagaría.
-11
.0
- .' 
117
.5,

C. FORMATO DEL TEXTO
1. Introducción
La mayoría de los sistemas de edición de texto utilizan un conjunto simple de comandos para darle al texto la forma deseada.
forma. Las subrutinas del Sistema de composición tipográfica han sido diseñadas para aceptar formato de texto.
Comandos de tres sistemas de edición NBS: RUNOFF, EDTEXT y ATS. Sólo
Los comandos de estilo EDTEXT se describirán aquí.
Los comandos de formato EDTEXT comienzan en la columna uno de una línea con "Control a" (si), el
ASCII Carácter de control de inicio del rumbo. El texto afectado por el comando comienza en el
siguiente línea hacia abajo.
2. Centrar Texto (Atuc)
La instrucción ituc se utiliza para centrar cada una de las siguientes líneas de texto. Sigue vigente
hasta que uno de los siguientes comandos lo desactive: Atu, itur o %tf. Estos comandos son
descrito más adelante.
Antes de realizar el cálculo de la longitud de la línea para los espacios en blanco de centrado, iniciales y finales
se eliminan de la línea y los espacios internos se vuelven uniformes (espere un solo ancho entero
espacio entre palabras sin importar cuántas hubiera originalmente).
La línea está centrada en el ancho de página establecido por el parámetro de formato tres en la tarjeta *MISC.
*Ver 
Consulte la Tabla 7 y la sección del Apéndice sobre parámetros de formato para obtener más información sobre este tema.
parámetro.
3. Color a la derecha (itur)
El comando itur establece las líneas subsiguientes al ras del margen derecho usando el ancho establecido por
parámetro de formato tres. Se eliminan los espacios en blanco iniciales y finales y se eliminan los espacios internos.
procesado antes de realizar el cálculo. El comando lo desactiva Atuc, itf o Atu.
4. Párrafo (dtf)
el comando 
tf comienza la formación de párrafos. Los párrafos se pueden describir mediante
cuántos espacios tiene sangría la primera línea y hasta qué punto el resto de las líneas del párrafo
están sangrados. Los párrafos terminan con Att, ittu, Xtuc, itur o At+n, o un cambio de línea.
.
~ 
-sangría. 
Los párrafos de bloque deben estar separados por comandos "(' ya que no hay cambios en
sangría de línea.
5. Espaciado (it + n)
*'Oh" 
El comando de espaciado tiene la forma t+n donde "n" es un número entero. #t+0 se utiliza para
párrafos separados. En + I inserta un espacio entre líneas. Se calcula el tamaño del espacio.
agregando el parámetro de formato dos (tamaño en puntos) al parámetro de formato 5 (número de puntos a insertar)
entre líneas) y multiplicando el resultado por "n". El espaciado es independiente de todas las demás "i".
comandos.
• 
6. Paginación (es+ 99)
El comando para iniciar una nueva página es (t +99). La página será tan larga como el formato
parámetro cuatro (profundidad de página) o acortarlo con el comando t+ 99, lo que ocurra primero.
r.11
Ud. "" 
1 1 8
U.."
..
, 
.%- 
Ud. 
-
.'

D. FORMATO DE TABLA
1. Configuración de la mesa
El comando para hacer tablas es Xtu. Las tablas se ingresan línea por línea. Entradas adyacentes en
Las columnas deben estar separadas por al menos dos espacios. Cuando el comando de formato de tabla es
Dado, cada línea se lee de izquierda a derecha. Cuando dos o más espacios consecutivos son
encontrado en una línea, el programa calcula dónde estaría el siguiente carácter si la línea
fueron escritos en monoancho. Luego, el cursor se mueve a ese punto antes del siguiente carácter.
está apagado. El ancho del carácter monoancho (CHARWD) utilizado para determinar el cursor.
La posición es el ancho de un número entero de la fuente elegida. En general, las letras minúsculas son
más pequeño que CHARWD y las letras mayúsculas son más grandes. Los símbolos matemáticos tratan sobre
el doble del tamaño de CHARWD y la puntuación es aproximadamente la mitad del tamaño de CHARWD. Los personajes en el
secuencias de escape, y los comandos de modificación y composición tipográfica no se cuentan cuando
calcular la posición del cursor.
El comando de formato de tabla finaliza con uno de los siguientes comandos: Etuc, Etf o
Atur.
Ejemplo (con comandos mostrados):
CHARWD 
FUENTE
100 
Times Roman
104 
Bodoni
112 
helvética
88 
gótico
2. Tabulación
Las tablas se pueden configurar espaciando las entradas de las columnas en una línea, o las entradas se pueden tabular a la
posición adecuada utilizando el carácter de tabulación ASCII. El comando 0l establece una pestaña en la columna
el carácter "i" está adentro. Cualquier comando 01 anterior en la línea se ignora al calcular
la posición de la pestaña. Por ejemplo, para configurar pestañas después de las posiciones 5 y 10, la línea se establecería como: 5
espacios, 6l, 5 espacios, 0l. Se pueden configurar hasta 15 pestañas en una línea. El comando 2 borra todas las pestañas.
configuración a la derecha del comando. Para usar. la configuración de la pestaña con el material de la mesa, simplemente clave
en un carácter de tabulación al final de cada entrada de columna. Cuando se escriba, el cursor
avanza automáticamente a la siguiente pestaña antes de mostrar los caracteres siguientes. Líneas
Los archivos que contienen conjuntos de pestañas y borrados de pestañas se pueden utilizar según se desee en todo el archivo ASCII.
Las tablas se ingresan como lo haría un mecanógrafo. Las columnas están espaciadas para que la mesa se vea bien.
Las entradas de comentarios pueden ocupar varias columnas sin cambiar el formato. La única regla de
El pulgar es asegurarse de que cada entrada en una línea esté separada por al menos dos espacios de
la siguiente entrada y que ninguna entrada de una sola columna contenga dos espacios adyacentes. La figura 21 es una
Ejemplo de una tabla configurada con diferentes conjuntos de posiciones de pestañas en una sola página.
En un archivo con caracteres de tabulación ASCII pero sin pestañas configuradas, la tarjeta *TAB (consulte la Figura 22) se puede
se utiliza para establecer las posiciones de las pestañas antes de que se procese el archivo. La configuración de las pestañas de esta tarjeta ha sido modificada.
cuando se encuentran líneas de borrado de tabulación y conjunto de tabulación en el archivo.
119

E. CONTROLES DE COMPOSICIÓN
1. Antecedentes
Todos los comandos relacionados directamente con el dispositivo de composición tipográfica se realizan en caracteres "rojos".
cadenas, es decir, los comandos comienzan con 03 y terminan con 04. Estos comandos están impresos en
rojo en un terminal ASCII para evitar cualquier confusión con el texto normal en una línea. cuando
convertidos a GPSDC (ver Tabla 4), los comandos están representados por los caracteres "rojos"
enumerados en la tabla.
-' 
Los controles de composición tipográfica se dividen en órdenes generales y específicas (únicas). el
Los controles generales de composición tipográfica se encuentran en los comandos de parámetros de formato numerados dos.
hasta las seis.
2. Parámetros de formato
Hay siete parámetros de formato:
Parámetro 
Descripción
1 
Número de archivos que se procesarán en una cinta de entrada.
2 
tamaño de punto
3 
ancho de página en picas o unidades tipográficas
es decir 
4 
profundidad de página en picas o unidades tipográficas
5 
número de puntos a insertar entre líneas (interlineado) Valores de 0 a
7 puntos
6 
Valor = 0, impresión en modo normal (el eje largo de la página coincide con el eje largo)
del papel de máquina de fotocomposición). Tamaño máximo de página 45 picas de ancho y
65 picas de fondo.
6 
Valor = 90, modo de pasar página (eje largo de la página perpendicular al eje largo de
papel para máquina de fotocomposición). tamaño máximo de página 45 picas de ancho y 45
picas profundas.
.
7 
Cambiar temporalmente el espacio entre líneas del valor establecido por formato
parámetro 5 a un nuevo valor entre 0 y 48 puntos. Este valor se utiliza sólo
* 
para el espaciado con la línea que sigue a la línea con este comando.
Un comando de parámetro de formato comienza en la primera posición de una línea y está solo en esa línea.
Seis de los siete parámetros de formato (2-7) se pueden almacenar como líneas dentro de un archivo ASCII.
El parámetro de formato uno, el número de archivos que se procesarán desde una cinta de entrada, no se puede
almacenados en una línea. Este comando tiene significado sólo antes de que se lea un archivo y por lo tanto no es
.. 
válido dentro del archivo.
.1',
4
%., 
120
C.~ 
%~.%. 
%
t 
JiJdI 
2. 
c 
6JI> 
j 
.


Dentro de un archivo, los comandos de parámetros de formato tienen la forma:
'63fpn=m64
donde n = 2,3,4,5,6,7 es el número de parámetro e 'i' es un número entero positivo o cero.
Los parámetros de formato del uno al cinco se pueden preestablecer antes de procesar el archivo usando el
*Tarjeta MISC en el flujo de ejecución de la computadora como se muestra en la Figura 22. El primer número en la tarjeta *MISC
La tarjeta es el parámetro de formato uno, el segundo número es el parámetro de formato dos, etc., como se muestra en
Tabla 7. Los números establecidos por la tarjeta *MISC cambian cuando se ejecuta un comando de formato.
encontrado en el archivo. La tarjeta *MISC se utiliza para establecer parámetros predeterminados y procesar archivos.
que no contiene ningún comando de parámetro de formato.
2. Descripciones de parámetros de formato
un. Formato del parámetro dos (fp2)
Este es el tamaño en puntos utilizado en cualquier formato realizado por los comandos tf, Atuc e itur.
El tamaño en puntos de un fragmento específico de texto formateado se puede modificar sin cambiar el
valor de fp2 mediante el uso de un comando interno de cambio de tamaño de punto. Al final de un
línea centrada (ituc), línea derecha al ras (tur), 
o párrafo (Atf), el tamaño en puntos es
regresa automáticamente al valor fp2. Esta alteración del tamaño de puntos es útil, por ejemplo,
para configurar el encabezado de una tabla en un tamaño de puntos diferente al del cuerpo de la tabla. también es
útil para poner notas a pie de página en letras más pequeñas que el texto principal.
b. Formato del parámetro tres (fp3)
Este es el ancho del texto formateado en picas o unidades tipográficas. desde el
El ancho máximo que puede tener una página es de 65 picas, el programa interpreta cualquier valor de ancho superior a
65 como unidades tipográficas. Hay 2400 unidades tipográficas Videocomp500 por pica.
Se utilizarían unidades tipográficas para el ancho si, por ejemplo, un ancho no entero (en picas)
era deseado. Dado que los valores de los parámetros de formato deben ser enteros sin signo, el ancho sería
deben expresarse en unidades tipográficas.
Ejemplo: establecer el ancho de página en 20,5 picas
Dado que esto requiere un ancho no integral, convierta el ancho a unidades: 20,5 picas=
49200 unidades. El ancho entonces sería establecido por: 3fp3 -4920064
* 
c. Formato del parámetro cuatro (fp4)
Esta es la profundidad de la página en picas o unidades tipográficas. Precaución: hacer

Asegúrate de la profundidad
especificado es menor que el valor descrito en fp6.
.1'2
Eo
.5
". 
121
,.,


d. Formato del parámetro cinco (fp5)
Este es el espacio insertado entre líneas en puntos. El comando fp5 puede tener valores
de 0 a 7 puntos. Cuando 3fp5=004, el texto está "fijado".
Ejemplo:
1) Si 3fp5 -204 y 3fp2 = 84 la ventaja será de 10 puntos.
2) Si O3fp5=2E4 y una línea formateada comienza con un tamaño de puntos internos de 14
(3f144), la línea líder será de 16 puntos.
Nota: Si se aumenta el tamaño en puntos dentro de una línea formateada, es posible sobreimprimir
la línea anterior como líder solo se calcula al comienzo de una línea formateada.
e. Formato del parámetro seis (fp6)
Esto se utiliza para rotar la página 90 grados. Es decir, el eje largo de la página se coloca
perpendicular al eje largo de la página Videocomp 500. El Videocomp 500 tiene un
ventana de 45 picas por 65 picas. Con L3fp6=9004, la página es más ancha que larga: 65
picas por 45 picas. Si se usa, fp6 debe ser 0 o 90. Todos los comandos de fp6 fuerzan una nueva página.
f. Formato del parámetro siete (fp7)
,- 
Cuando se utiliza, fp7 provoca un cambio temporal en el espacio entre líneas establecido por fp5. el
el espacio entre líneas vuelve al valor nominal fp5 después de que se escribe la siguiente línea de texto.
encontrado. El comando fp7 puede tener un valor de 0 a 48 puntos. Esto le da al fp7
ordena un control más preciso del espaciado entre líneas que el comando t + n.
122
%Q
,°-
£ 
% 
A°


".
3. Comandos internos de composición tipográfica
un. Antecedentes
Los comandos internos de composición generalmente permiten un control más preciso de la composición tipográfica.
dispositivo de lo que permiten los parámetros de formato, aunque algunos de los comandos se duplican
* 
funciones de parámetros de formato. Estos códigos tipográficos especiales se pueden insertar en cualquier lugar de
el texto.
La forma del código es: 3fnnj4 donde "nn" es un número entero de dos dígitos.
b. Tabla de comandos de composición tipográfica
Comando 
Descripción
f5 a f36 
establezca el tamaño del punto en este número.
fSO 
persiana desde la posición establecida por (O3f8364) hasta esta posición.
f8. 
subrayado desde la posición establecida por (O3f8304) hasta esta posición.
f82 
sobrepuntuación desde la posición establecida por (3f8304) hasta esta posición.
f83 
establezca una pestaña en esta posición en el dispositivo de composición tipográfica.
f84 
cursor de tabulación a la posición establecida por (03f8304).
f85 
mueva el cursor hacia la parte superior de la página la mitad del interlineado actual.
fhu 
esta es una forma alternativa de medio espacio hacia arriba en formato f85.
f86 
centre el carácter siguiente sobre el carácter anterior.
f87 
disminuir el contador de posición del carácter, COUNTL, en uno. Cuando se utiliza f83 con
f84 para crear caracteres especiales, f87 debe usarse para disminuir COUNTL en uno para
cada carácter adicional que se va a sobreimprimir. Este ajuste es necesario para hacer el
El formato de la tabla funciona correctamente.
-. 0. 
f88 
mueva el cursor hacia abajo en la página una distancia de un cuarto del tamaño en puntos.
f89 
mueva el cursor hacia arriba en la página una distancia de un cuarto del tamaño en puntos.
*'." 
NO 
gire la página 90 grados para que sea más ancha que larga.
f91 
restaurar la página a la rotación adecuada, es decir, la página es más larga que ancha.
f92 a f99 
el número de puntos de espacio (0-7) que se colocarán entre líneas.
Una línea de 8 puntos con una ventaja de 10 puntos tiene 2 puntos de ritmo entre líneas.
123
,%,

do. Usos de muestra de los comandos de composición tipográfica
Los nombres de lugares extranjeros que se muestran en la Figura 23 contienen marcas especiales que no se encuentran en
fuentes de tipo normal. Se pueden crear a partir de fuentes de tipo normal con el uso del
Comandos de composición tipográfica y formato descritos. La Figura 24 muestra cómo se hizo esto. como
Como se ilustra aquí, el comando más útil para la creación de personajes es f86. Figura 25
ilustra varios de los efectos especiales que se pueden crear mediante el uso de combinaciones de
.- 
Comandos de composición tipográfica internos. La Figura 26 muestra los comandos utilizados para realizar la Figura 25.
d. Reglas sobre reglas y tamaños de puntos
.
Los comandos para cambiar el tamaño de los puntos y su efecto se muestran en la parte superior de la figura.
27.
La siguiente sección sobre reglas se muestra tipográfica en la mitad inferior de la Figura 27 para
Ilustre cómo se ven las reglas descritas.
Las reglas nunca deben estar centradas ni justificadas. Las reglas están hechas por una serie de desventajas en un
fila. Las reglas aparecen en el centro de la línea y no en la parte inferior de la línea como en
subrayado.
Regla normal 
3Fn4....................
Regla de la luz (Fa rojo) 
13Fa4 ................. 
3Fn&4
Regla pesada (Fb rojo) 63Fb4 ................ 
OFn&4
" 
Regla extra pesada (F roja) 
03FfH4 ........... 
3Fn4
Regla doble (Fi roja) 
3Fi4-............. 
3Fn4
Normal... Ligero 3Fa4.... 3Fn4 Pesado, 3Fb4...... 3Fn4
Extra Pesado 03Ff4 ..... 3Fn4 Doble 
3Fi£4 .... 3FnO4
e. Espacios y guiones
A veces se necesitan espacios y guiones de ancho fijo. La siguiente tabla muestra
cómo crearlos.
Tabla de guiones y espacios
Comando 
Descripción del espacio y el guión
03V4 
un espacio muy pequeño adecuado para colocar entre un número y su unidad (es decir,
273.15t3!O4K lo que da: 273.15 K)
3f4 
un espacio del ancho de un número entero
un espacio fijo muy grande del ancho de una "W" (un guión bajo ASCII)
.3-44 
un pequeño guión (guión de nuez)
_ 
-un 
guión de tamaño negativo
-354 
un guión del tamaño de una "M
124
IE%
IV 
=;. 
. .,.................,..,.,xp.,...:..,,,',y rw',,
",
,,'P 
pag;, 
W,'p 
(."".2p 
.
'pág. 
"""P",??S


G. EJEMPLO DE TEXTO COMPLEJO
Los comandos de este informe se pueden combinar para realizar una composición tipográfica sofisticada. Figuras 28
y 29 contienen la mayoría de los comandos descritos en este Apéndice. La figura 28 muestra la composición tipográfica.
ejemplo y la Figura 29 muestra los comandos utilizados para producirlo. Algunas tablas en el ejemplo son
configurados en tipo de ocho puntos usando 03fp2=804 y otros se configuran en tipo de ocho puntos usando fD8.
Las modificaciones se logran mediante el comando 3Fb4 y subrayando. El espaciado entre líneas es
.P 
hecho tanto por f3fp7=nnj4 como con comandos ot+n. El texto y las tablas de la Figura 29 están colocados en
exactamente el orden dado en la Figura 28.
pág.4.
'125
V.
-t 
R,.q


*0*
,.J.
-. 4
---
yo
0
~
yo..,
.pJ
~4j
pág. 
.~
* 
.* 
.d

LISTA DE DISTRIBUCIÓN
No, de 
No. de
Copias 
Organización 
Copias 
Organización
12 
Administrador 
1 director
Centro de información técnica de defensa 
Investigación de movilidad aérea del ejército de EE. UU. y
ATENCIÓN: 
DTIC-DDA 
Laboratorio de Desarrollo
Estación Cameron 
Centro de investigación Ames
Alejandría, Virginia, EE.UU. 
22314 
Moffett Field, California, EE.UU. 
94035
1 
Comandante 
1 comandante
Desarrollo de material del ejército estadounidense 
Comunicaciones del Ejército de EE. UU. Rsch y
y comando de preparación 
Comando de desarrollo
ATENCIÓN: DRCDRA-ST. 
ATENCIÓN: DRSEL-ATDD
5001 Avenida Eisenhower 
Fort Monmouth, Nueva Jersey, EE.UU. 
07703
Alejandría, Virginia, EE.UU. 
22333
1 comandante
1 
Comandante 
Investigación en Electrónica del Ejército de EE. UU. y
Centro de I+D de armamento 
Comando de desarrollo
AMCCOM del ejército de EE. UU. 
Actividad de soporte técnico
ATENCIÓN: 
DRSMC-TDC(D) 
ATENCIÓN: 
DELSD-L
Dover, Nueva Jersey 
07801 
Fort Monmouth, Nueva Jersey, EE.UU. 
07703
1 
Comandante 
1 comandante
Centro de I+D de armamento 
Comando de Misiles del Ejército de EE. UU.
AMCCOM del ejército de EE. UU. 
ATENCIÓN: DRSMI-R
ATENCIÓN: 
DRSKC-TSS(D) 
Redstone Arsenal, Alabama 
35898
Dover, Nueva Jersey 
07801
1 comandante
1- Comandante 
Comando de Misiles del Ejército de EE. UU.
Armamento y municiones del ejército estadounidense 
ATENCIÓN: 
DRSMI-YDL
y comando químico 
Redstone Arsenal, Alabama 
35898
ATENCIÓN: 
DRSAR-LEP-L(R)
Rock Island, Illinois, EE.UU. 
61299 
1 comandante
Comando Automotriz de Tanques del Ejército de EE. UU.
1 
Directora 
ATENCIÓN: 
DRSTA-TSL
Laboratorio de armas Benet 
Warren, Michigan, EE.UU. 
48090
Centro de I+D de armamento
AMCCOM del ejército de EE. UU. 
1 director
ATENCIÓN: 
DRSMC-LCB-TL(D) 
Análisis de sistemas TRADOC del ejército de EE. UU.
Watervliet, Nueva York, EE.UU. 
12189 
Actividad
1 
m 
daTTN: 
ATAA-SL
Comandante de 1" 
Campo de misiles White Sands,
Investigación de aviación del ejército de EE. UU. 
Nuevo México 
88002
* @y 
Comando de desarrollo
ATENCIÓN: 
DRDAV-E 
1 comandante
4300 Goodfellow Blvd. 
Escuela de Infantería del Ejército de EE. UU.
San Luis, Missouri 
63120 
ATENCIÓN: ATSH-CD-CSO-OR
1 
Comandante 
Fort Benning, Georgia, EE.UU. 
31905
Desarrollo del ejército de EE. UU.
Agencia de Empleo 
i AFWL/SUL
ATENCIÓN: MODE-TED-SAB 
Base Aérea de Kirtland, Nuevo México 
87117
Fort Lewis, WA 98433 
1 IIQDA(DAMA-ART-M)
127 
Washington, DC 20310
, 
2
•1


LISTA DE DISTRIBUCIÓN (Continuación)
No. de 
No. de
Copias 
Organización 
Copias 
Organización
1 
AFATL/EDIFICIO 
1 
Información Internacional
ATENCIÓN: 
Jack Robbins 
ATENCIÓN: 
Sr. Steve Sandborn
* 
Base de la Fuerza Aérea de Eglin, Florida 
32542 
1747 antiguo camino de la pradera
2 
CmMcLean. 
VA 
22101
2 
Comandante
Centro de armas de superficie naval de EE. UU. Campo de pruebas de Aberdeen
ATENCIÓN: 
Código G12, Harold Jones
Código K11, Don Daniels 
Director, EE.UU.MSAA
Dahlgren, Virginia, EE.UU. 
22448 
ATENCIÓN: 
DRXSY-D
DRXSY-MP, H. Cohen
1 
Cdr de la Comisión Federal de Comunicaciones, USATECOM
División de Servicios Móviles 
ATENCIÓN: 
DRSTE-TO-F
Oficina de transporte común 
Cdr, CRDC, AMCCOM
ATENCIÓN: 
Sr. Gaspar Messina, PHYS/EE 
ATENCIÓN: 
DRSMC-CLB-PA
1919 M Street, N.W. 
DRSMC-CLN
Washington, DC 
20554 
DRSMC-CLJ-L
Subdivisión de Técnicas de AMCCOM/MISSD
1 
Oficina Nacional de Normas 
ATENCIÓN: 
DRSMC-MSE-TL
Oficina de datos de referencia estándar 
Sr. W. Wallace
Edificio de Física A323
ATENCIÓN: 
Dr. David R. Lide
Washington, DC 
20234
2 
Oficina Nacional de Normas
Composición tipográfica electrónica
Edificio administrativo A813
ATENCIÓN: 
Sra. R. J. Morehouse
Washington, DC 
20234
1 
Oficina Nacional de Normas
Información técnica y
División de Publicaciones
Edificio administrativo A540
ATENCIÓN: 
Sr. RC MacCullough
oh 
Washington, DC 
20234
1 
Sr. John Seybold, editor en jefe
El informe Seybold sobre el sector editorial
Sistemas
28936 Cliffside Drive
* 
Malibú, California 
90265
1 
Sra. P. A. Johnson, editora
El P.E.O. Registro
P.E.O. Colección de libros de autores
3700 Gran Avenida
* 
Des Moines, IA 50312
128

* 
-....
HOJA DE EVALUACIÓN DE USUARIO/CAMBIO DE DIRECCIÓN
Este Laboratorio realiza un esfuerzo continuo para mejorar la calidad de los
informes que publica. Sus comentarios/respuestas a los elementos/preguntas a continuación
ayudarnos en nuestros esfuerzos.
1. Número de informe BRL 
Fecha del informe
2. Fecha de recepción del informe
3. ¿Este informe satisface una necesidad? 
(Comentario sobre propósito, proyecto relacionado, o
otra área de interés para la cual se utilizará el informe).
4. flujo específico, ¿se está utilizando el informe? 
(Fuente de información, diseño
datos, procedimiento, fuente de ideas, etc.)
S. ¿La información contenida en este informe ha generado algún ahorro cuantitativo en lo que respecta a
como horas de trabajo o dólares ahorrados, costos operativos evitados o eficiencias logradas,
etc? 
Si es así, por favor explíquelo.
6. Comentarios Generales. 
¿Qué crees que debería cambiarse para mejorar el futuro?
informes? 
(Indicar cambios de organización, contenido técnico, formato, etc.)
.-. 
Nombre
..
ETOrganización
• 
ACTUAL
~DIRECCIÓN
Dirección ARS
Ciudad, Estado, Código Postal
7. Si indica un cambio de dirección o una corrección de dirección, proporcione la
Dirección nueva o correcta en el bloque 6 anterior y la dirección antigua o incorrecta a continuación.
, 
Nombre
VIEJO 
Organización
DIRECCIÓN
Dirección
*Ciudad, 
Estado, Código Postal
(Retire esta hoja a lo largo de la perforación, dóblela como se indica, engrape o pegue con cinta adhesiva
.
cerrado y correo.)
";,* ,' .. .-.,'. ., •.."."-.-> ; . ." 
-.- 
-" 
.-"'-.-;-4 .;';.%'4'"-.-- , 
.,;- -.
,,* -.
'X:'.


.
.
.. 
.. 
-
DOBLAR AQUÍ
3director 
111
Laboratorio de investigación balística del ejército JS 
SIN ENVÍO
_TTN: 
DRXBR-OD-ST 
NECESARIO
Campo de pruebas berdeen, MD 21005-5066 
EN EL
ESTADOS UNIDOS
NEGOCIO OFICIAL
PENALIDAD POR USO PRIVADO. 
oh 
3 
CORREO DE RESPUESTA COMERCIAL
PRIMERA CLASE 
PERMISO N° 12062 
WA44INGTONOC
EL FRANQUEO SERÁ PAGADO POR EL DEPARTAMENTO DEL EJÉRCITO
Directora
Laboratorio de Investigación Balística del Ejército de EE. UU.
ATENCIÓN: DRXBR-OD-ST
Campo de pruebas de Aberdeen, MD 21005-9989
-- 
--- 
DOBLAR AQUÍ--
%
yo
Yo:
S.* 
* 
S% 
.
..
2 
% , ' * .
~ 
% 
' '
S 
°.b 
J~~


*4 
14
*4.
.< 
4w
{ 
AP
~ 
4n4
yo, un
161
t*
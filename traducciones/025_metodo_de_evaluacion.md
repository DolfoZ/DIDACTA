# metodo de evaluacion

doi: 10.21495/5896-3-440 
26ª Conferencia Internacional 
INGENIERÍA MECÁNICA 2020 
Brno, República Checa, 24 y 25 de noviembre de 2020 
DISEÑO DE CURSOS ASINTÓTICOS ADECUADOS DE METEO-
FUNCIONES DEL FACTOR DE PONDERACIÓN BALÍSTICA PARA LA SENSIBILIDAD 
ANÁLISIS DE TRAYECTORIAS DE PROYECTILES PERTURBADOS 
Rozehnal O.*, Čech V.** 
Resumen: Este artículo es una continuación gratuita del artículo presentado en Engineering Mechanics 2014 por Čech, Jevický 
y Jedlička. En la práctica, se utilizan diversas relaciones para analizar la sensibilidad del efecto de las condiciones meteorológicas. 
en la trayectoria incontrolada del proyectil, todos los cuales se derivan del correspondiente Factor de Ponderación 
Funciones - WFF. Una de las formas de analizar la influencia de la tendencia de las condiciones meteorológicas en el proyectil. 
La trayectoria es el uso de cursos asintóticos simplificados de WFF. Así, por ejemplo, Factores de ponderación - WF 
Para STANAG 4061 se crearon de esta manera. En el artículo nos ocupamos del análisis de las propiedades de uno. 
grupo de WFF asintóticos, que es adecuado para incendios de superficie a superficie y el efecto del viento 
en la trayectoria del proyectil con una altitud de hasta cc. 10 km (alcance hasta cc. 30 km) y temperatura virtual hasta 
a la altitud cc. 6 km (autonomía hasta cc. 20 km). A partir de los WFF dados, los sistemas correspondientes de WF son 
fácilmente calculado. A su vez presentamos las relaciones para el cálculo de la Altura de Referencia. 
de trayectoria del proyectil, que se da en las tablas de disparo según la metodología soviética. 
Palabras clave: Perturbación de la trayectoria del proyectil, Función del factor de ponderación (curva), Ponderación 
factor, elementos balísticos (meteorológicos), mesas de tiro. 
1. Introducción 
Cálculos de la posición del Punto Medio de Impacto/Explosión (MPI) utilizando Tablas de Disparo Tabulares (TFT) 
asumir el uso de los llamados “valores balísticos” de viento wB = (wx,B, 0, wz,B), densidad del aire B y virtual 
temperatura Tv,B según metodología NATO STANAG 4061 y 4119 o wB = (wx,B, 0, wz,B), 
temperatura virtual Tv,B y presión del aire p(hG), donde hG es la altitud de la boca del cañón 
del arma/pistola (según la metodología soviética). Para calcular valores balísticos (wB, B, Tv,B), 
Se utilizan los correspondientes Factores de Ponderación - WF, los cuales se calculan simplemente a partir de los correspondientes 
Funciones de factores de ponderación - WFF. Según la metodología soviética, no se utilizan WF, pero 
las correspondientes alturas de referencia YR de la trayectoria del proyectil: los RHT se calculan a partir de los valores dados 
WFF (Kovalenko y Shevkunov, 1975) y (Cech et al., 2014a). Se presentan los valores balísticos actuales. 
en mensajes meteorológicos de artillería especiales, por ejemplo METBKQ (según STANAG 4061). 
Las funciones WFF y Green también son funciones de sensibilidad especiales, sin las cuales no es posible 
realizar análisis de sensibilidad de alta calidad de la influencia de las condiciones meteorológicas en los cambios 
en la trayectoria del proyectil no guiado. 
Las complicaciones en el cálculo de los WFF se deben al llamado "efecto norma". Una teoría mejorada 
de WFF meteobalísticos generalizados (Cech y Jevicky, 2016 y 2019), que 
supera con éxito estos problemas. Esta teoría fue complementada por una teoría mejorada. 
de RHT generalizadas (Cech y Jevicky, 2017). 
Otra complicación (Bliss, 1944), (Molitz y Strobel, 1963) es que la forma de un WFF determinado depende 
sobre el valor específico del coeficiente balístico c, la velocidad inicial (de salida) v0 y el ángulo de salida Θ0. 
En lugar de la dependencia del ángulo Θ0, la dependencia del vértice de la trayectoria (cumbre) 
yS = f (c, v0, Θ0) se menciona con más frecuencia. 
 
* 
Ing. Ondřej Rozehnal: Departamento de Armas y Municiones, Universidad de Defensa; Kounicová 65; 662 10, Brno; 
CZ,ondrej.rozehnal@unob.cz 
**Asociado. Prof. Ing. Vladimír Čech, CSc.: Servicios de investigación y asesoramiento, Osvobození 1654, 666 01 Tišnov; República Checa y 
Departamento de Armas y Municiones, Universidad de Defensa; Kounicová 65; 662 10, Brno; República Checa, vlaczekh@gmail.com 
440

3
Las metodologías para generar mensajes meteorológicos similares a METBKQ asumen la dependencia únicamente de los WF 
en el vértice de la trayectoria yS e ignorar la dependencia del coeficiente balístico c y la velocidad inicial v0. esto 
simplifica todo el problema, pero a costa de reducir la precisión de los valores balísticos calculados. 
En otras palabras, los WF son "promediados" para calibres habituales (cc. 30 a 300 mm) y velocidades iniciales habituales v0 
(cc. 100 a 1300 m/s). Por lo tanto, los WFF "promediados" se utilizan para calcular los WF, que expresan la tendencia 
o componente asintótico del curso de WFF reales (Cech et al., 2014a, b). 
Para el análisis de sensibilidad, estos WFF "promediados" o asintóticos se pueden utilizar en la primera aproximación. 
Sus subconjuntos adecuadamente seleccionados pueden aproximarse ventajosamente mediante funciones analíticas simples. 
En nuestro artículo presentamos una aproximación de los WFF r(, n) - Fig. 1a y r(, n) - Fig. 2b para superficie a
fuego de superficie, que es adecuado para la aproximación de WFF reales para windw = (wx, 0, wz,), hasta 
un vértice de altitud yS de 10 km, que corresponde al rango hasta cc. 30 km, y por virtual. 
temperatura Tv hasta altitud cc. 6 km, lo que corresponde a la autonomía hasta cc. 20 kilómetros. 
2. Aproximación de funciones de factores de ponderación 
La definición básica o aproximación de WFF r(, n) está en el dominio del tiempo - Fig. 1a. la aproximación 
El parámetro es el exponente n  0. De WFF lo obtenemos derivando los correspondientes de Green (impulso 
respuesta) función g(, n) – Fig. 1b (Cech. y Jevicky, 2016 y 2019). 
Sin embargo, para cálculos prácticos, WFF r(, n) – Fig. 2b y funciones de Green g(, n) – Fig. 3a 
en el dominio y de coordenadas verticales (y – dominio de coordenadas) con la notación de Bliss (Bliss, 1944) son más a menudo 
utilizado (Cech y Jevicky, 2016 y 2019). 
La conversión de funciones del dominio del tiempo al dominio de coordenadas y se realiza utilizando la función 
t = f (y), que se selecciona en la primera aproximación como resultado de la teoría de la trayectoria parabólica del vacío. 
Como resultado intermedio obtenemos una función de efecto de dos ramasr(2)(, n) - Fig. 2a. A partir de ahí, WFF 
en y – se calcula el dominio de coordenadas en las notaciones de Garnier y Bliss (Cech y Jevicky, 2016 
y 2019). 
En nuestro caso obtenemos 
 
𝑟(𝜂, 𝑛) = 1 −
1
2𝑛+1 {[1 + √1 −𝜂]
𝑛+1 −[1 −√1 −𝜂]
𝑛+1} 
(1) 
y más 
 
𝛾(𝜂, 𝑛) =
𝑔(𝜂,𝑛)
𝑔(𝜂,0) =
𝑛+1
2𝑛+1 {[1 + √1 −𝜂]
𝑛+ [1 −√1 −𝜂]
𝑛}. 
(2) 
La relación se cumple para el cálculo de valores balísticos ( = wx, wz, Tv, ) 
 
Δ𝜇𝐵(𝑛) = ∫Δ𝜇(𝜏) ∙𝑔(𝜏, 𝑛) ∙𝑑𝜏=
1
0
∫Δ𝜇(𝜂) ∙𝑔(𝜂, 𝑛) ∙𝑑𝜂
1
0
, 
(3) 
donde: 
 =  - STD– desviación absoluta del parámetro meteorológico , 
 
 - valores medidos o modelo, 
 
STD – valores estándar. 
Una relación similar se aplica a las desviaciones relativas  = /STD (Cech y Jevicky, 2016 y 2019). 
3. Análisis de relaciones para los WFF y las funciones de Green 
Ec. (3) representan las integrales de convolución de Duhamel, que también pueden interpretarse como fórmulas 
para calcular el promedio ponderado B de una función dada  usando la función “peso” - Green 
función g. 
Para n = 0, la integral en el dominio del tiempo (Fig. 1b) representa el cálculo de la media aritmética. 
para g(, 0) = 1, mientras que en el dominio de coordenadas y ya es un promedio ponderado. 
Estas relaciones fueron utilizadas por el matemático francés M. E. Borel para calcular el viento balístico ya en 
como la década de 1910 (Cranz, 1925). Sin embargo, el curso g(, 0) contradice la realidad física, porque 
g() = 0 para   1 debe ser válido. Los cursos reales se aproximan para n  0. Surge la pregunta de cómo 
441

4 
Estas aproximaciones se han utilizado con éxito durante más de 100 años. La respuesta es paradójica: 
Los cursos de ambos WFF y la función de Green para n = 0 y 1 son idénticos en y - dominio de coordenadas - 
Fig. 2b, Fig. 3a, aunque tienen cursos completamente diferentes en el dominio del tiempo – Fig. 1. Por lo que sabemos 
Ya sabes, somos los primeros en publicar esta revelación aquí. 
 
 a) b) 
Fig. 1: a) Funciones de factores de ponderación – WFF r(, n); b) Funciones de Green g(, n) 
en el dominio del tiempo (tF – tiempo de vuelo hasta el punto de caída; elegido por simplicidad tF = 1 s). 
 
 a) b) 
Fig. 2: a) Funciones de efecto de dos ramas r(2)(, n); b) Funciones de factores de ponderación – WFF r(, n) 
en coordenadas verticales dominio y (y – dominio de coordenadas). 
 
 a) b) 
Fig. 3: a) Funciones de Green g(, n); b) relación (, n) 
en coordenadas verticales dominio y (y – dominio de coordenadas). 
442

 
 
5
 
Fig. 4: Momento mWFF,1(n) de las funciones de factores de ponderación r(, n). 
De la Fig. 3a queda claro que las funciones de Green g(, n) divergen para  1, más cercanas a Cech V. y Jevicky J. 
(2019). 
De la Fig. 3a, b muestra que a medida que n (n  0,414) aumenta, el peso de una parte de la trayectoria del proyectil 
cerca de su vértice (  cc. 0,667) disminuye, y luego el peso de su parte en el suelo aumenta 
(cc. 0,667). Como resultado, la altura de referencia YR de la trayectoria del proyectil también cambia – Fig. 4. 
4. Conclusiones 
En el siguiente período, publicaremos gradualmente otras aproximaciones asintóticas adecuadas de WFF. 
Reconocimiento 
Este trabajo se originó con el apoyo del financiamiento del Proyecto de Investigación para el Desarrollo de la 
Departamento de Armas y Municiones, Facultad de Tecnología Militar, Universidad de Defensa, Brno, 
DZRO VYZBROJ. 
Referencias 
Bliss, G. A. (1944) Matemáticas para balística exterior. John Wiley and Sons, Inc., Londres, Impreso en EE. UU. 1944, 
pág. 128. 
Cech, V., Jedlicka, L. y Jevicky, J. (2014a) Problema de la altura de referencia de la trayectoria del proyectil 
como factor de ponderación meteobalístico reducido. Tecnología de Defensa 10, no. 2, edición. 2, Número especial del día 28. 
Simposio Internacional de Balística, ISSN: 2214-9147, págs. 131-140. 
Cech, V., Jedlicka, L. y Jevicky, J. (2014b) Algunos problemas con la estimación de la trayectoria del proyectil 
Perturbaciones. Proc. de la XX Conferencia Internacional. Ingeniería Mecánica 2014, Ed. Fuis, V., Svratka, págs. 116-119. 
Cech, V. y Jevicky, J. (2016) Teoría mejorada de las funciones de los factores de ponderación meteobalísticos generalizados y sus 
uso, Tecnología de Defensa 12, edición. 3: Número especial del 29º Simposio Internacional de Balística, ISSN: 2214-
9147, págs. 242-254. 
Cech, V. y Jevicky, J. (2017) Teoría mejorada de las alturas de referencia de la trayectoria del proyectil como características de 
Funciones de sensibilidad meteobalística, Defense Technology 13, iss. 3: Número especial de la 30ª Internacional 
Simposio de Balística, ISSN: 2214-9147, págs. 177-187. 
Cech V. y Jevicky J. (2019) Algunos problemas con los cálculos numéricos de la sensibilidad meteobalística 
Funciones y sus soluciones. Revista IOSR de Ingeniería Civil y Mecánica (IOSR – JMCE), vol. 16, edición. 4, 
Ser. Yo, págs. 1-16. 
Cranz C. (1925) Libro de texto de balística. 1er volumen. Balística Exterior. 5ª edición, Springer Verlag, Berlín 1925, 
pág. 712, (en alemán). 
Kovalenko, V. V. y Shevkunov, V. I. (1975) Preparación meteorológica del fuego de artillería. Artillería militar 
Academia de M. I. Kalinin, Leningrado, p. 84, (en ruso). 
Molitz, H. y Strobel, R. (1963) Exterior Ballistics, Berlín, Springer-Verlag, 610 p., (en alemán). 
STANAG 4061 MET, ed. 4 Adopción de un mensaje meteorológico balístico estándar (METBKQ), 2000. 
STANAG 4119, ed. 2 Adopción de un formato estándar de mesa de disparo de artillería de cañón, 2007. 
443
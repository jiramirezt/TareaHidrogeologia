# Taller 1 Hidrogeologia Ambiental

## Introduccion
En el presente trabajo se realizará el análisis hirdogeoquimico de una serie de muestras tomadas en puerto Wilches, 
con el fin de identificar y explicar el comportamiento hidrogeológico de la zona.

## Área de estudio
Puerto Wilches es un municipio del departamento de Santander, estando situado en la margen derecha del rio Magdalena. El municipio se encuentra a una altura promedio de 75 msnm, su extensión se caracteriza por ser de características calurosas y húmedas, pues su temperatura oscila en el rango de los 35 y 40°C. La zona cuenta con una precipitación media anual (PMA) de 3100 mm. La zona esta conformada por distintas unidades hidrogeológicas de edad cuaternaria cuyo principal atributo es la baja consolidación y predominio de sedimentos como arena y grava, intercalados con materiales de grano fino como lo son arcillas y limos. Las unidades que funcionan como acuíferos son los depósitos de origen aluvial que afloran en cercanías del rio Magdalena (Malagón et al., 2021).

![Imagen1](https://user-images.githubusercontent.com/69225268/167980246-a37f46b8-44a6-478b-9d9a-9307802b2bb6.png?style=centerme)

**Figura 1:** Mapa Geológico del Sistema Acuífero Valle Medio del Magdalena (Malagón et al., 2021). 

Para el estudio a analizar en el presente trabajo se utilizó la información de 45 muestras realizadas en el dominio aledaño al rio Magdalena y el rio Sogamoso.
![Mapa 1](https://user-images.githubusercontent.com/69225268/167980589-d4fc9109-c4a3-4501-b9c0-cbcbde571400.png)

**Figura 2:** Mapa de los puntos tomados en campo y su tipología. Fuente: Elaboración propia

## Balance ionico

Para asegurar la calidad de las muestras compiladas, se calculó el valor del error analítico del balance iónico, de manera tal, que la suma de la concentración en miliequivalentes de cationes debe ser igual a la suma de las concentraciones en miliequivalentes de aniones. La ecuación para efectuar el balance iónico es la siguiente:

![ecuacion](https://user-images.githubusercontent.com/69225268/168128807-743c944a-3881-4411-89ba-c401f2c071cd.png)

Para garantizar que la muestra cumple con estándares de calidad se debe rechazar si el balance iónico es menor o igual a ±10%. Al efectuar el balance iónico de las 45 muestras tomadas, 29 cumplen adecuadamente con el balance iónico. En el siguiente mapa se puede ver como estuvieron distribuidas espacialmente las muestras según su estudio. 

![Mapa2](https://user-images.githubusercontent.com/69225268/168134400-d79a6e2f-07cc-49f6-96e3-239f0df29149.png)

**Figura 3:** Mapa de los puntos filtrados y no filtrados en el balance iónico 

## Análisis estadistico multivariado 

El análisis estadístico multivariado (AEM) es una herramienta que permite la identificación de grupos distintivos de las muestras y las correlaciones presentes entre sus parámetros. Para efectuar el AEM, se utilizó el paquete estadístico FactoMineR incluido en el lenguaje de programación estadístico R. El conjunto de datos utilizado para el AEM consistió en una base de datos de 29 muestras por 13 parámetros, 11 activos (pH, Ca<sup>2+</sup>, Na<sup>+</sup>, K<sup>+</sup>, Mg<sup>2+</sup>, Fe total, Cl<sup>-</sup> , SO<sub>4</sub><sup>2-</sup>, HCO<sub>3</sub><sup>2-</sup> , NO<sub>3</sub><sup>-</sup> y NO<sub>2</sub><sup>-</sup>) y 2 suplementarios (CE y SDT). A partir de estos se obtuvo la tabla descriptiva de cada uno de los parámetros.


**Tabla 1:** Resumen estadístico para cada una de las variables presentes en la zona

![tabla](https://user-images.githubusercontent.com/69225268/168139240-154628e3-0c03-48b3-b38d-46fa8336d05a.png)

## Resultados
### Análisis de agrupamiento Jerárquico (AAJ)
Lo primero que se realizó en el ámbito asociado al AEM fue el análisis de agrupamiento jerárquico a partir de el paquete FactoMineR del lenguaje de programación R. La posición marcada por la línea fenotípica que cruza el dendograma permitió la conformación de 3 grupos que conformaron cada una de las 29 muestras tomadas en campo.  Inicialmente se efectuó el diagrama de circulo de correlaciones para cada muestra a partir del análisis. 

![image](https://user-images.githubusercontent.com/69225268/168167805-fd7176fc-699f-42f6-a303-2dd98e8ec15b.png)

![image](https://user-images.githubusercontent.com/69225268/168168189-44a24add-e9d5-4065-b6fd-fc410c8a499a.png)

**Figura 4:** Circulo de Correlaciones. Fuente: Elaboración Propia

A partir del análisis de agrupamiento jerárquico también se esquematizaron de manera adecuada las diferentes muestras tomadas en campo. 

![image](https://user-images.githubusercontent.com/69225268/168146565-bcf0d53f-def7-47e2-a386-e8ec334143a9.png)

**Figura 5:** Proyección de las 29 muestras según sus resultados del AAJ. Fuente: Elaboración Propia

Adicionalmente se presenta un diagrama jerárquico donde se analiza cada uno de los grupos presentes en el muestreo realizado en la zona, para lo cual se presenta el siguiente esquema:

![image](https://user-images.githubusercontent.com/69225268/168147694-cd7f0c79-0f78-4258-9094-4738d9f3f13b.png)

 
**Figura 6:** Proyección de las 29 muestras según sus resultados del AAJ. Fuente: Elaboración Propia

A partir del análisis químico de las muestras se correlacionará lo obtenido en el análisis jerárquico con las características químicas presentes en las muestras tomadas en campo. 

### Química del agua

La exploración y análisis de la información hidro química del agua subterránea se realizó mediante la exploración de diferentes métodos gráficos teniendo en cuenta el contenido de los componentes presentes en cada una de las muestras. Para este estudio se realizaron los diagramas de Piper, Stiff, Durov, Schoeller, Gibbs, Chadha, Gaillardet y el HFed, esto con el fin de analizar de manera precisa las características hidro geoquímicas de la zona de muestreo.  

Inicialmente se hace el análisis respecto a lo que se obtuvo en el diagrama de Piper

 ![image](https://user-images.githubusercontent.com/69225268/168148345-9accc8e7-7244-4dd4-9b2b-17a9337690aa.png)

**Figura 7:** Diagrama de Piper
Con base al diagrama de Piper (Figura 6), se determino que la gran cantidad de muestras no tiene un tipo dominante en lo que cationes concierne, pero se evidencia a su vez la tendencia de ciertas muestras a presentar características cálcicas en los cationes. El agua adicionalmente presenta características bicarbonatadas en el ámbito de los aniones; la característica dominante en las muestras es que son del tipo magnésico bicarbonatado, este aspecto al relacionarlo con la tabla 1 presenta una correlación adecuada, debido principalmente a que las concentraciones medias son mas altas en el Bicarbonato y en el Calcio. Si se efectúa el análisis por grupos jerárquicos, las muestras del grupo 1 cuentan con una característica mixta y en ciertos casos de tipo sódica bicarbonatada, mientras que las del grupo 2 y 3 cuentan con características magnésica bicarbonatada. 

Luego se hace el análisis respecto a lo que se obtuvo en el diagrama de Stiff

![image](https://user-images.githubusercontent.com/69225268/168148911-592eee81-a948-4988-9c37-3e26a9edb7bb.png)

**Figura 8:** Diagramas de Stiff

Se puede ver que en el grupo 1 la muestra que en las muestras del grupo 1 existe una tendencia a ser bicarbonatadas con una leve presencia de sodio en su contenido, y resalta un bajo contenido de bicarbonatos en su estructura. El grupo 2 se caracteriza por una tendencia a los bicarbonatos y los calcios, para lo cual se asocia bien a la descripción asignada por el diagrama de Piper de la Figura 6. Finalmente el grupo 3 cuenta con una concentración prioritaria de calcio, bicarbonatos y moderada de sulfatos, para lo cual existe una correlación con lo determinado en el diagrama de Piper. 
Luego se hace el análisis respecto a lo que se obtuvo en el diagrama de Durov

![image](https://user-images.githubusercontent.com/69225268/168151492-1e44f55b-609d-4648-8666-630c056e2f91.png)

**Figura 9:** Diagrama de Durov

En el diagrama de Durov muestra muestra que la mayoría de las muestras tomadas en campo están marcando la tendencia en el intercambio iónico inverso (Reverse Ion Exchange), lo cual caracteriza la muestra tomada en el ámbito relacionado con el intercambio de iones mas que una situación ligada a la mezcla. 

Luego se hace el análisis respecto a lo que se obtuvo en el diagrama de Schoeller
 
 ![image](https://user-images.githubusercontent.com/69225268/168153994-5ffc13fb-07ed-46a9-9b5b-120dfbfb6a3f.png)

**Figura 10:** Diagrama de Schoeller

Los diagramas de Schoeller se utilizan para mostrar las concentraciones relativas de aniones y cationes típicamente expresadas en miliequivalentes por litro. Se pueden esbozar múltiples muestras de diferentes pozos en un solo diagrama para identificar patrones similares en las proporciones de aniones y cationes particulares. Las concentraciones de agua son una función de la geoquímica del agua subterránea y la composición química del material rocoso presente en los cuerpos hidrogeológicos. Se puede evidenciar que existe una tendencia muy marcada por la separación de los grupos, por lo cual vale la pena resaltar que el AAJ efectuo una buena diferenciación separando los diferentes grupos en sistemas con una tendencia de cambio similar.  

Luego se hace el análisis respecto a lo que se obtuvo en el diagrama de Gibbs  

![image](https://user-images.githubusercontent.com/69225268/168154346-62c8e707-8977-464a-9b8e-8eeb8d95cf57.png)

**Figura 11:** Diagrama de Gibbs

El diagrama de Gibbs describe los principales procesos que gobiernan la quimica del agua superficial. Según Gibbs, los principales procesos que gobiernan incluyen la evaporación, la precipitación y la interacción agua-roca. La influencia de estos procesos es clara en el diagrama de dispersión: donde las relaciones sodico calcicas plasmadas en el eje x se representan frente a los sólidos disueltos totales plasmados en el eje y (Marandi & Shand, 2018). El patrón del mundo cuerpos de agua superficiales forman una nube en forma de boomerang como se puede ver en la figura 10. Observando los puntos tomados en campo se evidencia un dominio rocoso en la muestras. La mayoría de los ríos y cuentan con concentraciones bajas o moderadas, y por lo tanto, se suelen ubicar en la parte media del 'boomerang' como se puede ver en la figura. 

Luego se hace el análisis respecto a lo que se obtuvo en el diagrama de Chadha

![image](https://user-images.githubusercontent.com/69225268/168154436-40d8f370-1c2f-483c-924d-7a665d421dfc.png)

**Figura 12:** Diagrama de Chadha

El diagrama de Chadca se construye a partir de ubicar en el eje x la diferencia entre las tierras y los metales alcalinos, expresados como porcentaje de valores reactivos, mientras que en el eje y se dibuja la diferencia entre los aniones débiles y aniones fuertes (Chadha, 1999). Se puede observar en la figura 11, que la mayoría de los puntos se encuentra localizado en la zona 5 del diagrama, esto implica que las aguas presentes en el diagrama cuentan con una alta diferencia entre los bicarbonatos y los cloros, por lo cual se pueden caracterizar como aguas cálcicas-magnésicas bicarbonatadas. Al hacer la jerarquización por grupos se evidencia que el grupo q esta mas ligado a aguas incluso de características sodico-bicarbonatadas (cuadrantes 3 y 8 del diagrama). 



Luego se hace el análisis respecto a lo que se obtuvo en el diagrama de Gaillardet

![image](https://user-images.githubusercontent.com/69225268/168154981-b16a604f-2d0d-4285-ae4c-58b683a9cc88.png)

**Figura 13:** Diagrama de Gaillardet

El diagrama de Gaillardet consta de tres regiones que corresponden a tres procesos hidroquimicos respectivos: disolución de carbonato, meteorización de silicato y disolución de evaporita. Si una muestra tomada en campo de agua subterránea cae en cierta región del gráfico, significa que el proceso hidroquímico representado por esa región juega un papel dominante en el sitio donde se recolectó la muestra (Wu et al., 2021). Cuando una muestra cae entre dos regiones, eso implica la coexistencia de diferentes procesos hidro químicos en el sitio. A partir de los datos tomados en campo se puede observar que están ubicados en la región situada entre los silicatos y los carbonatos, sugiriendo que la composición del agua subterránea de la zona esta dominada por la meteorización de silicatos y la disolución de carbonatos. 
Luego se hace el análisis respecto a lo que se obtuvo en el diagrama de HFED


 ![image](https://user-images.githubusercontent.com/69225268/168155608-ab692262-efce-43fd-b65f-cad3a8b530a2.png)

**Figura 14:** Diagrama de HFED

El diagrama de evolución de fases hidroquimicas (HFED) fue concebido para interpretar la hidroquimica de las fases de intrusión y recuperación de la intrusión marina en acuíferos de características costeras. Sin embargo, también se puede emplear como alternativa a otros diagramas hidroquímicos(Giménez-Forcada, 2019). Tiene como gran ventaja que permite la visualización de posibles agrupaciones de muestras y tendencias de evolución que ocurren en el acuífero. En la zona de estudio se puede asimilar que la gran parte de las muestras están contenidas en la zona asociada al freshening que combina un alto contenido de calcios y carbonatos, lo cual confirma lo analizado previamente en los diferentes diagramas. 

## Conclusiones

A partir de el desarrollo de los diferentes diagramas y agrupación se pueden evidenciar los siguientes aspectos principales: La zona a estudiar cuenta con aguas donde predominan características cálcicas en los cationes;  adicionalmente presenta características bicarbonatadas en el ámbito de los aniones. Por medio del clustering efectuado por cada uno de los grupos las muestras del grupo 1 cuentan con una característica mixta y en ciertos casos de tipo sódica bicarbonatada, mientras que las del grupo 2 y 3 cuentan con características magnésica bicarbonatada. A partir del PCA, se puede determinar que existe una buena consistencia con el AAJ. Las muestras del grupo 1 están situadas en el lado medio izquierdo de la figura y corresponden a las muestras con mayor mineralización. Las muestras de los grupos 2 se encuentran en el centro del plano factorial, por lo cual son muestras con un nivel intermedio de mineralización, finalmente las muestras del grupo 3 están situadas en el lado medio izquierdo de la figura y corresponden a las muestras con menor mineralización.

A partir de los diagramas se pudo obtener una descripción muy detallada de la caracterización de las aguas subterráneas en la zona de puerto Wilches, y como es mencionado previamente, para cada grafica existe una particularidad que ayuda a describir una propiedad nueva a partir de la caracterización química.   


## Bibliografia

Chadha, D. K. (1999). A proposed new diagram for geochemical classification of natural waters and interpretation of chemical data. Hydrogeology Journal, 7(5), 431–439. https://doi.org/10.1007/s100400050216

Giménez-Forcada, E. (2019). Use of the Hydrochemical Facies Diagram (HFE-D) for the evaluation of salinization by seawater intrusion in the coastal Oropesa Plain: Comparative analysis with the coastal Vinaroz Plain, Spain. HydroResearch, 2, 76–84. https://doi.org/10.1016/j.hydres.2019.11.007

Malagón, J. P., Piña, A., Argüello, S., & Donado, L. D. (2021). Hydrogeochemical-multivariate analysis of groundwater in the aquifer system of the middle Magdalena valley, Colombia: Regional-scale study. Boletin de La Sociedad Geologica Mexicana, 73(3). https://doi.org/10.18268/BSGM2021v73n3a070421

Marandi, A., & Shand, P. (2018). Groundwater chemistry and the Gibbs Diagram. In Applied Geochemistry (Vol. 97, pp. 209–212). Elsevier Ltd. https://doi.org/10.1016/j.apgeochem.2018.07.009

Wu, C., Wu, X., Lu, C., Sun, Q., He, X., Yan, L., & Qin, T. (2021). Hydrogeochemical characterization and its seasonal changes of groundwater based on self-organizing maps. Water (Switzerland), 13(21). https://doi.org/10.3390/w13213065

Yang, J., Liu, H., Tang, Z., Peeters, L. and Ye, M. (2022), Visualization of Aqueous Geochemical Data Using Python and WQChartPy. Groundwater. https://doi.org/10.1111/gwat.13185

Lê S, Josse J, Husson F (2008). “FactoMineR: A Package for Multivariate Analysis.” Journal of Statistical Software, 25(1), 1–18. doi: 10.18637/jss.

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


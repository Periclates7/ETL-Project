![Cabecera](https://static1-es.millenium.gg/articles/1/36/32/1/@/169471-league-of-legends-article_image_d-1.jpg)

# 馃幃 ETL PROJECT -> League of Legends Database 馃幃
  
El presente proyecto se basa en la necesidad que me surge como jugador del juego online League of Legends de tener una base de datos accesible y funcional para la configuraci贸n 贸ptima de cada campe贸n antes de cada partida. Para ello se han utilizado las t茅cnicas propias del proceso ETL (Extracci贸n, Transformaci贸n y Carga) para la realizaci贸n de dicha base de datos en un servidos SQL.
  
## 馃幆 OBJETIVOS DEL PROYECTO 
  
1. Crear un repositorio en GitHub con una buena organizaci贸n de los recursos.
2. Extraer datos de diversas fuentes tales como p谩ginas web, APIs o archivos '.csv'.
3. Aplicar herramientas, t茅cnicas y metodolog铆as para la limpieza de datos acordes a nuestras necesidades:
    - Filtrado de los datos extraidos
    - Exploraci贸n del conjunto de los datos
    - Limpieza de valores nulos
    - Transformaci贸n de diferentes conjuntos de datos
    - Librer铆as utilizadas: Pandas, Numpy, regex, pylab, seaborn, selenium, BeautifulSoup
3. Cargar de los datos a SQL a trav茅s de Python.
4. Establecer las relaciones entre tablas.
5. Filtrar datos a trav茅s de querys.

## 鉀? EXTRACCI脫N DE LOS DATOS  
  
Partimos de la base de datos [LOL-stats](https://www.kaggle.com/code/andycheung0211/lol-stats/data?select=League+of+Legends+Champion+Stats+12.1.csv) encontrada en la web Kaggle. En ella encontramos una relaci贸n de los campeones del juego con algunas estad铆sticas b谩sicas como el *winrate* o el *banrate*. Esta informaci贸n es insuficiente as铆 que se decide completarla a trav茅s de metodolog铆as de *scraping*. Para ello utilizaremos herramientas como *Selenium* para obtener datos referentes a las debilidades, las fortalezas, la composici贸n de objetos o los hechizos de invocador de cada campe贸n. Tambi茅n se utiliza *Selenium* para extraer datos acerca de los objetos comprables en la tienda del juego y sus estad铆sticas. Esta tabla ser谩 independiente al resto en nuestra base de datos. Mediante la herramienta de *scrapeo* *BeautifulSoup* obtendremos la composici贸n de runas que se a帽adir谩 a nuestra relaci贸n de campeones. Por 煤ltimo obtendremos de la API de Riot (empresa creadora del videojuego), la rotaci贸n semanal de campeones gratuitos y que podr谩 ser actualizada semanalmente.
  
## 馃搱 LIMPIEZA DE LOS DATOS  
  
Puesto que hemos sido meticulosos y cuidadosos en la extracci贸n, la limpieza de los datos no ha supuesto ning煤n reto. El archivo '.csv', ha sido el 煤nico recurso que no hemos extraido por nosotros mismos por lo que se han debido eliminar ciertas columnas que no aportaban nada a la base de datos para nuestro prop贸sito. Al hacer *merge* entre cada uno de nuestros *dataframes* se han generado valores nulos debido a falta de informaci贸n. Estos nulos se han limpiado previamente a su carga en SQL.

## 馃惉 IMPORTACI脫N A SQL  
  
Una vez preparados, es hora de cargar nuestros datos a SQL de manera que sean funcionales para su consulta. El resultado es la carga de tres tablas. La tabla objetos ser谩 independiente tal y como comentaba en anteriores lineas. La tabla campeones ser谩 el n煤cleo de nuesta base de datos la cual se relacionar谩 con la tabla en la que se contempla la disponibilidad de los campeones de rotaci贸n gratuita. La relaci贸n se muestra en el siguiente diagrama:
  
![EDR](https://github.com/Periclates7/ETL-Project/blob/main/img/diagrama.png)
  
## 馃摑 CONCLUSIONES
  
La organizaci贸n en una actividad que se est谩 desarrollando, independientemente de su 铆ndole, es imprescindible para llevarla a cabo con el mayor rigor y la mayor productividad. Es por esto que nace la necesidad de tener una base de datos ordenada, accesible y funcional. Mediante la extracci贸n, transformaci贸n y carga de los datos, se ha cubierto tal necesidad.
  
En la ruta 'data/querys/querys.sql' de este repositorio, encontrar谩n algunos ejemplos de querys que avalan el rendimiento y la funcionalidad de la reci茅n creada base de datos.
  

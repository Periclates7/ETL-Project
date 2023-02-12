![Cabecera](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.millenium.gg%2Fnoticias%2F36321.html&psig=AOvVaw2Ef_EOPqSrJws7hRLaKoz6&ust=1676308418664000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNCHgdG9kP0CFQAAAAAdAAAAABAE)

# ETL PROJECT -> League of Legends Database 🎮
  
El presente proyecto se basa en la necesidad que me surge como jugador del juego online League of Legends de tener una base de datos accesible y funcional para la configuración óptima de cada campeón antes de cada partida. Para ello se han utilizado las técnicas propias del proceso ETL (Extracción, Transformación y Carga) para la realización de dicha base de datos en un servidos SQL.
  
## 🎯 OBJETIVOS DEL PROYECTO 
  
1. Crear un repositorio en GitHub con una buena organización de los recursos.
2. Extraer datos de diversas fuentes tales como páginas web, APIs o archivos '.csv'.
3. Aplicar herramientas, técnicas y metodologías para la limpieza de datos acordes a nuestras necesidades:
    - Filtrado de los datos extraidos
    - Exploración del conjunto de los datos
    - Limpieza de valores nulos
    - Transformación de diferentes conjuntos de datos
    - Librerías utilizadas: Pandas, Numpy, regex, pylab, seaborn, selenium, BeautifulSoup
3. Cargar de los datos a SQL a través de Python.
4. Establecer las relaciones entre tablas.
5. Filtrar datos a través de querys.

## ⛏ EXTRACCIÓN DE LOS DATOS  
  
Partimos de la base de datos [LOL-stats](https://www.kaggle.com/code/andycheung0211/lol-stats/data?select=League+of+Legends+Champion+Stats+12.1.csv) encontrada en la web Kaggle. En ella encontramos una relación de los campeones del juego con algunas estadísticas básicas como el *winrate* o el *banrate*. Esta información es insuficiente así que se decide completarla a través de metodologías de *scraping*. Para ello utilizaremos herramientas como selenium para obtener datos referentes a las debilidades, las fortalezas, la composición de objetos o los hechizos de invocador de cada campeón. También se utiliza selenium para extraer datos acerca de los objetos comprables en la tienda del juego y sus estadísticas. Esta tabla será independiente al resto en nuestra base de datos. Mediante la herramienta de *scrapeo* BeautifulSoup obtendremos la composición de runas que se añadirá a nuestra relación de campeones. Por último obtendremos de la API de Riot(empresa creadora del videojuego), la rotación semanal de campeones gratuitos y que podrá ser actualizada semanalmente.
  
## 📈 LIMPIEZA DE LOS DATOS  
  
Puesto que hemos sido meticulosos y cuidadosos en la extracción, la limpieza de los datos no ha supuesto ningún reto. El archivo '.csv', ha sido el único recurso que no hemos extraido por nosotros mismos por lo que se han debido eliminar ciertas columnas que no aportaban nada a la base de datos para nuestro propósito. Al hacer *merge* entre cada uno de nuestros *dataframes* se han generado valores nulos debido a falta de información. Estos nulos se han limpiado previamente a su carga en SQL.

## 🐬 IMPORTACIÓN A SQL  
  
Una vez preparados, es hora de cargar nuestros datos a SQL de manera que sean funcionales para su consulta. El resultado es la carga de tres tablas. La tabla objetos será independiente tal y como comentaba en anteriores lineas. La tabla campeones será el núcleo de nuesta base de datos la cual se relacionará con la tabla en la que se contempla la disponibilidad de los campeones de rotación gratuita. La relación se muestra en el siguiente diagrama:
  
![EDR](https://github.com/Periclates7/ETL-Project/blob/main/img/diagrama.png)
  
## 📝 CONCLUSIONES
  
La organización en una actividad que se está desarrollando, independientemente de su índole, es imprescindible para llevarla a cabo con el mayor rigor y la mayor productividad. Es por esto que nace la necesidad de tener una base de datos ordenada, accesible y funcional. Mediante la extracción, transformación y carga de los datos, se ha cubierto tal necesidad.
  

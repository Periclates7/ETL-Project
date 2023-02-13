---------- QUERY 1 -------------
Agrupamos por campeones para sacar la buidl completa en partida.

SELECT campeon, 
	   CONCAT(item_1, item_2, item_3, 
              item_4, item_5, item_6)
FROM campeones 

GROUP BY campeon
;




---------- QUERY 2 -------------
Comprobamos la disponibilidad de campeones gratuitos de la semana.

SELECT campeon, runas, hechizos
FROM campeones as c

LEFT JOIN disponibilidad as d
ON c.riot_id = d.riot_id

WHERE disponibilidad = 'disponible'
;




---------- QUERY 3 -------------
Comprobamos que campeones son fuertes contra el campeón que se especifique en el WHERE

SELECT campeon
FROM campeones as c


WHERE fuerte LIKE '%Aatrox%'
;
---------- QUERY 1 -------------
SELECT campeon, 
	   CONCAT(item_1, item_2, item_3, 
              item_4, item_5, item_6)
FROM campeones 

GROUP BY campeon
;




---------- QUERY 2 -------------

SELECT campeon, runas, hechizos
FROM campeones as c

LEFT JOIN disponibilidad as d
ON c.riot_id = d.riot_id

WHERE disponibilidad = 'disponible'
;
WITH RECURSIVE cte_ecoli as (

    SELECT ID , PARENT_ID, 1 AS level
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL 
    
    SELECT e.ID , e.PARENT_ID, ce.level+1 AS level
    FROM ECOLI_DATA e
    JOIN cte_ecoli ce ON e.PARENT_ID = ce.ID
)

SELECT ID
FROM cte_ecoli ce
WHERE ce.level = '3'


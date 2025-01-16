SELECT DISTINCT DE.ID, DE.EMAIL, DE.FIRST_NAME, DE.LAST_NAME
FROM DEVELOPERS DE
INNER JOIN SKILLCODES S ON S.CODE & DE.SKILL_CODE 
WHERE S.NAME IN ('Python', 'C#')
ORDER BY DE.ID ASC;
SELECT COUNT(ED.ID) AS COUNT
FROM ECOLI_DATA AS ED
WHERE 
    (ED.GENOTYPE & (1 << (2 - 1))) = 0  -- 2번째 비트가 1인지 확인!!!
    AND (ED.GENOTYPE & ((1 << (3 - 1)) | (1 << (1 - 1)))) > 0;  -- 1번째 또는 3번째 비트가 1인지 확인 !!!

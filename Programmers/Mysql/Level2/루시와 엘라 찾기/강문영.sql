-- 코드를 입력하세요
SELECT animal_id, name, sex_upon_intake
from animal_ins
where name = "Lucy" or name = "Ella" or name = "Pickle" or name= "Rogan" or name = "Sabrina" or name = "Mitty"
order by animal_id

-- SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
-- FROM ANIMAL_INS
-- WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
-- ORDER BY ANIMAL_ID;

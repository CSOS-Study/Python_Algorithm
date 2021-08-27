-- 코드를 입력하세요
SELECT hour(datetime) as "HOUR", count(datetime) as "COUNT"
from animal_outs
where hour(datetime)>=09 and hour(datetime)<=19
group by hour(datetime)
order by hour(datetime)

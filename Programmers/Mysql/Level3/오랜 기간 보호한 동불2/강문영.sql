-- 코드를 입력하세요
SELECT animal_ins.animal_id, animal_ins.name
from animal_ins
left join animal_outs
on animal_ins.animal_id = animal_outs.animal_id
order by (animal_outs.datetime - animal_ins.datetime) desc
limit 2

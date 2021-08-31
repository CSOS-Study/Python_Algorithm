-- 코드를 입력하세요
with distinct_user as
(
SELECT host_id
from places
group by host_id
having count(host_id) >=2
)
select id, name, places.host_id
from places
right join distinct_user
on distinct_user.host_id = places.host_id
order by id

## left join이랑 right join이 헷갈린다. 왜지?
-- Inner Join : Table A와 Table B의 교집합을 조회
-- Outer Join : Table A와 Table B의 합집합을 조회(null이 포함된다.)
-- 레프트 조인은 왼쪽이 기준이기 때문에, 왼쪽 테이블의 데이터가 모두 나온다는 것이 보장된다.
-- 그리고 라이트 조인은 이하동문

--
-- 이번 문제에서는 distinct_user를 기준으로 교집합을 더하는 것이 문제였다. 그래서
-- from place left join distinct_user -> 이것은 왼쪽이 place가 되어서 place에 있는 데이터가 모두 나온다.

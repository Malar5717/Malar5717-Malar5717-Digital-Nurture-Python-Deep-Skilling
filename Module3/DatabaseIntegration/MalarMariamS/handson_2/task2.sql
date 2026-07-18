-- 20
select *
from students
where enrollment_year=2022
order by last_name;

-- 21
select *
from courses
where credits>3
order by credits desc;

-- 22
select *
from professors
where salary between 80000.00 and 950000.00;

-- 23
select *
from students
where email like '%college.edu';

-- 24
select count(*), enrollment_year
from students
group by enrollment_year
order by enrollment_year;
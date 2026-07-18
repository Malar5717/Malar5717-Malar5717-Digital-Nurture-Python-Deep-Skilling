-- 30
select c.course_name, count(e.enrollment_id) as enrollment_count
from courses c
left join enrollments e
on c.course_id = e.course_id
group by c.course_name;

-- 31
select d.dept_name, round(avg(p.salary), 2) as avg_salary
from departments d
join professors p
on d.department_id = p.department_id
group by d.dept_name;

-- 32
select dept_name, budget
from departments 
where budget>600000

-- 33
select grade, count(*) as grade_count
from enrollments e
join courses c 
on e.course_id = c.course_id
where c.course_code = 'CS101'
group by grade;

-- 34
select d.dept_name, count(e.student_id) as total_students_enrolled
from departments d
join courses c on d.department_id = c.department_id
join enrollments e on c.course_id = e.course_id
group by d.dept_name
having count(e.student_id) > 2;
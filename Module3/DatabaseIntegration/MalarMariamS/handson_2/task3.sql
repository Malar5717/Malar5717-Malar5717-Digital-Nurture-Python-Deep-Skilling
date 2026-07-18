-- 25
select concat(s.first_name, ' ', s.last_name) as full_name, d.dept_name
from students s
join departments d
on s.department_id = d.department_id;

-- 26
select e.enrollment_id, e.enrollment_date, e.grade, concat(s.first_name, ' ', 'last_name') as full_name, c.course_name
from enrollments e 
join students s on e.student_id = s.student_id
join courses c on e.course_id = c.course_id;

-- 27
select *
from students s
left join enrollments e 
on s.student_id = e.student_id
where e.enrollment_id is null;

-- 28
select c.course_id, c.course_name, c.course_code, count(e.student_id) as no_of_students
from courses c
left join enrollments e
on c.course_id = e.course_id
group by c.course_id, c.course_name, c.course_code;

-- 29
select d.department_id, d.dept_name, p.prof_name, p.salary 
from departments d
left join professors p 
on d.department_id = p.department_id;
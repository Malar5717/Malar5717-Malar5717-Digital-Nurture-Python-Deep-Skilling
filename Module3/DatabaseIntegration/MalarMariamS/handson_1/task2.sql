-- 1NF Compliance: Every column holds strictly atomic (indivisible) values. 
--     If a student had multiple phone numbers stored in a single comma-separated 
--     string, it would violate 1NF. Here, all entries are distinct and singular.
    
-- 2NF Compliance: The schema satisfies 1NF, and all non-key columns depend entirely 
--     on their table's primary key. In the enrollments table, columns like 
--     enrollment_date and grade depend fully on the primary key enrollment_id 
--     (or the composite candidate key student_id + course_id).
    
-- 3NF Compliance: There are no transitive dependencies. Non-key columns depend 
--     only on the primary key, not on other non-key columns. For instance, 
--     storing dept_name inside the students table would violate 3NF because 
--     dept_name depends on department_id, which depends on student_id. Keeping 
--     departments isolated prevents redundant update anomalies.
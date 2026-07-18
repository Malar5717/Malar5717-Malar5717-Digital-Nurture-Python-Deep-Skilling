-- 10
ALTER TABLE students ADD COLUMN phone_number VARCHAR(15);

-- 11
ALTER TABLE courses ADD COLUMN max_seats INT DEFAULT 60;

-- 13
ALTER TABLE enrollments
ADD CONSTRAINT check_grade
CHECK (grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL);

-- 14
ALTER TABLE students 
DROP COLUMN phone_number;
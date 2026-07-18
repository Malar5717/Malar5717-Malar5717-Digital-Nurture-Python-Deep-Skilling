create type grade as enum ('A', 'B', 'C', 'D', 'F');

-- create departments table
create table departments (
	department_id SERIAL PRIMARY KEY,
	dept_name VARCHAR(100) NOT NULL,
	hod_name VARCHAR(100),
	budget DECIMAL(12, 2)
);

-- create students table with foreign key reference to departments
create table students (
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	date_of_birth DATE,
	enrollment_year INT,
	department_id INT,
	constraint fk_stud_dept
		FOREIGN KEY (department_id)
		REFERENCES departments(department_id)
);

-- create courses table with foreign key reference to departments
create table courses (
	course_id SERIAL PRIMARY KEY,
	course_name VARCHAR(150) NOT NULL,
	course_code VARCHAR(20) UNIQUE,
	credits INT,
	department_id INT,
	constraint fk_cour_dept
		FOREIGN KEY (department_id)
		REFERENCES departments(department_id)
);

-- create enrollments table with foreign key references to students and courses
create table enrollments (
	enrollment_id SERIAL PRIMARY KEY,
	enrollment_date DATE,
	grade grade NULL,
	student_id INT NOT NULL,
	course_id INT NOT NULL,
	constraint fk_enrl_stude
		FOREIGN KEY (student_id)
		REFERENCES students(student_id),
	constraint fk_enrl_cour
		FOREIGN KEY (course_id)
		REFERENCES courses(course_id)
);

-- create professors table with foreign key reference to departments
create table professors (
	professor_id SERIAL PRIMARY KEY,
	prof_name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE,
	salary DECIMAL(10, 2),
	department_id INT,
	constraint fk_prof_dept
		FOREIGN KEY (department_id)
		REFERENCES departments(department_id)
);

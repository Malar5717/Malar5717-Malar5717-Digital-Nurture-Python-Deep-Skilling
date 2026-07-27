from sqlalchemy.orm import sessionmaker, joinedload
from models import engine, Enrollment

Session = sessionmaker(bind=engine)
session = Session()

try:
    print("\n================ Step 88 & 89: Eager Loading with joinedload ================")
    
    # Query using joinedload to fetch student and course in a single query
    enrollments = (
        session.query(Enrollment)
        .options(
            joinedload(Enrollment.student),
            joinedload(Enrollment.course)
        )
        .all()
    )

    print("\n--- Processing Results ---")
    for enrollment in enrollments:
        student_name = f"{enrollment.student.first_name} {enrollment.student.last_name}"
        course_name = enrollment.course.course_name
        print(f"Student: {student_name} | Course: {course_name} | Semester: {enrollment.semester}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    session.close()

"""
1. WITHOUT joinedload (Lazy Loading - Task 2 Step 84):
   - Total SQL Queries Issued: 13 (or 1 + 2N queries)
   - Reason: 1 initial SELECT query on enrollment table, followed by N separate 
     SELECT queries for student and N separate SELECT queries for course 
     as each row is accessed in the loop.

2. WITH joinedload (Eager Loading - Task 3 Step 88):
   - Total SQL Queries Issued: 1
   - Reason: SQLAlchemy generates a SINGLE SQL query using LEFT OUTER JOINs 
     to fetch enrollment, student, and course tables together at once.
"""
from sqlalchemy.orm import sessionmaker
from models import engine,Department,Student,Professor,Course,Enrollment

Session=sessionmaker(bind=engine)
session=Session()
try:
    # dept1=Department(dept_name="Computer Science", head_of_dept="Dr. Malar", budget=500000)
    # dept2=Department(dept_name="Electrical Engineering", head_of_dept="Dr. Sajetha", budget=400000)
    # dept3=Department(dept_name="Mechanical Engineering", head_of_dept="Dr. Meaw", budget=350000)

    # session.add_all([dept1,dept2,dept3])
    # session.commit()

    # print("Deptartments added")

    # students=[
    #     Student(first_name="Harry", last_name="K", email="harry@example.com", dept_id=dept1.dept_id),
    #     Student(first_name="Blackberry", last_name="TS", email="blackberry@example.com", dept_id=dept1.dept_id),
    #     Student(first_name="Kritree", last_name="kree", email="kritree@example.com", dept_id=dept2.dept_id),
    #     Student(first_name="Nira", last_name="charm", email="nira@example.com", dept_id=dept2.dept_id),
    #     Student(first_name="meap", last_name="mop", email="meap@example.com", dept_id=dept3.dept_id)
    # ]
    # session.add_all(students)
    # session.commit()
    # print("Students added")

# --------- NEXT SUB TASK 

    # course1 = Course(course_code="CS101", course_name="Intro to CS", credits=4)
    # course2 = Course(course_code="EE101", course_name="Circuits", credits=3)
    # course3 = Course(course_code="ME101", course_name="Thermodynamics", credits=4)

    # session.add_all([course1, course2, course3])
    # session.commit()

    # Fetch existing students to link
    # s1 = session.query(Student).filter_by(email="harry@example.com").first()
    # s2 = session.query(Student).filter_by(email="blackberry@example.com").first()
    # s3 = session.query(Student).filter_by(email="kritree@example.com").first()
    # s4 = session.query(Student).filter_by(email="nira@example.com").first()

    # enrollments = [
    #     Enrollment(student_id=s1.student_id, course_id=course1.course_id, semester="2025-ODD", grade="A"),
    #     Enrollment(student_id=s2.student_id, course_id=course1.course_id, semester="2025-ODD", grade="B"),
    #     Enrollment(student_id=s3.student_id, course_id=course2.course_id, semester="2025-ODD", grade="A"),
    #     Enrollment(student_id=s4.student_id, course_id=course3.course_id, semester="2025-ODD", grade="C"),
    # ]
    # session.add_all(enrollments)
    # session.commit()
    # print("Courses and Enrollments added successfully!")

#  ---------------- NEXT SUB TASK
    # cs_students = (
    #     session.query(Student)
    #     .join(Department)
    #     .filter(Department.dept_name == "Computer Science")
    #     .all()
    # )

    # for student in cs_students:
    #     print(f"ID: {student.student_id} | Name: {student.first_name} {student.last_name} | Email: {student.email}")

# ---------------- NEXT SUB TASK
    # all_enrollments = session.query(Enrollment).all()

    # for enrollment in all_enrollments:
    #     student_name = f"{enrollment.student.first_name} {enrollment.student.last_name}"
    #     course_name = enrollment.course.course_name
    #     print(f"Student: {student_name} | Course: {course_name} | Semester: {enrollment.semester}")

# ------------------NEXT SUB TASK
    # target_student = session.query(Student).filter(Student.email == "harry@example.com").first()
    # if target_student:
    #     target_student.last_name = "HP"
    #     session.commit()
    #     print(f"Updated student: {target_student.first_name} {target_student.last_name}")

# --------------- NEXT SUB TASK 
    enrollment_to_delete = session.query(Enrollment).first()
    if enrollment_to_delete:
        session.delete(enrollment_to_delete)
        session.commit()
        print("Successfully deleted 1 enrollment record.")
        
        remaining_count = session.query(Enrollment).count()
        print(f"Remaining Enrollments Count: {remaining_count}")
        

except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()

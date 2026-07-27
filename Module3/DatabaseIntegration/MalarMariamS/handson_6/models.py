from datetime import datetime
from sqlalchemy import create_engine,Column,Integer,String,Numeric,Date,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

DB_Url="mysql+mysqlconnector://root:malar123@localhost:3306/college_db_orm"
engine = create_engine(DB_Url, echo=True)
Base=declarative_base()
# try:
#     with engine.connect() as conn:
#         print("Connected successfully to MySQL!")
# except Exception as e:
#     print(f"Connection failed: {e}")

class Department(Base):
    __tablename__='department'

    dept_id=Column(Integer,primary_key=True,autoincrement=True)
    dept_name=Column(String(50),nullable=False)
    head_of_dept=Column(String(50))
    budget=Column(Integer)

    students=relationship('Student',back_populates='department')
    professors=relationship('Professor',back_populates='department')

class Student(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    dept_id = Column(Integer, ForeignKey('department.dept_id'))

    department = relationship('Department', back_populates='students')
    enrollments = relationship('Enrollment', back_populates='student')

class Professor(Base):
    __tablename__ = 'professor'

    prof_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    dept_id = Column(Integer, ForeignKey('department.dept_id'))

    department = relationship('Department', back_populates='professors')
    courses = relationship('Course', back_populates='professor')

class Course(Base):
    __tablename__ = 'course'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_code = Column(String(20), unique=True, nullable=False)
    course_name = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False)
    prof_id = Column(Integer, ForeignKey('professor.prof_id'))

    # Relationships
    professor = relationship('Professor', back_populates='courses')
    enrollments = relationship('Enrollment', back_populates='course')

class Enrollment(Base):
    __tablename__ = 'enrollment'

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.student_id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)
    semester = Column(String(20), nullable=False)
    grade = Column(String(5))

    # Relationships
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')

if __name__ == "__main__":
    print("Creating tables in college_db_orm...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")
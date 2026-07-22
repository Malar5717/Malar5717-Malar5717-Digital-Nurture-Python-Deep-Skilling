from flask import Blueprint, jsonify, request
from extensions import db
from courses.models import Department, Student, Course, Enrollment

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses');

# # temp
# COURSES_DATA = []

def make_response_json(data, status_code):
    envelope = {
        'status': 'success',
        'data': data
    }
    return jsonify(envelope), status_code


@courses_bp.route('/', methods=['GET'])
def get_all_courses():
    # return jsonify(COURSES_DATA), 200
    courses = Course.query.all()
    serialized_courses = [course.to_dict() for course in courses]
    return make_response_json(serialized_courses, 200)


@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()

    if data is None:
        return jsonify({'status': 'error', 'message': 'Invalid JSON data format'}), 400
    
    # required_fields = ['name', 'code', 'credits']
    required_fields = ['name', 'code', 'credits', 'department_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'status': 'error', 'message': f'Missing required field: {field}'}), 400

    new_course = {
        # "id": len(COURSES_DATA) + 1,
        # "name": data.get("name", "UNKNOWN"),
        # "code": data.get("code", "UNKNOWN"),
        # "credits": data.get("credits", "UNKOWN"),
        Course(
            name=data['name'],
            code=data['code'],
            credits=data['credits'],
            department_id=data['department_id']
        )
    }

    # COURSES_DATA.append(new_course)
    db.session.add(new_course)
    db.session.commit()

    # success_data = {
    #     'message': 'Course validated successfully',
    #     'course': data
    # }
    # return make_response_json(success_data, 201)
    return make_response_json(new_course.to_dict(), 201)


@courses_bp.route('/<int:course_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_course(course_id):

    course = Course.query.get_or_404(course_id)

    if request.method == 'GET':
        return make_response_json(course.to_dict(), 200)

    if request.method == 'PUT':
        data = request.get_json()

        if data is None:
            return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400
        
        course.name = data.get('name', course.name)
        course.code = data.get('code', course.code)
        course.credits = data.get('credits', course.credits)
        course.department_id = data.get('department_id', course.department_id)

        return make_response_json(course.to_dict(), 200)

    if request.method == 'DELETE':
        db.session.delete(course)
        db.session.commit()

        delete_confirmation = {
            "message": f"Course with ID {course_id} has been deleted successfully"
        }
        return make_response_json(delete_confirmation, 200)


@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id):
    # verify it exists
    Course.query.get_or_404(course_id)

    enrolled_students = db.session.query(Student)\
        .join(Enrollment, Student.id == Enrollment.student_id)\
        .filter(Enrollment.course_id == course_id).all()

    serialized_students = [student.to_dict() for student in enrolled_students]
    return make_response_json(serialized_students, 200)


@courses_bp.errorhandler(404)
def not_found_error(error):
    return jsonify({'status': 'error', 'message': 'Resources not found'}), 404

@courses_bp.errorhandler(500)
def internal_error(error):
    return jsonify({'status': 'error', 'message': 'An internal server error occurred'}), 500
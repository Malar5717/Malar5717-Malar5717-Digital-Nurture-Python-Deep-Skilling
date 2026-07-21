from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses');
# temp
COURSES_DATA = []

@courses_bp.route('/', methods=['GET'])
def get_courses():
    return jsonify(COURSES_DATA), 200

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()

    new_course = {
        "id": len(COURSES_DATA) + 1,
        "name": data.get("name", "UNKNOWN"),
        "code": data.get("code", "UNKNOWN"),
        "credits": data.get("credits", "UNKOWN"),
    }
    COURSES_DATA.append(new_course)

    return jsonify(new_course), 201

def response(data):
    response = {
        'status': 'success',
        'data': data
    }

    return jsonify(response), 200

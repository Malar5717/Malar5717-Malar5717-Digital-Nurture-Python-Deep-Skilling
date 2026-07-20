from flask import Flask
from Module5.PythonBackendFrameworks.flask_project.flask_coursemanager.config import Config
from Module5.PythonBackendFrameworks.flask_project.flask_coursemanager.extensions import db, migrate
from Module5.PythonBackendFrameworks.flask_project.flask_coursemanager.courses.routes import courses_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # bind the app config, after app created
    db.init_app(app)
    migrate.init_app(app, db)

    from Module5.PythonBackendFrameworks.flask_project.flask_coursemanager.courses.models import Department, Course, Student, Enrollment

    app.register_blueprint(courses_bp)

    return app


if __name__=='__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
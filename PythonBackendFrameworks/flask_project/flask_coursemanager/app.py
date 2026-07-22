from flask import Flask
from config import Config
from extensions import db, migrate
from courses.routes import courses_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # bind the app config, after app created
    db.init_app(app)
    migrate.init_app(app, db)

    from courses.models import Department, Course, Student, Enrollment

    app.register_blueprint(courses_bp)

    return app


if __name__=='__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
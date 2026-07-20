from fastapi import FastAPI
from Module5.PythonBackendFrameworks.fastapi_project.schemas import CourseCreate, CourseResponse

app = FastAPI(title='Course Management API', version='1.0')

@app.get('/')
def read_root():
    return { "message": "API running" }

@app.post('/api/courses/')
async def create_course(course: CourseCreate):
    return { "message": "course created" }
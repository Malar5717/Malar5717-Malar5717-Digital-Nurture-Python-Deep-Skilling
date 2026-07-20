from pydantic import BaseModel
from typing import Optional, List

# reused
class CourseBase(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int

# all fields required
class CourseCreate(CourseBase):
    pass

# all fields optional
class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None

# base + id field
class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True

class DepartmentResponse(BaseModel):
    # department
    id: int
    name: str
    # courses
    courses: List[CourseResponse]

    class Config:
        from_attributes = True
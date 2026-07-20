from django.urls import path, include
from . import views
# from .views import CourseListView, CourseDetailView
from .views import CourseViewSet, StudentViewSet, EnrollmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('students', StudentViewSet)
router.register('enrollments', EnrollmentViewSet)

# urlpatterns = [
#     path('hello/', views.hello_view, name='hello'),
#     path('courses/', CourseListView.as_view(), name='course-list'),
#     path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
# ]

urlpatterns = [
    path('', include(router.urls))
]
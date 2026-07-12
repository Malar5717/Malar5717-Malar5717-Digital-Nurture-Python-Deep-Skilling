from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status

from .models import Course, Student, Enrollment
from .serializers import CourseSerializer, StudentSerializer, EnrollmentSerializer

from rest_framework.decorators import action

def hello_view(req):
    return HttpResponse('Course Management API is running.')


# class CourseListView(APIView):
#     def get(self, req):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True) # List of JSON
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, req):
#         serializer = CourseSerializer(data=req.data) # get input
#         if serializer.is_valid(): # auto validate
#             serializer.save() # new row created
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CourseDetailView(APIView):
    def get(self, req, pk): # pk - primary key
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, req, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=req.data) # overwrite
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, req, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def students(self, req, pk):
        course = get_object_or_404(Course, pk=pk)

        enrollments = Enrollment.objects.filter(course=course)
        students = [enrollment.student for enrollment in enrollments]

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer



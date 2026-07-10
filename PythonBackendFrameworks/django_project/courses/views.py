from django.http import HttpResponse

def hello_view(req):
    return HttpResponse('Course Management API is running.')
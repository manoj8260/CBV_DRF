from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404 
from rest_framework import status
# Create your views here.


class CoursesListView(APIView):
    def get(self,request):
        courses=Courses.objects.all()
        serializers=CoursesSerializers(courses,many=True)
        return Response(serializers.data)

    def post(self,request):
        coursesSerializers=CoursesSerializers(data=request.data)
        if coursesSerializers.is_valid():
            coursesSerializers.save()
            return Response(coursesSerializers.data)
        return Response(coursesSerializers.errors)

class CoursesDetailsView(APIView):
    def get_objects(self,pk):
        try:
            return  Courses.objects.get(pk=pk)
        except Courses.DoesNotExist:
            raise  Http404

    def get(self,request,pk,format=None):      
        serializers=CoursesSerializers(self.get_objects(pk))
        return Response(serializers.data)
    
    def put(self,request,pk,format=None):
        course=self.get_objects(pk)
        serializers=CoursesSerializers(course,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_403_FORBIDDEN)
        
    def delete(self,request,pk,format=None):
         course=self.get_objects(pk)
         course.delete()
         return Response({"message":f'course {course.name} deleted successfully'},status=status.HTTP_205_RESET_CONTENT)
        
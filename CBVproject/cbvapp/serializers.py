from rest_framework import serializers
from .models import *
class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courses
        # fields=['name','author','price','discount','duration']
        fields='__all__'

from django.db import models

# Create your models here.
class  Courses(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    discount=models.IntegerField(default=0)
    duration=models.FloatField()

    def __str__(self):
        return self.name
    
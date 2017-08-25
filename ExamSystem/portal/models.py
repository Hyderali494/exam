from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    course = models.CharField(max_length = 250)
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.course	
    
class Question(models.Model):
    question = models.CharField(max_length = 1000)
    c1 = models.CharField(max_length = 500)
    c2 = models.CharField(max_length = 500)
    c3 = models.CharField(max_length = 500)
    c4 = models.CharField(max_length = 500)
    answer = models.CharField(max_length = 500)
    status = models.CharField(max_length = 500)
    course = models.ForeignKey(Course)
    

    def __str__(self):
        return self.question+" "+self.answer

    

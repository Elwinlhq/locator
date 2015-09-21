from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# TO REVIEW THE SQL python manage.py sql geld
class Bar(models.Model):
    name        = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    user        = models.ForeignKey(User)
    
    def __str__(self):
        return "(id=" + self.id.__str__() + ") " + self.name

class Comment(models.Model):
    text = models.CharField(max_length=100)
    bar  = models.ForeignKey(Bar)
    user = models.ForeignKey(User)

    def __str__(self):
        return "(id=" + self.id.__str__() + ") " + self.text        
        
admin.site.register(Bar)
admin.site.register(Comment)

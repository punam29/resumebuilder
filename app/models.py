from django.db import models

# Create your models here.


class Resume(models.Model):
    summary=models.TextField()
    name=models.CharField(max_length=100)
    phoneno=models.IntegerField()
    emailid=models.CharField(max_length=100)
    skills=models.TextField()
    designation=models.CharField(max_length=100)
    jobdescription=models.TextField()
    yearsofexperience=models.IntegerField()
    schoolname=models.CharField(max_length=100)
    schoolduration=models.CharField(max_length=100)
    collegename=models.CharField(max_length=100)
    collegeduration=models.CharField(max_length=100)




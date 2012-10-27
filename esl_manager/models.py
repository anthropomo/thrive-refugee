from django.db import models
import datetime

# Create your models here.

class ESLStudent(models.Model):
    FirstName = models.CharField("First Name",  max_length=50)
    LastName = models.CharField("Last Name", max_length=80)
    StreetAddress = models.CharField("Address", max_length=50)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=2)
    Zip = models.CharField(max_length=10)
    Phones = models.CharField(max_length=50)
    
    
    def __unicode__(self):
        return self.FirstName

class Attended(models.Model):
    esl_tudent = models.ForeignKey(ESLStudent)
    attend_date = models.DateField('Attended')

    def __unicode__(self):
        return self.attend_date


class Assesment(models.Model):
    esl_tudent = models.ForeignKey(ESLStudent)
    taken_date = models.DateField('Taken')
    Score = models.IntegerField()

    def __unicode__(self):
        return self.taken_date
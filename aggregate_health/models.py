from django.db import models

# Create your models here.
class PrimaryCareProvider(models.Model):
    firstName = models.CharField(max_length=200, null=False, blank=False)
    lastName = models.CharField(max_length=200, null=False, blank=False)
    npi = models.IntegerField(null=False)
    clinicSite = models.IntegerField(null=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName + " " + self.lastName



class Patient(models.Model):
    firstName = models.CharField(max_length=200, null=False, blank=False)
    lastName = models.CharField(max_length=200, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)   
    gender = models.CharField(max_length=1)
    primarycareprovider = models.ForeignKey(PrimaryCareProvider, null=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName + " " + self.lastName + " - " + str(self.date_of_birth)

class VisitTypes(models.Model):
    name = models.CharField(max_length=99, null=False, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Encounter(models.Model):
    patient = models.ForeignKey(Patient, null=False)
    visit_type = models.ForeignKey(VisitTypes, null=False)
    date_performed = models.DateField(auto_now=False, null=False)
    provider = models.ForeignKey(PrimaryCareProvider, null=False)
        
        
class Condition(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    code = models.CharField(max_length=20)

class ProblemList(models.Model):
    patient = models.ForeignKey(Patient, null=False)
    condition = models.ForeignKey(Condition)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    active = models.BooleanField(default=True)

    def inactivate(self):
        if end_date:
            self.active = False


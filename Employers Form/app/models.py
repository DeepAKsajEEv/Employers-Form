from django.db import models

# Create your models here.
class Employee(models.Model):


    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=25, unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    date_of_birth = models.DateField(max_length=8)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    professional_skills = models.CharField(max_length=200)
    photo =models.ImageField(null = True, blank=True, upload_to = 'images/')


    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname
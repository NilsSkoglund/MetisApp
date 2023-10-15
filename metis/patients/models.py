from django.db import models


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    MALE = 'M'
    FEMALE = 'F'
    NON_BINARY = "NB"
    UNKNOWN = 'X'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BINARY, "Non-binary"),
        (UNKNOWN, 'Unknown'),
    ]

    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    description = models.TextField(max_length=200)
    history = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    medication = models.CharField(max_length=200)

from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

MARITAL_STATUS_CHOICES = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
)

#Model to record patients demographics
class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    phone_number = PhoneNumberField(help_text='Contact phone number')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS_CHOICES)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

#Model to record patients vitals at the time of visit
class PatientVitals(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    body_temperature = models.DecimalField(max_digits=4, decimal_places=2)
    heart_rate = models.PositiveIntegerField()
    blood_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_visit = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.patient.user.first_name} {self.patient.user.last_name}'



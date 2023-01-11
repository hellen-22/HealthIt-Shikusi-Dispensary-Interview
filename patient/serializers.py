from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import serializers


from .models import *
from accounts.models import User


#Serializer to simplify and display user details to be used for patient registration
class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=50)
    confirm_password = serializers.CharField(write_only=True, max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']


#Registration of Patients
class PatientRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'user', 'age', 'phone_number', 'gender', 'marital_status']
    
    
    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']

            if password == confirm_password:

                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])

                patient = Patient.objects.create(user=user, age=self.validated_data['age'], phone_number=self.validated_data['phone_number'], gender=self.validated_data['gender'], marital_status=self.validated_data['marital_status'])

                return patient
            else:
                raise serializers.ValidationError('Passwords do not match')


"""Serializer that enables addition of patients vitals at time of visit"""
class PatientVitalsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        patient_id = self.context['patient_id']

        patient = Patient.objects.get(pk=patient_id)

        patient_vitals = PatientVitals.objects.create(patient=patient, **self.validated_data)

        return patient_vitals
    class Meta:
        model = PatientVitals
        fields = ['id','body_temperature', 'heart_rate', 'blood_pressure', 'date_of_visit']
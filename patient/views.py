from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import *
from .serializers import *

# Create your views here.

"""Api view for adding, updating, deleting and listing patients"""
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientRegistrationSerializer
    #permission_classes = [IsAdminUser]

"""Api view for adding, updating, deleting and listing patients vitals"""
class PatientVitalsViewSet(viewsets.ModelViewSet):
    serializer_class = PatientVitalsSerializer

    def get_serializer_context(self):
        return {'patient_id': self.kwargs['patient_pk']}

    def get_queryset(self):
        return PatientVitals.objects.filter(patient_id=self.kwargs['patient_pk'])
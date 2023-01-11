from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

# Create your views here.

"""Api view for adding, updating, deleting and listing patients"""
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientRegistrationSerializer
    #permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['age', 'marital_status', 'gender']

"""Api view for adding, updating, deleting and listing patients vitals"""
class PatientVitalsViewSet(viewsets.ModelViewSet):
    serializer_class = PatientVitalsSerializer
    #permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['body_temperature']

    def get_serializer_context(self):
        return {'patient_id': self.kwargs['patient_pk']}

    def get_queryset(self):
        return PatientVitals.objects.filter(patient_id=self.kwargs['patient_pk'])
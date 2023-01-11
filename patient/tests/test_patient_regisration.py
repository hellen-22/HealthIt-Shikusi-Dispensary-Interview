import pytest
from model_bakery import baker
from rest_framework import status


from accounts.models import *
from patient.models import *

@pytest.fixture
def create_patient(api_client):
    def create(patient):
        return api_client.post("/patient/", patient, format='json')
    return create

@pytest.fixture
def update_patient(api_client):
    def update(patient):
        patient_sample = baker.make(Patient)
        return api_client.patch(f'/patient/{patient_sample.id}/', patient)
    return update


@pytest.fixture
def delete_patient(api_client):
    def delete():
        patient_sample = baker.make(Patient)
        return api_client.delete(f'/patient/{patient_sample.id}/')
    return delete


@pytest.mark.django_db
class TestCreatePatient():
    def test_data_is_invalid_return_400(self, authenticate_user, create_patient):
        authenticate_user()
        
        patient = {
            "user": {
                "username": "Hellen",
                "first_name": "Hellen",
                "last_name": "Wain",
                "email": "",
                "phone_number" : "",
                "password": "password"
            },
            "confirm_password": "password",
            "age": 22,
            "gender": "",
            "marital_status": "Single"
        }

        response = create_patient(patient)

        assert response.status_code == status.HTTP_400_BAD_REQUEST




@pytest.mark.django_db
class TestUpdatePatient():
    
    def test_if_data_is_invalid_return_400(self, authenticate_user, update_patient):
        authenticate_user()

        user = baker.make(User)
        patient = {
            "user": user.id,
            "confirm_password": "password",
            "age": 22,
            "gender": "",
            "marital_status": "Single"
        }

    
        response = update_patient(patient)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
class TestDeletePatient():
    def test_if_is_admin_return_200(self, delete_patient, authenticate_user):
        authenticate_user()

        response = delete_patient()

        assert response.status_code == status.HTTP_204_NO_CONTENT

from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('patient', views.PatientViewSet, basename='patient')

"""Nesting to enable addition of patient vitals under an existing patient"""
patient_router = routers.NestedDefaultRouter(router, 'patient', lookup='patient')

patient_router.register('vitals', views.PatientVitalsViewSet, basename='vitals')

urlpatterns = router.urls + patient_router.urls
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls 
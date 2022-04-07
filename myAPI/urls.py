from django.urls import include, path
from rest_framework import routers
from . import views

router = router.DefaultRouter()
router.register('vehicls', views.vehiclviewset)

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
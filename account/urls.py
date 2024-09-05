from rest_framework import routers
from .views import ClientViewSet


route =routers.DefaultRouter()
route.register(r'client',ClientViewSet)

urlpatterns = route.urls
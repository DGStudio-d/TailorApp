from rest_framework import routers


route =routers.DefaultRouter()
route.register(r'usres')

urlpatterns = route.urls
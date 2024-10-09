from django.urls import include, path
from rest_framework import routers

from api.views import PostModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'post', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

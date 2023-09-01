from django.urls import path
from .views import AloqaSerializerAPI

urlpatterns = [
    path('api/', AloqaSerializerAPI.as_view())
]
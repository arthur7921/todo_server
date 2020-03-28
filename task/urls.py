from django.urls import path
from .views import TaskViewSet
urlpatterns = [
    path('task/', TaskViewSet.as_view({'get': 'list', 'post':'create', 'delete': 'destroy'})),
]
from django.conf.urls import url
from django.urls import path
from .views import TaskViewSet, UserTag
urlpatterns = [
    path('task/', TaskViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path('task/<int:pk>', TaskViewSet.as_view({'delete': 'destroy', 'put': 'update'})),
    url('user-tag/', UserTag.as_view()),
]
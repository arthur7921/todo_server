import django_filters
from rest_framework.viewsets import mixins, GenericViewSet
from django_filters import FilterSet
from .models import Task
from .serializers import TaskModelSerializers
# Create your views here.


class TaskFilter(FilterSet):
    userTag = django_filters.CharFilter(field_name='userTag')
    class Meta:
        model = Task  # 关联的模型
        fields = ['userTag']


class TaskViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = TaskModelSerializers
    queryset = Task.objects.all()
    filter_fields = ['userTag']
    filterset_class = TaskFilter

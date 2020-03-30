import django_filters
from django.db.models import Max
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from django_filters import FilterSet
from .models import Task
from .serializers import TaskModelSerializers
from rest_framework.views import APIView
from django_filters import rest_framework as filters
# Create your views here.


class TaskFilter(FilterSet):
    # userTag = django_filters.NumberFilter(field_name='userTag', look_expr='exact')
    class Meta:
        model = Task  # 关联的模型
        fields = ['userTag']


class TaskViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = TaskModelSerializers
    queryset = Task.objects.all()
    # filterset_class = TaskFilter
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('userTag',)


class UserTag(APIView):
    def get(self, request):
        return Response(Task.objects.all().aggregate(Max('userTag')) + 1)
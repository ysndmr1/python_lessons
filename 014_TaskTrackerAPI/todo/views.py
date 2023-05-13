from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer, Todo


class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

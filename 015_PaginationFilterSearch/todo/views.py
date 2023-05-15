from rest_framework.viewsets import ModelViewSet
from .serializers import Todo, TodoSerializer

# Alternatif geçici yöntem:
# from rest_framework.pagination import PageNumberPagination


from .paginations import (
    CustomPageNumberPagination,
    CustomLimitOffsetPagination,
    CustomCursorPagination
)


class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomCursorPagination  # Local Setting.

    # Alternatif geçici (veya sadece bu class için çalışan) yöntem:
    # pagination_class = PageNumberPagination
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_size_query_param = 'adet' # URL ile kaç adet gösterileceğini belirleyebilirim
    # PageNumberPagination.page_query_param = 'sayfa' # aktif sayfa numarası için "page" yerinde başka bir isim kullanabilirim.

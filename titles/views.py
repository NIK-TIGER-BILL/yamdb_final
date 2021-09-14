from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from titles.models import Title, Category, Genre
from .permissions import IsAdminUserOrReadOnly
from .serializers import (TitleSerializer, CategorySerializer,
                          GengreSerializer, TitlePostSerializer)
from .filters import TitleFilter


class MyMixin(mixins.CreateModelMixin,
              mixins.ListModelMixin,
              mixins.DestroyModelMixin,
              viewsets.GenericViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleSerializer
        return TitlePostSerializer


class CategoryViewSet(MyMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'


class GenreViewSet(MyMixin):
    queryset = Genre.objects.all()
    serializer_class = GengreSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'

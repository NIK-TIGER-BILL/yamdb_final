from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .permission import IsAdminOrModerUser, IsOwnerOrReadOnly
from reviews.models import Review
from titles.models import Title
from .serializers import ReviewSerializer, CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes_by_action = {'destroy': [IsAdminOrModerUser]}
    pagination_class = PageNumberPagination

    def get_permissions(self):
        try:
            return (permission() for permission in
                    self.permission_classes_by_action[self.action])
        except KeyError:
            return (permission() for permission in self.permission_classes)

    def get_queryset(self):
        title_id = self.request.parser_context['kwargs'].get('title_id')
        title = get_object_or_404(Title, id=title_id)
        queryset = title.review.all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.request.parser_context['kwargs'].get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(title_id=title, author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes_by_action = {'destroy': [IsAdminOrModerUser]}
    pagination_class = PageNumberPagination

    def get_permissions(self):
        try:
            return (permission() for permission in
                    self.permission_classes_by_action[self.action])
        except KeyError:
            return (permission() for permission in self.permission_classes)

    def get_queryset(self):
        title_id = self.request.parser_context['kwargs'].get('title_id')
        review_id = self.request.parser_context['kwargs'].get('review_id')
        review = get_object_or_404(Review, id=review_id, title_id=title_id)
        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.request.parser_context['kwargs'].get('title_id')
        review_id = self.request.parser_context['kwargs'].get('review_id')
        review = get_object_or_404(Review, id=review_id, title_id=title_id)
        serializer.save(review_id=review, author=self.request.user)

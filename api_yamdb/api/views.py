from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, mixins
from .permissions import ReviewCommentPermissions
from reviews.models import Category, Genre, Title, Review
from rest_framework.pagination import LimitOffsetPagination
from users.permissions import IsAdminOrReadOnly
from api.serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer
)


class CategoriesViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenresViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'category__slug', 'genre__slug', 'year')
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        category = get_object_or_404(
            Category,
            slug=self.request.data['category']
        )
        genres = []
        slugs = self.request.data['genre']
        for slug in slugs:
            genre = get_object_or_404(Genre, slug=slug)
            genres.append(genre)
        serializer.save(category=category, genre=genres)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [ReviewCommentPermissions]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        new_queryset = Title.objects.filter(title=title_id)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [ReviewCommentPermissions]

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        new_queryset = Review.objects.filter(review=review_id)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination

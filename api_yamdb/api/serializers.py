from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Category, Genre, Title, Comment, Review


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        read_only=True
    )
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        read_only=True
    )

    class Meta:
        fields = ('id', 'category', 'genre', 'name', 'year', 'description')
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзывов."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    def validate(self, data):
        title_id = self.context['view'].kwargs['title_id']
        title = get_object_or_404(Title, pk=title_id)
        if (self.context['view'].request.method == 'POST'
                and title.review_titles.filter(
                    author=self.context['request'].user).exists()):
            raise serializers.ValidationError(
                'Нельзя добавить второй отзыв на одно произведение.')
        return data

    class Meta:
        model = Review

        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        read_only_fields = ('author',)
        validators = []


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date')
        model = Comment

    
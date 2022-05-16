from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
import datetime as dt
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
        queryset=Genre.objects.all(),
        many=True,
        slug_field='slug',
    )

    def validate(self, data):
        try:
            slug = self.context['request'].data.get('category')
            category = Category.objects.get(slug=slug)
            data['category'] = category
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Категории нет в базе данных!')
        try:
            genres = []
            slugs = self.context['request'].data.getlist('genre')
            for slug in slugs:
                genre = Genre.objects.get(slug=slug)
                genres.append(genre)
            data['genre'] = genres
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Жанра нет в базе данных!')
        return data

    def validate_year(self, value):
        year = dt.date.today().year
        if not (value <= year):
            raise serializers.ValidationError('Произведение из будущего?')
        return value

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)
        title.genre.set(genres)
        return title

    class Meta:
        fields = (
            'id', 'category', 'genre', 'name', 'year', 'description', 'rating'
        )
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзывов."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('title', 'author'),
                message='Нельзя оставить больше одного отзыв'
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = '__all__'
        model = Comment

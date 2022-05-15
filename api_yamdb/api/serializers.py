from rest_framework import serializers

from reviews.models import Category, Genre, Title


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
from rest_framework import serializers

from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'slug'),
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):

    category = CategorySerializer(
        many=True,
        read_only=True

    )
    genre = GenreSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        fields = ('id', 'category', 'genre', 'name', 'year', 'description')
        model = Title

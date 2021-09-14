from rest_framework import serializers
from django.db.models import Avg

from titles.models import Title, Category, Genre
from reviews.models import Review


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Category


class GengreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = GengreSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Title

    def get_rating(self, obj):
        score_avg = (Review.objects.filter(title_id=obj.id).
                     aggregate(Avg('score'))['score__avg'])
        if score_avg is None:
            rating = None
        else:
            rating = round(score_avg, 0)
        return rating


class TitlePostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug', )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True)

    class Meta:
        fields = '__all__'
        model = Title

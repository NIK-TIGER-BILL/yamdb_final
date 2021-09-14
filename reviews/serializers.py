from titles.models import Title
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from reviews.models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    title_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, data):
        if self.context['request'].method == 'POST':
            title_id = (self.context['request'].parser_context['kwargs'].
                        get('title_id'))
            author = self.context['request'].user
            current_title = get_object_or_404(Title, id=title_id)
            if current_title.review.filter(author=author).exists():
                raise serializers.ValidationError('Отзыв на это произведение '
                                                  'уже существует')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    review_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'review_id', 'text', 'author', 'pub_date')
        model = Comment

    def validate(self, data):
        if self.context['request'].method == 'POST':
            title_id = (self.context['request'].parser_context['kwargs'].
                        get('title_id'))
            current_title = get_object_or_404(Title, id=title_id)

            review_id = (self.context['request'].parser_context['kwargs'].
                         get('review_id'))
            current_review = get_object_or_404(Review, id=review_id)

            if (
                (not current_review.comments.filter(review_id=review_id).
                 exists())
                and not current_title.review.filter(title_id=title_id).exists()
            ):
                raise serializers.ValidationError('Пост или отзыв отсутствует')
        return data

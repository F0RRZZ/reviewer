import rest_framework.serializers

import rating.models


base_fields = [
    rating.models.Rating.story.field.name,
    rating.models.Rating.acting.field.name,
    rating.models.Rating.music.field.name,
    rating.models.Rating.visual.field.name,
    rating.models.Rating.final.field.name,
    rating.models.Rating.total_rating.field.name,
    rating.models.Rating.comment.field.name,
    rating.models.Rating.created_at.field.name,
]


class ReviewSerializerForMovies(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = rating.models.Rating
        fields = [rating.models.Rating.user.field.name] + base_fields


class ReviewSerializerForUsers(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = rating.models.Rating
        fields = [rating.models.Rating.movie.field.name] + base_fields

from rest_framework.serializers import ModelSerializer

from rating.models import Rating


base_fields = [
    Rating.story.field.name,
    Rating.acting.field.name,
    Rating.music.field.name,
    Rating.visual.field.name,
    Rating.final.field.name,
    Rating.total_rating.field.name,
    Rating.comment.field.name,
    Rating.created_at.field.name,
]


class ReviewSerializerForMovies(ModelSerializer):
    class Meta:
        model = Rating
        fields = [Rating.user.field.name] + base_fields


class ReviewSerializerForUsers(ModelSerializer):
    class Meta:
        model = Rating
        fields = [Rating.movie.field.name] + base_fields

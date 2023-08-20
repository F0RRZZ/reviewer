from rest_framework.serializers import ModelSerializer

from api.v1.genres.serializers import GenreSerializer
from api.v1.persons.serializers import PersonSerializer
from api.v1.reviews.serializers import ReviewSerializerForMovies
from movies.models import Movie


class MovieSerializer(ModelSerializer):
    actors = PersonSerializer(
        many=True,
        read_only=True,
    )
    director = PersonSerializer(
        many=True,
        read_only=True,
    )
    producer = PersonSerializer(
        many=True,
        read_only=True,
    )
    screenwriter = PersonSerializer(
        many=True,
        read_only=True,
    )
    operator = PersonSerializer(
        many=True,
        read_only=True,
    )
    composer = PersonSerializer(
        many=True,
        read_only=True,
    )
    artist = PersonSerializer(
        many=True,
        read_only=True,
    )
    montage = PersonSerializer(
        many=True,
        read_only=True,
    )
    genre = GenreSerializer(
        many=True,
        read_only=True,
    )
    movies_reviews = ReviewSerializerForMovies(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Movie
        fields = (
            'id',
            Movie.name.field.name,
            Movie.description.field.name,
            Movie.genre.field.name,
            Movie.country.field.name,
            Movie.actors.field.name,
            Movie.director.field.name,
            Movie.producer.field.name,
            Movie.screenwriter.field.name,
            Movie.operator.field.name,
            Movie.composer.field.name,
            Movie.artist.field.name,
            Movie.montage.field.name,
            Movie.budget.field.name,
            Movie.created_at.field.name,
            'movies_reviews',
        )

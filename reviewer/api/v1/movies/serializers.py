import rest_framework.serializers

import api.v1.genres.serializers
import api.v1.persons.serializers
import api.v1.reviews.serializers
import movies.models


class MovieSerializer(rest_framework.serializers.ModelSerializer):
    actors = api.v1.persons.serializers.PersonSerializer(
        many=True,
        read_only=True,
    )
    director = api.v1.persons.serializers.PersonSerializer(
        many=True,
        read_only=True,
    )
    producer = api.v1.persons.serializers.PersonSerializer(
        many=True,
        read_only=True,
    )
    screenwriter = api.v1.persons.serializers.PersonSerializer(
        many=True,
        read_only=True,
    )
    operator = api.v1.persons.serializers.PersonSerializer(
        many=True,
        read_only=True,
    )
    composer = api.v1.persons.serializers.PersonSerializer(
        many=True,
        read_only=True,
    )
    artist = api.v1.persons.serializers.PersonSerializer(
        many=True,
        read_only=True,
    )
    montage = api.v1.persons.serializers.PersonSerializer(
        many=True,
        read_only=True,
    )
    genre = api.v1.genres.serializers.GenreSerializer(
        many=True,
        read_only=True,
    )
    movies_reviews = api.v1.reviews.serializers.ReviewSerializerForMovies(
        many=True,
        read_only=True,
    )

    class Meta:
        model = movies.models.Movie
        fields = (
            'id',
            movies.models.Movie.name.field.name,
            movies.models.Movie.description.field.name,
            movies.models.Movie.genre.field.name,
            movies.models.Movie.country.field.name,
            movies.models.Movie.actors.field.name,
            movies.models.Movie.director.field.name,
            movies.models.Movie.producer.field.name,
            movies.models.Movie.screenwriter.field.name,
            movies.models.Movie.operator.field.name,
            movies.models.Movie.composer.field.name,
            movies.models.Movie.artist.field.name,
            movies.models.Movie.montage.field.name,
            movies.models.Movie.budget.field.name,
            movies.models.Movie.created_at.field.name,
            'movies_reviews',
        )

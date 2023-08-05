import rest_framework.serializers

import genres.models


class GenreSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = genres.models.Genre
        fields = (
            'id',
            genres.models.Genre.name.field.name,
        )

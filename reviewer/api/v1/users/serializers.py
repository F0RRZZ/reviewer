import rest_framework.serializers

import api.v1.reviews.serializers
import users.models


class UserSerializer(rest_framework.serializers.ModelSerializer):
    users_reviews = api.v1.reviews.serializers.ReviewSerializerForUsers(
        many=True,
        read_only=True,
    )

    class Meta:
        model = users.models.User
        fields = (
            'id',
            users.models.User.username.field.name,
            users.models.User.email.field.name,
            users.models.User.bio.field.name,
            users.models.User.date_joined.field.name,
            users.models.User.is_staff.field.name,
            'users_reviews',
        )

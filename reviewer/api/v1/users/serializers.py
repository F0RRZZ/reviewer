from rest_framework.serializers import ModelSerializer

from api.v1.reviews.serializers import ReviewSerializerForUsers
from users.models import User


class UserSerializer(ModelSerializer):
    users_reviews = ReviewSerializerForUsers(
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            User.username.field.name,
            User.email.field.name,
            User.bio.field.name,
            User.date_joined.field.name,
            User.is_staff.field.name,
            'users_reviews',
        )

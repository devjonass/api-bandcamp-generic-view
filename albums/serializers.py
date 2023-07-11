from rest_framework import serializers
from .models import Album
from users.models import User


class AlbumSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]

    def get_user_id(self, obj: User):
        return obj.id

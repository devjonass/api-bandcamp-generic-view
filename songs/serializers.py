from rest_framework import serializers
from albums.serializers import AlbumSerializer
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    album_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]

    def get_album_id(self, obj: Song):
        return obj.album.id

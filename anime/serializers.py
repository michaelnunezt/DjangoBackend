from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from anime.models import *


class AnimeSerializer(ModelSerializer):
    class Meta:
        model = Anime
        fields = [
            "id",
            "title",
            "description",
            "genre",
            "release_date",
            "duration",
            "thumbnail",
            "video_url"
        ]


class UserAnimeListSerializer(ModelSerializer):
    class Meta:
        model = UserAnimeList
        fields = "__all__"  # Include all fields in the UserAnimeList model
        read_only_fields = ["user"]  # The user field will be populated automatically

    def to_representation(self, instance):
        output = super().to_representation(instance)
        output["anime"] = AnimeSerializer(instance=instance.anime).data
        return output


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"  # Include all fields in the Review model
        read_only_fields = ["user", "created_at", "updated_at"]  # Auto-populated fields

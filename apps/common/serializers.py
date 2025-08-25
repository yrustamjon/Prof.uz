from rest_framework.serializers import ModelSerializer
from .models import Banner, Button

class ButtonsSerializer(ModelSerializer):
    class Meta:
        model = Button
        fields = (
            "id", "created_at", "updated_at",
            "name", "link",
        )

class BannerSerializer(ModelSerializer):
    buttons = ButtonsSerializer(many=True)
    class Meta:
        model = Banner
        fields = (
            "id", "created_at", "updated_at",
            "title", "description", "image", "background_color",
            "buttons"
        )
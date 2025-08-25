from rest_framework import generics
from .serializers import BannerSerializer
from .models import Banner

class BannerListAPIView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

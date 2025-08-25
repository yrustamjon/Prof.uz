from django.urls import path, include
from .views import BannerListAPIView

urlpatterns = [
    path('user/', include('apps.users.urls')),
    path('professions/', include('apps.professions.urls')),
    path('banners/', BannerListAPIView.as_view(), name='banner-list')
]
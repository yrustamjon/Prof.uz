from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.users.urls')),
    path('professions/', include('apps.professions.urls')),
]
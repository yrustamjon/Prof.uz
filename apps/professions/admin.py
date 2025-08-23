from django.contrib import admin
from .models import (
    Profession,Category,Subject,Comment,
    Training, 
                     )


admin.site.register(Profession)
admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Training)
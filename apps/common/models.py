from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
class Button(BaseModel):
    name=models.CharField(max_length=100)
    link=models.URLField()
    

class Banner(BaseModel):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='banners/')
    background_color = models.CharField(max_length=100)
    buttons = models.ManyToManyField(Button, related_name='banners')

    def __str__(self):
        return self.title


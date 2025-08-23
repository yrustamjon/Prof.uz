from django.db import models
from apps.common.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100)
    

class Subject(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Profession(BaseModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    
    category = models.ForeignKey(
        Category,
        related_name='professions', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )
    
    subjects = models.ManyToManyField(
        Subject, 
        related_name='professions', 
        blank=True
    )
    
    
    at_worked = models.BooleanField(default=False)
    selery_min= models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salery_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    card_image = models.ImageField(upload_to='professions/cards/', blank=True, null=True)
    back_graund_image = models.ImageField(upload_to='professions/backgrounds/', blank=True, null=True)
    video = models.FileField(upload_to='professions/videos/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
class Comment(BaseModel):
    user = models.ForeignKey(
        'users.CustomUser', 
        related_name='comments', 
        on_delete=models.CASCADE
    )
    text = models.TextField()
    training= models.ForeignKey(
        'Training', 
        related_name='comments', 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.text[:20]  

class Training(BaseModel):
    title= models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='trainings/pictures/', blank=True, null=True)
    video = models.FileField(upload_to='trainings/videos/', blank=True, null=True)
    def __str__(self):
        return self.title
    
    



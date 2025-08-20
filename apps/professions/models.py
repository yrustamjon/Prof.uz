from django.db import models
from apps.common.models import BaseModel

class Field(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Profession(BaseModel):
    name = models.CharField(max_length=100)
    at_worked = models.BooleanField(default=False)
    selery_min= models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salery_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    card_image = models.ImageField(upload_to='professions/cards/', blank=True, null=True)
    back_graund_image = models.ImageField(upload_to='professions/backgrounds/', blank=True, null=True)
    field = models.ForeignKey(Field, related_name='professions', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name
    


class Types(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    card_image = models.ImageField(upload_to='categories/cards/', blank=True, null=True)
    #back_graund_image = models.ImageField(upload_to='categories/backgrounds/', blank=True, null=True)
    profession = models.ManyToManyField(Profession, related_name='categories', blank=True)
    def __str__(self):
        return self.name
    



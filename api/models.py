from django.db import models
from django.db.models import CharField,IntegerField,TextField,FloatField,ImageField
# Create your models here.


class Book(models.Model):
    title=CharField(max_length=100,unique=False,null=False,blank=False)
    author=CharField(max_length=30,null=False,blank=False)
    synopsis=TextField(blank=True,null=True)
    isbn=IntegerField(unique=True)
    image=ImageField(blank=True,null=True,upload_to='book_cover')
    price=FloatField()
    
    def __str__(self):
        return self.title
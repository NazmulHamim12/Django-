from django.db import models
from django.utils import timezone
# Create your models here.
class Table(models.Model):
    LANGUAGE_CHOISE=[
        ('PY','PYTHON'),
        ('JS','JAVASCRIPT'),
        ('PHP','PHP'),
        ('CSS','CASCADING STYLE SHEET'),
        ('C++','C++'),
    ]
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to='img/')
    date = models.DateTimeField(default=timezone.now)
    lang_type=models.CharField(max_length=4,choices=LANGUAGE_CHOISE,default='PY')
    des=models.TextField(default='')
    
    
    
    def __str__(self):
        return self.name
    
class About(models.Model):
    HOBBY=[
        ('cpp','Competive programming'),
        ('Book','Reading book'),
        ('Edu','Education')
    ]
    name=models.CharField(max_length=60)
    image=models.ImageField(upload_to='img/')
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=8)
    hobby=models.CharField(max_length=80,choices=HOBBY,default='cpp')
    
    def __str__(self):
        return self.name
    

class Sing_up(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    image= models.ImageField(upload_to='img/',null=True, blank=True)
    passw=models.CharField(max_length=8,null=True, blank=True)

    def __str__(self):
        return self.name
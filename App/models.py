from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

class Contact(models.Model):
    manager=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    info=models.CharField(max_length=200)
    gender=models.CharField(max_length=30,choices=(
        ('male','Male'),
        ('female','Female')
    ))
    image=models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    class Meta:
        ordering=['-id']
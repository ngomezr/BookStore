from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import datetime

class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item

class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Search(models.Model):
    search = models.CharField(max_length=255)
    def str(self):
        return str(self.id)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()

class WishList(models.Model):
    book = models.CharField(max_length=255)
    publishdate = models.DateField(auto_now=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def str(self):
        return str(self.id)

class ShoppingCart(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def str(self):
        return str(self.id)

class ForumPost(models.Model):
    test = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, default="Guest")
    body = models.TextField(max_length=500)
    publishdate = models.DateField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return str(self.username)

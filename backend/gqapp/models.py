from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
class UserProfile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="product_pics/profile_pics")
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_pic = models.ImageField(upload_to='categoris')
class Music(models.Model):
    music_name = models.CharField(max_length=200)
    audio = models.FileField(upload_to="music/")
    music_pic = models.ImageField(upload_to='music/pics/')
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    period = models.TimeField()
    date_diffusion = models.DateField(default=timezone.now)
    views = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=300)
class PlayListe(models.Model):
    music_included=models.ManyToManyField("Music")
    playliste_name=models.CharField(max_length=200)
    created_by = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
class Mix(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE,null=True , blank =True)
    Mixname = models.CharField(max_length=200)
    music_included = models.ManyToManyField("Music")
    date = models.DateField(default=timezone.now)
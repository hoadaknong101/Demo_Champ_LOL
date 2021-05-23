from django.db import models
from django.db.models import fields
from django.db.models.fields.related import OneToOneField


class General(models.Model):
    name = models.CharField(max_length=50)
    avata = models.ImageField(upload_to='Anh_Tuong')

    def __str__(self):
        return self.name


class IntroduceGeneral(models.Model):
    general = OneToOneField(
        General, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='Anh_Tuong')
    role = models.CharField(max_length=50)
    level = models.IntegerField(default=0)
    diffculty = models.CharField(max_length=50)
    introduction = models.TextField(max_length=1000)
    video_intro_id = models.FileField(upload_to='video')

    def __str__(self):
        return self.general.name


class AbilityGeneral(models.Model):
    general = OneToOneField(
        General, on_delete=models.CASCADE, primary_key=True)

    name_passive = models.CharField(max_length=500)
    content_passive = models.CharField(max_length=500)
    image_passive = models.ImageField(upload_to='ability')

    name_q = models.CharField(max_length=100)
    content_q = models.CharField(max_length=500)
    image_q = models.ImageField(upload_to='ability')

    name_w = models.CharField(max_length=100)
    content_w = models.CharField(max_length=500)
    image_w = models.ImageField(upload_to='ability')

    name_e = models.CharField(max_length=100)
    content_e = models.CharField(max_length=500)
    image_e = models.ImageField(upload_to='ability')

    name_r = models.CharField(max_length=100)
    content_r = models.CharField(max_length=500)
    image_r = models.ImageField(upload_to='ability')

    video_ability = models.FileField(upload_to='video', blank=True, null=True)

    def __str__(self):
        return self.general.name


class SkinGeneral(models.Model):
    general = OneToOneField(
        General, on_delete=models.CASCADE, primary_key=True)

    name_1 = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='skin')

    name_2 = models.CharField(max_length=100)
    image_2 = models.ImageField(upload_to='skin')

    name_3 = models.CharField(max_length=100)
    image_3 = models.ImageField(upload_to='skin')

    name_4 = models.CharField(max_length=100)
    image_4 = models.ImageField(upload_to='skin')

    name_5 = models.CharField(max_length=100)
    image_5 = models.ImageField(upload_to='skin')

    def __str__(self):
        return self.general.name


class Cosplay(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cosplay')

    def __str__(self):
        return self.name

# Create your models here.

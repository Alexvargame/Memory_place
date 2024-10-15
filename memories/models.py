import os.path

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render,redirect, reverse



class Country(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name='Страна'
        verbose_name_plural='Страны'
    def __str__(self):
        return self.name



class City(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name='Город'
        verbose_name_plural='Города'
    def __str__(self):
        return self.name

class Memories(models.Model):
    user = models.ForeignKey(User,related_name='memory_creator',on_delete=models.CASCADE)
    place_name=models.CharField(max_length=250)
    place_city=models.CharField(choices=[(c.name,c.name) for c in City.objects.all()],max_length=250,blank=True,null=True)#default='')#models.ManyToManyField(Country,verbose_name='Страна',related_name='country')
    place_country=models.CharField(choices=[(c.name,c.name) for c in Country.objects.all()],max_length=250,blank=True,null=True)#default='')#models.ManyToManyField(City,verbose_name='Город',related_name='city')
    place_coord_lat=models.FloatField(default=0.0)
    place_coord_lon = models.FloatField(default=0.0)
    place_address=models.CharField(max_length=500, blank=True,null=True)
    description=models.TextField()
    date_event=models.DateField()

    class Meta:
        verbose_name='Памятное место'
        verbose_name_plural='Памятные места'

    def __str__(self):
        return self.place_name


    def get_absolute_url(self):
        return reverse('detail_memory_url', kwargs={'pk': self.id})
    def get_delete_url(self):
        return reverse('delete_memory_url', kwargs={'pk': self.id})
    def get_update_url(self):
        return reverse('update_memory_url', kwargs={'pk': self.id})

def get_memory_image_path(instance,filename):
    return os.path.join('memories/pics/'+f'{instance.memory.place_name}',filename)
class ImageMemory(models.Model):
    memory=models.ForeignKey(Memories,related_name='mem_image',on_delete=models.CASCADE)
    image_data=models.ImageField(default='default.jpg',upload_to=get_memory_image_path,blank=True,null=True)
    image_url=models.URLField(blank=True)


    class Meta:
        verbose_name='Фотография'
        verbose_name_plural='Фотографии'

    def get_absolute_url(self):
        return reverse('big_image_url', kwargs={'im_pk': self.id})

    def get_delete_url(self):
        return reverse('image_delete_url', kwargs={'im_pk': self.id})


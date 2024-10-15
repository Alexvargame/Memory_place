from django.contrib import admin
from .models import Country,City,Memories,ImageMemory

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=('name',)
# Register your models here.

@admin.register(Memories)
class MemoriesAdmin(admin.ModelAdmin):
    list_display=('id','user','place_name','place_country','place_city','date_event','description','place_coord_lat','place_coord_lon','place_address')

@admin.register(ImageMemory)
class ImageMemoreyAdmin(admin.ModelAdmin):
    list_display = ('id','memory','image_data','image_url')
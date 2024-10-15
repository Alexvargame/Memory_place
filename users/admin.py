from django.contrib import admin
from .models import Profile,PhoneNumber

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user',)


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display=('phone_number',)


# Register your models here.

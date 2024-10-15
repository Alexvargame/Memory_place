from django.db import models
from django.forms import fields
from django.contrib.auth.models import User


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=17, blank=True)  # , primary_key=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    sirname = models.CharField(max_length=30, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    about_user = models.TextField(max_length=300, blank=True)
    phone_number = models.ManyToManyField(PhoneNumber, verbose_name="Телефоны", related_name="phons")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_phone_number(self):
        return [pn.phone_number for pn in self.phone_number.all()]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

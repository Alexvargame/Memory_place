from django import forms
from django.forms import widgets, fields
from .models import Memories,Country,City

class MemoryCreateForm(forms.ModelForm):

    class Meta:
        model=Memories
        fields={'user','place_name','place_country','place_city','description','date_event'}
        widgets={
            'user': forms.TextInput(attrs={'class': 'form-control', 'empty_value': True}),
            'place_name':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'place_country':forms.Select(choices=sorted([(c.name,c.name) for c in Country.objects.all()]),attrs={'class':'form-control','empty_value':True}),
            'place_city': forms.Select(choices=sorted([(c.name, c.name) for c in City.objects.all()]),attrs = {'class': 'form-control', 'empty_value': True}),
            'discription':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'date_event':forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'})

        }

class MemoryUpdateForm(forms.ModelForm):
    mem_image = forms.ImageField(required=False,label=u'Фотографии', widget=forms.ClearableFileInput(
        attrs={'class': 'form-control',  'empty_value': True}))#,'allow_multiple_selected':True}))
    class Meta:
        model=Memories
        fields={'user','place_name','place_country','place_city','description','date_event'}
        widgets={
            'user': forms.TextInput(attrs={'class': 'form-control', 'empty_value': True}),
            'place_name':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'place_country':forms.Select(choices=sorted([(c.name,c.name) for c in Country.objects.all()]),attrs={'class':'form-control','empty_value':True}),
            'place_city': forms.Select(choices=sorted([(c.name, c.name) for c in City.objects.all()]),attrs = {'class': 'form-control', 'empty_value': True}),
            'discription':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'date_event':forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'})

        }


from django.shortcuts import render,redirect, reverse,get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile

from .models import Memories,ImageMemory
from .forms import MemoryCreateForm, MemoryUpdateForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from map.get_coord import get_route
from map.views import showpoint
import folium
from geopy.geocoders import Nominatim



def list_memories(request):
    l_mems=Memories.objects.filter(user=request.user)
    return render(request,'memories/list_memories.html',{'l_mems':l_mems})

def main_memories(request):

    return render(request,'memories/main_memories.html')

def delete_image(request,pk,im_pk):
    mem=Memories.objects.get(id=pk)
    image=get_object_or_404(ImageMemory,id=im_pk)
    image.delete()
    images = ['/media/' + str(im.image_data) for im in ImageMemory.objects.filter(memory=mem)]
    imgs = [img for img in ImageMemory.objects.filter(memory=mem)]
    return redirect(mem)

class MemoryDetailView(LoginRequiredMixin,View):

    def get(self,request,pk):
        mem=Memories.objects.get(id=pk)
        return render(request,'memories/detail_memory.html',{'mem':mem})


class MemoryCreateView(LoginRequiredMixin,View):

    def get(self,request):
        form=MemoryCreateForm(initial={'user':request.user,'place_country':'','place_city':''})

        return render(request,'memories/create_memories.html',{'form':form})

    def post(self,request):
        bound_form=MemoryCreateForm(request.POST,initial={'user':request.user,'place_country':'','place_city':''})
        #lat1, long1, lat2, long2 = float(lat1), float(long1), float(lat2), float(long2)
        pl_name=bound_form['place_name'].value()#+' '+bound_form['place_city'].value()+' '+bound_form['place_country'].value()
        geolocator = Nominatim(user_agent="coordinates_finder")
        location = geolocator.geocode(pl_name)
        print('pl',pl_name)
        #print(location.point,location.raw)
        print(location.raw['addresstype'])
        print(location.address)
        print((location.latitude, location.longitude))
        route = get_route(location.latitude, location.longitude)#(long1, lat1)
        if bound_form.is_valid():
            new_mem=bound_form.save()
            new_mem.user=request.user
            new_mem.place_coord_lat=route['point'][0]
            new_mem.place_coord_lon=route['point'][1]
            new_mem.place_address=location.address
            new_mem.save()
            #return render(request, 'memories/create_memories.html', {'form': bound_form,'s':route})
            return redirect(new_mem)
        return render(request, 'memories/create_memories.html', {'form': bound_form})

class MemoryUpdateView(LoginRequiredMixin,View):
    def get(self,request,pk):
        mem=Memories.objects.get(id=pk)
        form=MemoryUpdateForm(instance=mem)#,initial={'user':request.user})
        images = ['/media/' + str(im.image_data) for im in ImageMemory.objects.filter(memory=mem) if im]
        imgs=[img for img in ImageMemory.objects.filter(memory=mem) if img]
        return render(request,'memories/update_memories.html',{'form':form,'images':images,'imgs':imgs})
    def post(self,request,pk):
        mem = Memories.objects.get(id=pk)
        bound_form=MemoryUpdateForm(request.POST,request.FILES,instance=mem)#,initial={'user':request.user})
        if bound_form.is_valid():
            new_mem=bound_form.save()
            new_mem.user = request.user
            new_mem.save()
            for f in request.FILES.getlist('mem_image'):
                data = f.read()
                image = ImageMemory(memory=new_mem)
                image.image_data.save(f.name, ContentFile(data))
                image.save()

            return redirect(new_mem)
        return render(request, 'memories/update_memories.html', {'form': bound_form,'s':request.FILES.getlist('mem_image')})



class MemoryDetailView(LoginRequiredMixin,View):

    def get(self,request,pk):
        mem=Memories.objects.get(id=pk)
        img_dict={}
        images = [im for im in ImageMemory.objects.filter(memory=mem)]
        for im in images:
            img_dict[im]='/media/' + str(im.image_data)
        return render(request,'memories/detail_memory.html',{'mem':mem,'img_dict':img_dict})


class MemoryDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        mem=Memories.objects.get(id=pk)
        return render(request,'memories/delete_memories.html',{'mem':mem})
    def post(self,request,pk):
        mem=Memories.objects.get(id=pk)
        mem.delete()
        return redirect(reverse('list_memories_url'))

class BigImageView(LoginRequiredMixin,View):
    def get(self,request,im_pk):
        #img=ImageMemory.objects.get(id=im_pk)
        #img_url='/media/' + str(img.image_data)
        images=ImageMemory.objects.filter(memory=ImageMemory.objects.get(id=im_pk).memory)
        img_dict={}
        for im in images:
            img_dict[im]='/media/' + str(im.image_data)
        #paginator = Paginator(images, 1)
        #page = request.GET.get('page')
        #try:
        #    images = paginator.page(page)
       # except PageNotAnInteger:
       #     images = paginator.page(1)
      #  except EmptyPage:
        #    images = paginator.page(paginator.num_pages)

        paginator = Paginator(images, 1)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url ='?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url ='?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        context={
            'img_dict': img_dict,
            #'images': images,
            'images': page,
            'memory':ImageMemory.objects.get(id=im_pk).memory,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
        }
        return render(request,'memories/big_image.html',context=context)


##

from django.urls import path

from .views import *


urlpatterns = [
    path('',main_memories,name='main_memories_url'),
    path('memories/',list_memories,name='list_memories_url'),
    path('memories/create/',MemoryCreateView.as_view(),name='create_memory_url'),
    path('memories/<int:pk>/',MemoryDetailView.as_view(),name='detail_memory_url'),
    path('memories/images/<int:im_pk>',BigImageView.as_view(),name='big_image_url'),
    path('memories/<int:pk>/update/',MemoryUpdateView.as_view(),name='update_memory_url'),
    path('memories/<int:pk>/update/<int:im_pk>/',delete_image,name='delete_image_url'),
    path('memories/<int:pk>/delete/',MemoryDeleteView.as_view(),name='delete_memory_url'),
]


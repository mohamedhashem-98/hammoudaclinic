from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('' , views.index , name='index'),
  path('login/' , views.reserve , name='reserve'),
  path('ar/' , views.ar , name='ar'),
  path('loginar/' , views.reservear , name='reservear'),
  path('gallery/' , views.gallery , name='gallery'),
  path('ar/gallery' , views.galleryar , name='galleryar'),
  path('ar/services/<int:id>' , views.servicesar , name='servicesar'),
  path('services/<int:id>' , views.services , name='services'),
  path('ar/posts/<int:id>' , views.postsar , name='postsar'),
  path('posts/<int:id>' , views.posts , name='posts'),
  path('posts/' , views.postsN , name='postsN'),
  path('ar/posts/' , views.postsNar , name='postsNar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

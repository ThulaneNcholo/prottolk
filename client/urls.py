
from django.urls import path
from .import views

app_name = "client"

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('about', views.AboutView, name='about'),
    path('services', views.ServicesView, name='services'),
    path('service-details/<int:id>',
         views.ServiceDetailsView, name='service-details'),
    path('gallery', views.GalleryView, name='gallery'),
    path('contact', views.ContactView, name='contact'),
]

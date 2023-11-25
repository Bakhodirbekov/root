from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('work', views.work, name= 'work'),
    path('works', views.works, name= 'works'),
    path('contact', views.contact, name= 'contact')

]
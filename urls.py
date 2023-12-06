
from django.urls import path
#path("", views.index, name="index"),,
# path("",index_sujet, name="index_sujet"), 
from . import views
from .views import*
urlpatterns = [

    path("", AcceuilP, name="AcceuilP"),
    path("index", views.index, name="index"),
    path("Concours d'admission",index_sujet_sel, name="Concours d'admission"),
    path("selection",index_sujet_sel, name="index_sujet_sel"),
   
     path("information/",index_information, name="index_information"),
    ]
    

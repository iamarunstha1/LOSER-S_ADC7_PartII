
from django.urls import path

from .views import index5
from .views import aboutus
from nepal.views import search
from nepal.views import searchresults

urlpatterns = [
    path("index5/", index5, name="index"),
    #path("aboutus/", aboutus, name="aboutus")
    path('search/',search),
    path('searchlist/',searchresults),
    ]

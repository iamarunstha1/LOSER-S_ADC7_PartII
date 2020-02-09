from django.contrib import admin
from django.urls import path
from faceofnepal.views import index
from faceofnepal.views import freelancer_list
from faceofnepal.views import freelancer_form
from faceofnepal.views import freelancer_update_save
from faceofnepal.views import freelancer_save
from faceofnepal.views import freelancer_edit
from faceofnepal.views import freelancer_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('freelancerform/',freelancer_form,name="freelancer_add"),
    path('freelancerform/save/',freelancer_save),
    path('freelancerlist/',freelancer_list), 
    path('freelancer/edit/<int:ID>',freelancer_edit, name="freelancer_edit"),
    path('freelancer/edit/save/<int:ID>',freelancer_update_save),
    path('freelancer/delete/<int:ID>',freelancer_delete, name='freelancer_delete'),
    
]
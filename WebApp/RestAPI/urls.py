from django.urls import path
from .views import view_get_post_freelancer
from .views import view_getByID_updateByID_deleteByID


urlpatterns = [
    path('freelancers/',view_get_post_freelancer),
    path('freelancers/<int:ID>',view_getByID_updateByID_deleteByID),
]
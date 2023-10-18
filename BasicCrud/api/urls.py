
from django.urls import path
from . import views


urlpatterns = [
    path('drf-crud/' , views.Crudapi_view.as_view() , name= 'crud'),
]
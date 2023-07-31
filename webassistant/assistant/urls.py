from django.urls import path
from . import views

# a list of all the urls
urlpatterns = [
    path('', views.home, name='home'),
    path('new_chat/', views.new_chat, name='new_chat'),
    path('error_handler/', views.error_handler, name='error_handler')
]

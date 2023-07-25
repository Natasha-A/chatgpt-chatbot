from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Url to the admin site
    path('admin/', admin.site.urls),
    
    # registering all the assistant application urls 
    path('', include('assistant.urls'))
]

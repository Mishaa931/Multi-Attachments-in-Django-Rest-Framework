
from django.contrib import admin
from django.urls import path,include
from multiattachment1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('multiattachment1.urls')),
    path("api/file/", include('file.urls')),

    
]

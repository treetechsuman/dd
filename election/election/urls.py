
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('address/', include('address.urls')),
    path('api/', include('myapi.urls')),
    path('admin/', admin.site.urls),
]

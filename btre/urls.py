from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]

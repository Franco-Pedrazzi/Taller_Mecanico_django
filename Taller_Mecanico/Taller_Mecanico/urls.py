from django.urls import path 
from django.contrib import admin
import myapp.views as views
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path("", views.index, name="index") ,
] 

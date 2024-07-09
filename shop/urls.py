
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from shop import views
from django.contrib import admin
from django.urls import path, include
from shop import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path('info/', views.info,name='info'),
    path('gallery/', views.gallery,name='gallery'),
    path('form/', views.form, name='form'),
    path('login/', views.login),
    path('registration/', views.registration),

]

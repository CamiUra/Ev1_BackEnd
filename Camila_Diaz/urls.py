"""
URL configuration for Camila_Diaz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.viewHome),
    path('home', views.viewHome),
    path('page1', views.viewPage1),
    path('page2', views.viewPage2),
    path('page3', views.viewPage3),
    path('page4', views.viewPage4),
    path('page5', views.viewPage5),
    path('page6', views.viewPage6),
]

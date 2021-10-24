"""Django_Template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from django.urls.conf import include, include
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("user/", views.user, name="people"),
    path("table/", views.table, name="table"),
    path("typography/", views.typo, name="typo"),
    path("icon/", views.icon, name="icon"),
    path("maps/", views.maps, name="map"),
    path("notifications/", views.notif, name="notif"),

    # Super Admin
    path('admin/', admin.site.urls),
]

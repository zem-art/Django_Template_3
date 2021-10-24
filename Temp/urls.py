from django.urls import re_path, path
from . import views

app_name = "dashboard"

urlpatterns = [
    re_path(r'^$', views.index, name="")
]

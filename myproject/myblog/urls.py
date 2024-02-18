
from myblog import views
from django.urls import path

urlpatterns = [
    path('', views.archive, name='archive'),
]

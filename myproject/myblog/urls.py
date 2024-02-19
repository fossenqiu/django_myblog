
from myblog import views
from django.urls import path

urlpatterns = [
    path('', views.archive, name='archive'),
    path('create/', views.create_myblog_post, name='create_myblog_post')
]

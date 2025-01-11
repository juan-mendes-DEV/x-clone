from django.urls import path

from x_blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]
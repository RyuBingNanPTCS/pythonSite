from django.urls import path, include
from . import views

#ルート
urlpatterns = [
    path("", views.index),
    path("login", views.login),
    path("logout", views.logout),
    path("reg", views.reg),
    path("index", views.index),
    path("manage",views.manage),
    path('delete', views.delete),
    path('modify', views.modify),
    # path("success", views.success),
]
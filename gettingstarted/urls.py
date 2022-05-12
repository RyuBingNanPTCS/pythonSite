from django.urls import path, include

from django.contrib import admin

from rest_framework import routers
from login.views import UserInfoViewSet

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/
defaulutRouter = routers.DefaultRouter()
defaulutRouter.register('userInfo', UserInfoViewSet)

urlpatterns = [
    path("hello", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("login/", include("login.urls")),
    path("user/", include(defaulutRouter.urls))
]

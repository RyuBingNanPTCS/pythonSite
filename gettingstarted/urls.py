from django.urls import path, include

from django.contrib import admin

from blog.urls import router as blog_router
from django.views.generic import TemplateView 

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("hello", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("login/", include("login.urls")),
    # blog.urlsをincludeする
    path("api/", include(blog_router.urls)),
    path("login2/", include(blog_router.urls)),
]

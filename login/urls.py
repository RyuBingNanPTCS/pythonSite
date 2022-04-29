from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('changepwd', views.change_pwd),
    path('productadd', views.product_add),
    path('productlist', views.product_list),
    # path("success", views.success),
]

print('settings.MEDIA_URL:',settings.MEDIA_URL)
print('settings.MEDAI_ROOT:',settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

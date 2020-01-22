from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home),
    path('upload_item', views.upload_item),
    path('upload', views.upload),
    path('delete/<int:pk>', views.delete),
    path('update_form/<int:pk>', views.update_form),
    path('update_form/update/<int:pk>', views.update),
    path('search/',views.search)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('items/',views.get_post_product),
    path('items/<int:Id>', views.get_update_delete),
    ]
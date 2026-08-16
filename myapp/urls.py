from django.urls import path
from .views import *

urlpatterns = [
    path("register/", register, name='register'),
    path("login/",login,name='login'),
    path("add-product/", add_product, name="add_product"),
    path("my-products/", my_products, name="my_products"),
    path(
    "delete-product/<int:id>/",delete_product,name="delete_product"),
    path("logout/", logout, name="logout"),
]
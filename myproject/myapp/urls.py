
from django.urls import path
from .views import Product_dict , Variant_dict , home

urlpatterns = [

    path('' , home ,name="myapp_home"),
    path('product/',Product_dict , name='Product_dict'),
    path('variant/',Variant_dict , name='Variant_dict'),
]
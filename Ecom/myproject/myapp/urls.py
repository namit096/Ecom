
# from django.urls import path
# from django.urls import path, include
# from .views import Product_dict , Variant_dict , home , list_collections , list_products_by_collection,list_variants_by_collection , list_variants_by_categories

# urlpatterns = [

#     path('' , home ,name="myapp_home"),
#     path('product/',Product_dict , name='Product_dict'),
#     path('variant/',Variant_dict , name='Variant_dict'),
#     path('list_collections/',list_collections , name='list_collections'),
#     path('collections/<int:collection_id>/products/', list_products_by_collection, name='list_products_by_collection'),
#     path('collections/<int:collection_id>/variants/', list_variants_by_collection, name='list_variants_by_collection'),
#     path('categories/<int:category_id>/variants/', list_variants_by_categories, name='list_variants_by_categories'),
# ]

# urlpatterns+= path('__debug__/', include("debug_toolbar.urls")),

from django.urls import path
from . import views

urlpatterns = [
    path('api/collections/', views.list_collections, name='list_collections'),
    path('api/collections/<int:pk>/', views.collection_detail, name='collection_detail'),
    path('api/collections/<int:collection_id>/products/', views.list_products_by_collection, name='list_products_by_collection'),
    path('api/collections/<int:collection_id>/variants/', views.list_variants_by_collection, name='list_variants_by_collection'),
    path('api/categories/<int:category_id>/variants/', views.list_variants_by_categories, name='list_variants_by_categories'),
    path('api/users/', views.list_users, name='list_users'),
    path('api/send-email-to-all-users/', views.send_email_to_all_users, name='send_email_to_all_users'),
    path('api/create-product/', views.create_product, name='create_product'),
]




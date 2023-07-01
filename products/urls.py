from django.urls import path
from .views import new_product, detail_product, product_update

urlpatterns = [
    path('new_product/', new_product, name='new'),
    path('product/<int:product_id>/', detail_product, name='product'),
    path('product/<int:product_id>/update/', product_update, name='update'),
]

from django.urls import path
from .views import new_product, detail_product, product_update, product_delete, new_comment, delete_comment

urlpatterns = [
    path('new_product/', new_product, name='new'),
    path('product/<int:product_id>/', detail_product, name='product'),
    path('product/<int:product_id>/update/', product_update, name='update'),
    path('product/<int:product_id>/delete/', product_delete, name='delete'),
    path('product/<int:product_id>/coment/new/', new_comment, name='coment'),
    path("<int:product_id>/comment/<int:comment_id>/delete", delete_comment, name='comment_delete'),
]

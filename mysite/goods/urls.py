from django.urls import path
from .views import all_goods, goods_new, goods_edit, goods_detail, goods_delete

urlpatterns = [
    path('', all_goods, name='all_goods'),
    path('<int:pk>/', goods_detail, name='goods_detail'),
    path('new/', goods_new, name='goods_new'),
    path('<int:pk>/edit/', goods_edit, name='goods_edit'),
    path('<int:pk>/delete/', goods_delete, name='goods_delete'),
]

from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.main, name='main'), #главная
    path('product_list', views.product_list, name='product_list'), #все товары
    path('category/<slug:category_slug>', views.product_list, name='product_list_by_category'), #отображаем по категориям
    path('franchise/<slug:franchise_slug>', views.product_list, name='product_list_by_franchise'), #отображаем по франшизам
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail') #отображаем по отдельности
]
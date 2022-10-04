from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('<int:id>/add', views.add, name='add'),
    path('', views.cartView, name='cartView'),
    path('<int:id>/remove', views.cartRemove, name='cartRemove'),
    path('<int:id>/remove_one', views.cartRemoveOne, name='cartRemoveOne'),
]

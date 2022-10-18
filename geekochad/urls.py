from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('accounts.urls')),
    path('', include('shop.urls', namespace='shop')), # По основному адресу будет открывать главную страницу из приложения shop
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import redirect, render, get_object_or_404
from .cart import Cart
from shop.models import Product, Category

def add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product)
    return redirect(request.META.get('HTTP_REFERER')) #Редиректит на страницу с которой был отправлен запрос

def cartView(request):
    cart = Cart(request)
    categories = Category.objects.all()
    return render(request, 'cart/cart.html', {'cart':cart,
                                              'categories': categories,})

def cartRemove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart:cartView')

def cartRemoveOne(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove_one(product)
    return redirect(request.META.get('HTTP_REFERER')) #Редиректит на страницу с которой был отправлен запрос

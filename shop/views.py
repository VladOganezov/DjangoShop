from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Franchise
from cart.cart import Cart


def args(req):
    cart = Cart(req)
    categories = Category.objects.all()
    franchises = Franchise.objects.all()
    return render(req,
                    {   
                        'cart': cart,
                        'categories': categories,
                        'franchises': franchises
                    })


def main(request, category_slug=None):
    cart = Cart(request)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main.html',
                    {
                        'category': category,
                        'categories': categories,
                        'products': products,
                        'cart': cart
                    })


def product_list(request, category_slug=None, franchise_slug=None):
    franchise = None
    category = None
    cart = Cart(request)
    categories = Category.objects.all()
    franchises = Franchise.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if franchise_slug:
        franchise = get_object_or_404(Franchise, slug=franchise_slug)
        products = products.filter(franchise=franchise)
    return render(request, 'shop/product_list.html', 
                    {   
                        'categories': categories,
                        'franchises': franchises,
                        'category': category,
                        'franchise': franchise,
                        'products': products,
                        'cart': cart
                    })


def product_detail(request, id, slug):
    cart = Cart(request)
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product_detail.html',
                    {   
                        'product': product,
                        'categories': categories,
                        'cart': cart
                    })
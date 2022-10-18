from django.shortcuts import render
from .models import OrderItem
from shop.models import Category
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order



@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/admin/orders/order/detail.html', {'order': order})


def order_create(request):
    categories = Category.objects.all()
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            del request.session['cart']
            # launch asynchronous task
            order_created.send(order.id)

            return render(request, 'orders/order_created.html',
                          {'order': order, 'categories': categories,})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_create.html',
                  {'cart': cart, 'form': form, 'categories': categories,})
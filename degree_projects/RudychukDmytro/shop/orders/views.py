from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    cart = Cart(request)
    user = request.user  # Отримуємо поточного користувача
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if user.is_authenticated:
                order.user = user
                order.first_name = user.first_name
                order.last_name = user.last_name
                order.email = user.email
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])
            # Очистка кошика
            cart.clear()
            return render(request, 'created_order.html', {'order': order})
    else:
        if user.is_authenticated:
            initial_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            }
            form = OrderCreateForm(initial=initial_data)
        else:
            form = OrderCreateForm()
    return render(request, 'create_order.html', {'cart': cart, 'form': form})


def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'order_history.html', {'orders': orders})


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_detail.html', {'order': order})

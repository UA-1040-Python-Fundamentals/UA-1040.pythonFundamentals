from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
        category = None
        categories = Category.objects.all()
    else:
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        else:
            category = None
            categories = Category.objects.all()
    return render(request, 'shop/product/list.html',
                      {
                          'category': category,
                          'categories': categories,
                          'products': products,
                      })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def action(request):
    return render(request, 'shop/product/action.html')


def contacts(request):
    return render(request, 'shop/product/contacts.html')


def about(request):
    return render(request, 'shop/product/about.html')





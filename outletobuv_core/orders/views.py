from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseBadRequest
from products.models import Product

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})  # Получаем корзину из сессии
        product_ids = cart.keys()
        products = Product.objects.filter(pk__in=product_ids)
        total_price = sum(product.price * cart[str(product.pk)]['quantity'] for product in products)
        return render(request, 'orders/cart.html', {'products': products, 'total_price': total_price})

class AddToCartView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        if not product_id:
            return HttpResponseBadRequest('Product ID is required.')

        if quantity <= 0:
            return HttpResponseBadRequest('Quantity must be a positive integer.')

        # Получаем корзину из сессии
        cart = request.session.get('cart', {})
        
        # Проверяем, есть ли уже этот товар в корзине
        if product_id in cart:
            # Если товар уже есть в корзине, увеличиваем количество
            cart[product_id]['quantity'] += quantity
        else:
            # Если товара нет в корзине, добавляем его
            try:
                product = Product.objects.get(pk=product_id)
                cart[product_id] = {'quantity': quantity, 'name': product.name, 'price': product.price}
            except Product.DoesNotExist:
                return HttpResponseBadRequest('Product with this ID does not exist.')

        # Обновляем корзину в сессии
        request.session['cart'] = cart
        return redirect('cart')

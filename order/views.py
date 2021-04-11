from django.shortcuts import render
from .models import OrderList

def order_service(request, category_slug=None):
    category = None
    orders = OrderList.objects.filter()
    return render(request, 'order/order.html', {'orders': orders})

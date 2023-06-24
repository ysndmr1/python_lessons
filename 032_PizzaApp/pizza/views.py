from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .forms import (
    Order, OrderForm
)
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render


def home(request):
    from .models import Pizza
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'home.html', context)


# ------------------------------------
# Class Based Views
# ------------------------------------


class FixView:
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_list')


# ------------------------------
# Views
# ------------------------------

# List:
class OrderListView(FixView, ListView):
    template_name = 'pizza/order_list.html'
    context_object_name = 'orders'
    order = ['-id']


# Create:
class OrderCreateView(FixView, CreateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'


# Detail:
class OrderDetailView(FixView, DetailView):
    template_name = 'pizza/order_detail.html'
    context_object_name = 'order'


# Update:
class OrderUpdateView(FixView, UpdateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'


# Delete:
class OrderDeleteView(FixView, DeleteView):
    pass

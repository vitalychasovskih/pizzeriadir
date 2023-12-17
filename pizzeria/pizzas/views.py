from django.shortcuts import render
from .models import Pizza
# Create your views here.


def index(request):
    """Home page for pizzas app"""
    return render(request, 'pizzas/index.html')


def pizzas_list(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.order_by("name")
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas_list.html', context)


def pizza_page(request, pizzas_id):
    """Show a single pizza and all its toppings"""
    pizza = Pizza.objects.get(id=pizzas_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza_page.html', context)

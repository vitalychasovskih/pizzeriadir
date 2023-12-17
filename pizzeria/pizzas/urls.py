"""Defines patterns for pizzas"""

from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all pizzas.
    path('pizzas/', views.pizzas_list, name='pizzas_list'),
    # Detail page for a single pizza with all followed toppings.
    path('pizzas_list/<int:pizzas_id>/', views.pizza_page, name='pizza_page'),
]

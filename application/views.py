from django.shortcuts import render
from .models import Service, Order, Vehicle
from django.contrib.auth.decorators import permission_required


# Create your views here.

def index(request):
    return render(request, 'index.html')


@permission_required('application.view_service')
def show_services(request):
    services = Service.objects.values()
    return render(request, 'show_services.html', context={'services': services})


def show_orders(request):
    orders = Order.objects.filter(vehicle__model__brand__startswith='Brand').all()
    return render(request, 'show_orders.html', context={'orders': orders})


def show_user_vehicles(request):
    user_vehicles = Vehicle.objects.filter(client=request.user.id).all()
    return render(request, 'show_user_vehicles.html', context={'user_vehicles': user_vehicles})

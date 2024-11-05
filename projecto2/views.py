
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from apps.user.models import User  # Modelo User de la app user
from apps.product.models import Productos  # Modelo Productos de la app product
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html', {})

def main(request):
    return render(request, 'main.html', {})

def ventas(request):
    return render(request, 'ventas.html', {})

def menu_view(request):
    # Obtener todos los usuarios y productos
    users = User.objects.all()
    products = Productos.objects.all()

    # Pasamos los datos a la plantilla
    return render(request, 'main.html', {'users': users, 'products': products})

def ventas_view(request):
    #Obtener todos los productos
    products = Productos.objects.all()

    # Pasamos los datos a la plantilla
    return render(request, 'ventas.html', {'products': products})

def process_sale(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            return JsonResponse({'message': "Cantidad no válida"}, status=400)

        try:
            # Buscar el producto por ID
            product = Productos.objects.get(id=product_id)
            # Verificar que haya suficiente stock
            if product.stock >= quantity:
                product.stock -= quantity
                product.save()
                return JsonResponse({'message': "Venta procesada exitosamente"}, status=200)
            else:
                return JsonResponse({'message': "Stock insuficiente"}, status=400)
        except Productos.DoesNotExist:
            return JsonResponse({'message': "Producto no encontrado"}, status=404)

    return JsonResponse({'message': "Método no permitido"}, status=405)
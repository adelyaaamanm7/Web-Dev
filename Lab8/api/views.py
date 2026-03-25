from django.http import JsonResponse
from .models import Product, Category


def products_list(request):
    products = Product.objects.all()
    data = []

    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id
        })

    return JsonResponse(data, safe=False)


def product_detail(request, id):
    try:
        p = Product.objects.get(id=id)
        return JsonResponse({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)


def categories_list(request):
    categories = Category.objects.all()
    data = [{'id': c.id, 'name': c.name} for c in categories]
    return JsonResponse(data, safe=False)


def category_detail(request, id):
    try:
        c = Category.objects.get(id=id)
        return JsonResponse({'id': c.id, 'name': c.name})
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)


def category_products(request, id):
    try:
        category = Category.objects.get(id=id)
        products = category.products.all()

        data = []
        for p in products:
            data.append({
                'id': p.id,
                'name': p.name,
                'price': p.price,
                'description': p.description,
                'count': p.count,
                'is_active': p.is_active
            })

        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

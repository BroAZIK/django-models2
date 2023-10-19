from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Product



class ProductView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.all()

        results = []
        for product in products:
            results.append({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
            })

        return JsonResponse(results, safe=False)

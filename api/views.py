from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Product



class ProductView(View):
    def get(self, request: HttpRequest, pk=None) -> JsonResponse:
        if pk is None:
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
        else:
            product = Product.objects.get(id=pk)
            
            results = {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
            }
            return JsonResponse(results)

    def post(self, request: HttpRequest) -> JsonResponse:
        pass

    def put(self, request: HttpRequest) -> JsonResponse:
        pass

    def delete(self, request: HttpRequest) -> JsonResponse:
        pass

    

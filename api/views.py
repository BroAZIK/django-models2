from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Product
import json



class ProductView(View):
    def get(self, request: HttpRequest, pk=None) -> JsonResponse:
        """Get all products or product

        Args:
            request (HttpRequest): HttpRequest object.
            pk (_type_, optional): pk for getting product as id. Defaults to None.

        Returns:
            JsonResponse: JsonResponse
        """
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
        """Add new product

        Args:
            request (HttpRequest): HttpRequest object.

        Returns:
            JsonResponse: HttpResponse object.
        """
        body = request.body.decode()
        data = json.loads(body)

        Product.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price')
        )
        return JsonResponse({'message': 'object created.'}, status=201)

    def put(self, request: HttpRequest) -> JsonResponse:
        pass

    def delete(self, request: HttpRequest) -> JsonResponse:
        pass

    

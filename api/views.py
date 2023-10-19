from django.views import View
from django.http import HttpRequest, JsonResponse



class ProductView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass

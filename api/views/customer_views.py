from django.views import View
from django.http import HttpRequest, JsonResponse
from api.models import Customer
import json



class CustomerView(View):
    def get(self, request: HttpRequest, pk=None) -> JsonResponse:
        """Get all customers or customer

        Args:
            request (HttpRequest): HttpRequest object.
            pk (_type_, optional): pk for getting customer as id. Defaults to None.

        Returns:
            JsonResponse: JsonResponse
        """
        pass

    def post(self, request: HttpRequest) -> JsonResponse:
        """Add new customer

        Args:
            request (HttpRequest): HttpRequest object.

        Returns:
            JsonResponse: HttpResponse object.
        """
        pass

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        """Update old customer attributes

        Args:
            request (HttpRequest): HttpRequest object
            pk (int): pk of old customer id

        Returns:
            JsonResponse: JsonResponse object
        """
        pass

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        """Delete customer

        Args:
            request (HttpRequest): HttpRequest object
            pk (int): pk of old customer id

        Returns:
            JsonResponse: JsonResponse object
        """
        pass

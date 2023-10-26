from django.urls import path
from .views.product_views import ProductView
from .views.customer_views import CustomerView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>/', ProductView.as_view()),
    path('customers/', CustomerView.as_view()),
    path('customers/<int:pk>/', CustomerView.as_view())
]

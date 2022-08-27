from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path("accounts/", include("allauth.urls")),
    #    path("inventory/", include("inventory.urls")),
    #    path("orders/", include("orders.urls")),
    #    path("sales/", include("sales.urls")),
    path("authentication/", include("authentication.urls", namespace="authentication")),
]

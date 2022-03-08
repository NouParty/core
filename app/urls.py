from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/client/", include("app.client.urls")),
    path("api/seller/", include("app.seller.urls")),
    path("api/ticket/", include("app.ticket.urls")),
]

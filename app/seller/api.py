from rest_framework import viewsets

from .models import SellerModel
from .serializer import SellerSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = SellerModel.objects.all()
    serializer_class = SellerSerializer

from rest_framework import viewsets

from stores.models import Store
from stores.serializers import StoreSerializer


class SearchView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

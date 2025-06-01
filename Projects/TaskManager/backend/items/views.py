# Alex Miller
# deal with API 

from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from .models import Item
from .serializers import ItemSerializer

# gives the POST, GET, etc API requests

'''
GET /api/items          list all items
POST /api/items         create an item
GET /api/items/1        get an item
PUT /api/items/1        update an item
DELETE /api/items/1     delete an item

'''
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


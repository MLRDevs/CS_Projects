# Alex Miller
# convert the python model to JSON

from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' # all fields in model for JSON


from rest_framework.serializers import ModelSerializer

from .models import Commodity

class CommoditySerialzer(ModelSerializer):
    class Meta:
        model=Commodity
        fields='__all__'
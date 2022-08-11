from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name",
                  "product_title",
                  "product_price"]
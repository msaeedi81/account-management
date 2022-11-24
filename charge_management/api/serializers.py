from rest_framework.serializers import ModelSerializer
from charge_management.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        field = '__all__'

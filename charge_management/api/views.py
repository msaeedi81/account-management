from rest_framework.decorators import api_view
from rest_framework.response import Response
from charge_management.models import Customer
from .serializers import CustomerSerializer
from rest_framework import status
from django.db.models import F
from django.db import transaction
import decimal


@api_view(['POST'])
def add_date(request):
    with transaction.atomic():
        time = request.data.get('timestamp')
        Customer.date(time)
        return Response(status=status.HTTP_200_OK)
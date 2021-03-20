from rest_framework.generics import ListCreateAPIView

from .models import Reseller
from .serializers import ResellerSerializer


class ResellerView(ListCreateAPIView):
    queryset = Reseller.objects.all()
    serializer_class = ResellerSerializer

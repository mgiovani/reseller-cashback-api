from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Reseller
from .serializers import ResellerSerializer, ResellerLoginSerializer


class ResellerView(ListCreateAPIView):
    queryset = Reseller.objects.all()
    serializer_class = ResellerSerializer


class ResellerLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = ResellerLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'status': 'OK'})

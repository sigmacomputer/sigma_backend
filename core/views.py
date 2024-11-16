from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Site
from .serializers import SiteSerializer


class SiteDataAPIView(APIView):
    def get(self, request):
        site = Site.objects.first()
        serializer = SiteSerializer(site)
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from .models import ContactUsForm
from .serializers import ContactUsFormSerializer


class ContactViewSet(GenericViewSet, CreateModelMixin):
    queryset = ContactUsForm.objects.all()
    serializer_class = ContactUsFormSerializer
    
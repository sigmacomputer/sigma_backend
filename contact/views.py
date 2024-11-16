from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from .models import ContactUsForm
from .serializers import ContactUsFormSerializer
from .utils import send_email


class ContactViewSet(GenericViewSet, CreateModelMixin):
    queryset = ContactUsForm.objects.all()
    serializer_class = ContactUsFormSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        email = data.get("email")
        name = data.get("name")
        message = data.get("message")
        phone = data.get("phone")
        subject = f"New message from {name}"
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}"
        send_email(
            subject=subject,
            message=message,
            recipient_list=["henishpatel9045@gmail.com"]
        )
        print("Email sent")
        return super().create(request, *args, **kwargs)
    
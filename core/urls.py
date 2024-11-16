from django.urls import path

from .views import SiteDataAPIView

urlpatterns = [
    path("data/", SiteDataAPIView.as_view(), name="site-data"),
]

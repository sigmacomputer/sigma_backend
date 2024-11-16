from django.contrib import admin

from .models import Site, Gallery, Team, Client, Course

# Register your models here.
admin.site.register([Site, Gallery, Team, Client, Course])

from django.contrib import admin

from .models import Site, Gallery, Team, Client, Course

# Register your models here.
admin.site.site_title = "Sigma Computer Admin"
admin.site.site_header = "Sigma Computer Admin"
admin.site.register([Site, Gallery, Team, Client, Course])

from django.contrib import admin

from .models import Site, Gallery, Team, Client, Course

# Register your models here.
admin.site.site_title = "Sigma Computer Admin"
admin.site.site_header = "Sigma Computer Admin"
admin.site.register([Site,])


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "index_order")
    list_editable = ("index_order",)
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "index_order")
    list_editable = ("index_order",)
    list_display_links = ("title",)
    search_fields = ("title",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "index_order")
    list_editable = ("index_order",)
    list_display_links = ("title",)
    search_fields = ("title",)
    
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "index_order")
    list_editable = ("index_order",)
    list_display_links = ("name",)
    search_fields = ("name",)
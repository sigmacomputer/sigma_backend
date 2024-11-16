from django.contrib import admin

from .models import ContactUsForm
# Register your models here.

@admin.register(ContactUsForm)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "message", "replied", "created_at"]
    search_fields = ["name", "email", "phone",]
    list_filter = ["replied",]
    date_hierarchy = "created_at"
    
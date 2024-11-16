from django.db import models

# Create your models here.
class ContactUsForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    replied = models.BooleanField(default=False, help_text="Check this box if you have replied to this message.")
    message_note = models.TextField(blank=True, null=True, help_text="Any notes about the message.")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
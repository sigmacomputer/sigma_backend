from django.core.mail import send_mail

def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'your_email@gmail.com',  # Sender's email
        recipient_list,
        fail_silently=False,
    )
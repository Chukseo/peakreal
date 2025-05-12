from django.core.mail import send_mail
from django.conf import settings

def send_Email(email):
    subject = "Welcome On-Board!"
    body = '''
        Dear User,
        Thank you for setting up an account
        with us.
        
        This is a welcome message from the Dev Team.
    
    '''
    
    send_mail(
    subject,
    body,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)

    

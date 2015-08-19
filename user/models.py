from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.mail import send_mail

from todo.settings import DEFAULT_FROM_EMAIL

class User(AbstractBaseUser):
    """User extension table."""
    uuid = models.CharField(max_length=42, blank=True, null=True)
    uuid_expiration = models.DateTimeField(blank=True, null=True)
    mail_registration = models.BooleanField(
            default=False,
            db_index=True,
            verbose_name="Receive registration's emails",
            help_text=(
                "To receive a mail at each new registration."
                "(for staff members only)"
            )
    )
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'


    def send_mail(self, subject, message):
        """Send a mail to user."""
        return send_mail(
                subject,
                message,
                DEFAULT_FROM_EMAIL,
                [self.email],
        )


    def save(self, **kwargs):
        """Suscribe to mail if
        it's a creation and user is staff, then save."""

        if not self.pk and self.is_staff:
            self.mail_registration = True

        super(User, self).save()
    
    
    def __str__(self):
        return "{}".format(self.username)




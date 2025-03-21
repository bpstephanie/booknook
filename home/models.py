from django.db import models


# Create your models here.
class NewsletterSignup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_signed_up = models.DateTimeField(auto_now_add=True)

    def unsubscribe(self):
        self.delete()

    def __str__(self):
        return self.email

from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(default='hovno')
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email
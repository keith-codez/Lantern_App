from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)  # Phone number field
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to current date and time when the object is created

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    uploaded_file = models.FileField(upload_to='uploads/', blank=True, null=True)  # folder path inside MEDIA_ROOT

    def __str__(self):
        return self.name
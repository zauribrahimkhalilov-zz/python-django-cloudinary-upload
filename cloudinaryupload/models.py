from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField


class ImageUpload(models.Model):
    image = CloudinaryField('image')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.image

    class Meta:
        verbose_name_plural = "İmages"

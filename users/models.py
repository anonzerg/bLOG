from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_images")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()
        image_path = self.image.path
        image = Image.open(image_path)
        if image.height > 512 or image.width > 512:
            image_size = (512, 512)
            image.thumbnail(image_size)
            image.save(image_path)


from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            this = User.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except:
            pass
        super(User, self).save(*args, **kwargs)

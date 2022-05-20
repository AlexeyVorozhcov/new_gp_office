from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(
        upload_to="images/avatars/",
        default="images/avatars/default-avatar.jpg"
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        help_text="Имя пользователя или название магазина"
    )

    def __str__(self):
        return self.user.username

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Gallery(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='galleries',
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    icon = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class Picture(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        related_name='pictures',
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    image = models.ImageField(
        upload_to='pictures/',
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )

    class Meta:
        unique_together = ('gallery', 'name')

    def __str__(self):
        return self.name

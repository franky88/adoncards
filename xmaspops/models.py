from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import uuid
# Create your models here.


def image_file_location(instance, filename):
    return "theme/{0}/{1}".format(instance.id, filename)


class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=image_file_location,
                              help_text="Upload squre image dimension")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name.title()


class PopUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    user_update = models.ForeignKey(
        User, related_name='user_update', on_delete=models.SET_NULL, null=True)
    ref_code = models.CharField(max_length=15, unique=True)
    business_name = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    reinstatement = models.TextField(null=True, blank=True)
    text_color = models.CharField(max_length=60, default="#000000",
                                  help_text="You can customized text color")
    theme = models.ForeignKey(Theme, on_delete=SET_NULL, null=True, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.business_name.title()


@receiver(post_save, sender=PopUp)
def post_save_card_create_ref_code(sender, instance, created, *args, **kwargs):
    if created:
        instance.ref_code = str(uuid.uuid4()).replace('-', '')[:15]
        instance.save()

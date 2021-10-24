from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
import uuid
# Create your models here.


def save_image_location(instance, filename):
    imgpath = "image_{0}/{1}".format(instance.id, filename)
    return imgpath


class BackgroundImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=save_image_location)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class CardCategory(models.Model):
    category_name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Card Categories'

    def __str__(self):
        return self.category_name


class CardAdd(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=1)
    ref_code = models.CharField(max_length=12, unique=True, blank=True)
    category = models.ForeignKey(CardCategory, on_delete=SET_NULL, null=True)
    business_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField(verbose_name="message content")
    promotion = models.CharField(
        max_length=250, verbose_name="promotional offer")
    business_reinstatement = models.TextField()
    image = models.ForeignKey(
        BackgroundImage, on_delete=models.SET_NULL, null=True, verbose_name="background theme")
    card_link = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.business_name


@receiver(post_save, sender=CardAdd)
def post_save_card_create_ref_code(sender, instance, created, *args, **kwargs):
    if created:
        instance.ref_code = str(uuid.uuid4()).replace('-', '')[:12]
        instance.save()


@receiver(pre_save, sender=CardAdd)
def pre_save_card_link(sender, instance, *args, **kwargs):
    if instance.card_link == None:
        link = "http://localhost:8000/cards/details/%s" % (instance.ref_code)
        instance.card_link = link

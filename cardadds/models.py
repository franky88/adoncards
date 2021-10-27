from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.core.files.base import ContentFile
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
import uuid
import base64
import io
from PIL import Image
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
    title = models.CharField(
        max_length=200, default="Merry Christmas Happy New Year")
    content = models.TextField(verbose_name="message content",
                               default="We would like to wish all our valuable customers a Merry Christmas and Happy New Year and Holiday Season!")
    promotion = models.CharField(
        max_length=250, verbose_name="promotional offer", default="up to 30% off")
    business_reinstatement = models.TextField(
        default="We will be closed for the Christmas Season From 24th December to the 2nd January")
    image = models.ForeignKey(
        BackgroundImage, on_delete=models.SET_NULL, null=True, verbose_name="background theme")
    card_link = models.CharField(max_length=200, null=True, blank=True)
    base64 = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.business_name


# def base64_file(data, name=None):
#     _format, _img_str = data.split(';base64,')
#     _name, ext = _format.split('/')
#     if not name:
#         name = _name.split(":")[-1]
#     return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

def decodeDesignImage(data):
    try:
        data = base64.b64decode(data.encode('UTF-8'))
        buf = io.BytesIO(data)
        img = Image.open(buf)
        return img
    except:
        return None


@receiver(post_save, sender=CardAdd)
def post_save_card_create_ref_code(sender, instance, created, *args, **kwargs):
    if created:
        instance.ref_code = str(uuid.uuid4()).replace('-', '')[:12]
        link = "http://localhost:8000/card-link/%s" % (instance.ref_code)
        instance.card_link = link
        instance.save()


@receiver(pre_save, sender=CardAdd)
def pre_save_base64_text(sender, instance, *args, **kwargs):
    if instance.base64 == "":
        base64_img = CardAdd.objects.create(
            decodeDesignImage(instance.image.image))
        instance.base64 = base64_img

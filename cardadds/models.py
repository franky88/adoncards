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
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.


def save_image_location(instance, filename):
    imgpath = "image_{0}/{1}".format(instance.id, filename)
    return imgpath


class BackgroundImage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to=save_image_location, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class CardCategory(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
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
    updated_by = models.ForeignKey(
        User, related_name='updated_by', on_delete=models.SET_NULL, null=True)
    ref_code = models.CharField(max_length=12, unique=True, blank=True)
    category = models.ForeignKey(CardCategory, on_delete=SET_NULL, null=True)
    business_name = models.CharField(max_length=200)
    title = models.CharField(
        max_length=200, default="Merry Christmas Happy New Year", blank=True)
    content = models.TextField(verbose_name="message content", blank=True,
                               default="We would like to wish all our valuable customers a Merry Christmas and Happy New Year and Holiday Season!")
    promotion = models.CharField(
        max_length=250, verbose_name="promotional offer", default="up to 30% off", blank=True)
    business_reinstatement = models.TextField(
        default="We will be closed for the Christmas Season From 24th December to the 2nd January", blank=True)
    image = models.ForeignKey(
        BackgroundImage, on_delete=models.SET_NULL, null=True, verbose_name="background theme", default=1)
    is_posted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return self.business_name

    # def image_url(self):
    #     with open(self.image.image.path, 'rb') as imageFile:
    #         string = base64.b64encode(imageFile.read())
    #         print(str(string))
    #         # return string
    #     with open(self.image.image, "wb") as fh:
    #         fh.write(str.decode('base64'))
    #         return fh


# def decodeDesignImage(data):
#     try:
#         data = base64.b64encode(data.encode('UTF-8'))
#         buf = io.BytesIO(data)
#         img = Image.open(buf)
#         return img
#     except:
#         return None


@receiver(post_save, sender=CardAdd)
def post_save_card_create_ref_code(sender, instance, created, *args, **kwargs):
    if created:
        instance.ref_code = str(uuid.uuid4()).replace('-', '')[:12]
        link = "http://localhost:8000/card-link/%s" % (instance.ref_code)
        instance.card_link = link
        instance.save()


# @receiver(pre_save, sender=BackgroundImage)
# def pre_save_base64_text(sender, instance, *args, **kwargs):
#     if instance.base64 == "":
#         img = decodeDesignImage(instance.image)
#         img_io = io.BytesIO()
#         img.save(img_io, format='JPEG')
#         instance.base64 = InMemoryUploadedFile(
#             img_io, field_name=None, name=instance.name+instance.id+".jpg", content_type='image/jpeg', size=img_io.tell, charset=None)
        # instance.save()
        # instance.base64 = str(imgb64)

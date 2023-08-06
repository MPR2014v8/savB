import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.db import models

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
class AccountDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    address_number = models.IntegerField()
    address_detail = models.TextField()
    address_street = models.TextField()
    address_sub_district = models.TextField()
    address_district = models.TextField()
    address_province = models.TextField()
    address_post_code = models.IntegerField()
    phone = models.TextField()
    pic1 = models.ImageField(null=True, blank=True)
    pic_link1 = models.URLField(null=True, blank=True)
    
    def __str__(self) :
        return str(self.user.username)

class Transaction(models.Model):
    create_datetime = models.DateTimeField(default=datetime.datetime.now, blank=True)
    seller_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller_user")
    buyer_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="buyer_user")
    gest_buyer =models.BooleanField(default=False)
    gest_name = models.TextField(null=True, blank=True)
    gest_address_number = models.IntegerField()
    gest_address_detail = models.TextField(null=True, blank=True)
    gest_address_street = models.TextField(null=True, blank=True)
    gest_address_sub_district = models.TextField(null=True, blank=True)
    gest_address_district = models.TextField(null=True, blank=True)
    gest_address_province = models.TextField(null=True, blank=True)
    gest_address_post_code = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(default=0)     # 0=wait, 1=success, 2=closed
    
class TranDetails(models.Model):
    tran = models.ForeignKey(
        Transaction, on_delete=models.CASCADE, related_name="tran_detail")
    product_name = models.CharField(max_length=50)
    product_detail = models.TextField(null=True, blank=True)
    product_price = models.FloatField(null=True, blank=True)
    product_type = models.TextField(null=True, blank=True)
    pic1 = models.ImageField(null=True, blank=True)
    pic_link1 = models.URLField(null=True, blank=True)
    pic2 = models.ImageField(null=True, blank=True)
    pic_link2 = models.URLField(null=True, blank=True)
    pic3 = models.ImageField(null=True, blank=True)
    pic_link3 = models.URLField(null=True, blank=True)
    product_quantity = models.IntegerField(default=1)
    
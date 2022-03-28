from django.db.models.deletion import CASCADE, SET_NULL
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from housing_users.models import Account

class House(models.Model):
    name = models.CharField(max_length=300,unique=True,null=True),
    address = models.TextField(null=True),
    house_category = models.CharField(max_length=200,null=True)
    number_of_bedrooms = models.IntegerField(null=True)
    apartments_spaces = models.IntegerField(null=True)
    apartments_available = models.IntegerField(null=True)
    house_image = models.ImageField(null=True)
    livingroom_image = models.ImageField(null=True)
    kitchen_image = models.ImageField(null=True)
    sanitaryroom_image = models.ImageField(null=True)
    bathroom_image = models.ImageField(null=True)
    bedroom = models.ImageField(null=True)
    landlord = models.ForeignKey(Account,on_delete=CASCADE,null=True)

class User(models.Model):
    user = models.OneToOneField(Account,on_delete=CASCADE),
    house = models.ForeignKey(House,on_delete=SET_NULL),
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.username + "'s " + "profile"

    @receiver(post_save, sender=Account)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

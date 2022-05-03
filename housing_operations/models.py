from django.db.models.deletion import CASCADE, SET_NULL
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from housing_users.models import Account

class House(models.Model):
    house_name = models.CharField(max_length=300,null=True)
    house_category = models.CharField(max_length=200,null=True)
    number_of_bedrooms = models.IntegerField(null=True)
    apartments_spaces = models.IntegerField(null=True,blank=True)
    apartments_available = models.IntegerField(null=True,blank=True)
    house_image = models.ImageField(null=True)
    livingroom_image = models.ImageField(null=True)
    kitchen_image = models.ImageField(null=True)
    sanitaryroom_image = models.ImageField(null=True)
    bathroom_image = models.ImageField(null=True)
    bedroom_image = models.ImageField(null=True)
    landlord = models.ForeignKey(Account,on_delete=CASCADE,null=True)

    def __str__(self):
        return self.house_name

class Profile(models.Model):
    user = models.OneToOneField(Account,null=False,on_delete=CASCADE,default="",related_name="profile")
    house = models.ForeignKey(House,null=True,on_delete=SET_NULL,default="",related_name="house")

    def __str__(self):
        return self.user.username + "'s " + "profile"

    @receiver(post_save, sender=Account)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


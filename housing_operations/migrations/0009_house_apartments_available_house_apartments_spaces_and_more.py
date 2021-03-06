# Generated by Django 4.0.2 on 2022-05-03 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('housing_operations', '0008_remove_house_landlord'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='apartments_available',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='apartments_spaces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='bathroom_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='house',
            name='bedroom_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='house',
            name='house_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='house',
            name='kitchen_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='house',
            name='landlord',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='house',
            name='livingroom_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='house',
            name='number_of_bedrooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='sanitaryroom_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

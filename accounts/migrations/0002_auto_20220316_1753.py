# Generated by Django 2.2.24 on 2022-03-16 17:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]

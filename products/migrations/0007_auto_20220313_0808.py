# Generated by Django 2.2.24 on 2022-03-13 08:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220313_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='review_id',
            field=models.UUIDField(default=uuid.UUID('84944aa0-e329-4a1f-99c4-8863e175275a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='field_id',
            field=models.UUIDField(default=uuid.UUID('1200e63e-c692-4ae0-8749-adbf706fa010'), editable=False),
        ),
    ]

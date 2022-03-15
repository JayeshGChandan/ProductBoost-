# Generated by Django 2.2.24 on 2022-03-13 07:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220312_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='review_id',
            field=models.UUIDField(default=uuid.UUID('b4343626-d805-4407-b246-b44ab5a8ead4'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='field_id',
            field=models.UUIDField(default=uuid.UUID('b70c1da3-0d83-4dcc-b837-33bb6769029a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
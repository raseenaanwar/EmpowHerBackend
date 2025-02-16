# Generated by Django 5.0.3 on 2024-03-29 18:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_profile_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='city',
            new_name='profession',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
        migrations.CreateModel(
            name='OneTimePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

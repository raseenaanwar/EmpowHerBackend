# Generated by Django 5.0.3 on 2024-04-05 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='mentoring_language',
            new_name='language',
        ),
    ]

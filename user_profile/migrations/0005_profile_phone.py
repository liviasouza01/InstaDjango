# Generated by Django 3.1.2 on 2020-10-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
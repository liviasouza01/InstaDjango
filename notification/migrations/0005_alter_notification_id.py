# Generated by Django 5.0.3 on 2024-03-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20201015_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

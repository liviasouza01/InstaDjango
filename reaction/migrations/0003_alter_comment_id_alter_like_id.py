# Generated by Django 5.0.3 on 2024-03-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reaction', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

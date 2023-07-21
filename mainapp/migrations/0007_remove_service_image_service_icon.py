# Generated by Django 4.2 on 2023-07-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
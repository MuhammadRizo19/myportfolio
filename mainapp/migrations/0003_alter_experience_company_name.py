# Generated by Django 4.2 on 2023-07-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
    ]

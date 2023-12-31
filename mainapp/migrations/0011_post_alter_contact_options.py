# Generated by Django 4.2 on 2023-07-21 11:40

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_contact_sent_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=70)),
                ('post_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-sent_time']},
        ),
    ]

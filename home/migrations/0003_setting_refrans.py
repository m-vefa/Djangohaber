# Generated by Django 3.0.8 on 2020-07-12 11:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200712_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='refrans',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=255),
        ),
    ]

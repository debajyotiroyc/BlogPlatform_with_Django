# Generated by Django 3.1.2 on 2021-09-11 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_blog_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_id',
        ),
    ]

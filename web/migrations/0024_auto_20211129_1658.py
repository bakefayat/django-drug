# Generated by Django 3.2.6 on 2021-11-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_blog_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='updated',
        ),
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
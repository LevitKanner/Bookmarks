# Generated by Django 3.1.3 on 2020-12-03 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user_likes',
            new_name='liked_by',
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-09 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200309_1632'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auther',
            new_name='Author',
        ),
    ]
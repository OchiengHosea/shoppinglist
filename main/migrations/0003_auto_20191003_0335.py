# Generated by Django 2.2.6 on 2019-10-03 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191002_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingitem',
            old_name='list_name',
            new_name='list_ref',
        ),
    ]
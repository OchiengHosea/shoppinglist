# Generated by Django 2.2.6 on 2019-10-04 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191004_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingitem',
            old_name='item_id',
            new_name='shop_item_id',
        ),
    ]
# Generated by Django 2.2.6 on 2019-10-03 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191003_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingitem',
            name='id',
        ),
        migrations.AddField(
            model_name='shoppingitem',
            name='item_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]

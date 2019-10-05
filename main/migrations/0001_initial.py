# Generated by Django 2.2.6 on 2019-10-05 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=55)),
                ('overall_budget', models.DecimalField(decimal_places=2, max_digits=100)),
                ('minimum_refill_level', models.DecimalField(decimal_places=2, max_digits=100)),
                ('warning_message', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('shop_item_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('bought', models.BooleanField(default=True)),
                ('list_ref', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.ShoppingList')),
            ],
        ),
    ]

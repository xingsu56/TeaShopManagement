# Generated by Django 2.1.4 on 2019-01-07 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamanagement', '0014_sale_tea_tea_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale_tea',
            name='total_cost',
        ),
    ]
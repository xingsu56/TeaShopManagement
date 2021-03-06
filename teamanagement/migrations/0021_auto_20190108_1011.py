# Generated by Django 2.1.4 on 2019-01-08 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamanagement', '0020_goods_inout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('identity', models.CharField(max_length=50)),
                ('avatar', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='goods_inout',
            name='num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

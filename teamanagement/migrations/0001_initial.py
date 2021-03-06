# Generated by Django 2.1.4 on 2018-12-26 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('commodity_id', models.CharField(max_length=50)),
                ('commodity_name', models.CharField(max_length=100)),
                ('commodity_specification', models.CharField(max_length=100)),
                ('commodity_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=50)),
                ('merchant_name', models.CharField(max_length=100)),
                ('merchant_phone', models.CharField(max_length=50)),
                ('today', models.CharField(max_length=50)),
                ('estimated_time', models.CharField(max_length=50)),
                ('purchase_status', models.CharField(choices=[('finished', 'finished'), ('unfinished', 'unfinished')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='commodity_info',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamanagement.Purchase_info'),
        ),
    ]

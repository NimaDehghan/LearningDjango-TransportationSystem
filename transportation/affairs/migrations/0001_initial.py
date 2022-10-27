# Generated by Django 4.1.2 on 2022-10-27 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourierModel',
            fields=[
                ('courierId', models.IntegerField(primary_key=True, serialize=False)),
                ('cName', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('identityNo', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TransportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departDate', models.DateField()),
                ('arrivalDate', models.DateField()),
                ('vehicleNo', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100, null=True)),
                ('destination', models.CharField(max_length=100, null=True)),
                ('courierId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='affairs.couriermodel')),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='affairs.customermodel')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('isSuccessfull', models.BooleanField(default=False)),
                ('courierId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='affairs.couriermodel')),
            ],
        ),
    ]
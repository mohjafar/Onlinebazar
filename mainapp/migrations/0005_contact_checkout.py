# Generated by Django 4.1.2 on 2023-03-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Done')], default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('final', models.IntegerField()),
                ('rppid', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('paymentmode', models.IntegerField(choices=[(0, 'COD'), (1, 'Net Banking')], default=0)),
                ('paymentstatus', models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0)),
                ('orderstatus', models.IntegerField(choices=[(0, 'Order place'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Ready To Ship'), (4, 'Shipped'), (5, 'Out For Delivery'), (6, 'Delivered'), (7, 'Cancelled')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.buyer')),
            ],
        ),
    ]

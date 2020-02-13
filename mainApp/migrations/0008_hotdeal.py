# Generated by Django 2.0.3 on 2018-05-19 01:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_auto_20180518_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=10)),
                ('deal_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Product')),
            ],
        ),
    ]

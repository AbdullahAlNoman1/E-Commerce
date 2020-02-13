# Generated by Django 2.0.3 on 2018-05-19 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_todaydeal'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeacialDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Product')),
            ],
        ),
    ]

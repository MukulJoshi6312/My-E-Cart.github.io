# Generated by Django 3.0.8 on 2021-05-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

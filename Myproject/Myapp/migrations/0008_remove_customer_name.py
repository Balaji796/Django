# Generated by Django 4.1.4 on 2023-01-28 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0007_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Name',
        ),
    ]
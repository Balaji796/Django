# Generated by Django 4.1.4 on 2023-01-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0006_alter_bill_cash'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30, null=True)),
                ('Name', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('addr', models.CharField(max_length=30, null=True)),
                ('amount', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2023-11-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='for_test_purposes',
            field=models.TextField(blank=True, null=True),
        ),
    ]

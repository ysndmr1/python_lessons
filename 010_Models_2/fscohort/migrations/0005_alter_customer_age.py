# Generated by Django 4.2.1 on 2023-05-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0004_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(blank=True, choices=[(10, 'Age:10'), (20, 'Age:20'), (30, 'Age:30'), (40, 'Age:40'), (50, 'Age:50'), (60, 'Age:60')], default=0, null=True),
        ),
    ]

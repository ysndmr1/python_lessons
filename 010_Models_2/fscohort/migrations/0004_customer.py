# Generated by Django 4.2.1 on 2023-05-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0003_alter_student_email_alter_student_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]

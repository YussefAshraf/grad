# Generated by Django 4.2 on 2024-04-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livero', '0003_alter_readings_fbi_result_alter_readings_kidney_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

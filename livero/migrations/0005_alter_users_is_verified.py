# Generated by Django 4.2 on 2024-04-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livero', '0004_alter_users_first_name_alter_users_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.2 on 2024-04-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livero', '0002_alter_users_options_alter_users_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readings',
            name='fbi_result',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='readings',
            name='kidney',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=120, null=True),
        ),
        migrations.AlterField(
            model_name='readings',
            name='liver',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='readings',
            name='urine',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=90, null=True),
        ),
    ]
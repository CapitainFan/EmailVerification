# Generated by Django 4.2.9 on 2024-01-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0005_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='20f1ed', max_length=6),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_group_group_encryption_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin_logged_in',
            field=models.BooleanField(default=False),
        ),
    ]
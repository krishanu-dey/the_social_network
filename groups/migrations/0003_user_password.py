# Generated by Django 3.0.5 on 2020-04-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_user_admin_logged_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='posts',
            field=models.ManyToManyField(null=True, related_name='group', to='groups.Post'),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-01 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0006_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='private',
        ),
    ]

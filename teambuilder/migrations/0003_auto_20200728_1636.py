# Generated by Django 3.0.8 on 2020-07-28 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0002_auto_20200728_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teambuilder.Pokemon'),
        ),
    ]

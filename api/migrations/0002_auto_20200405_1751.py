# Generated by Django 3.0.5 on 2020-04-05 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='start',
            new_name='stars',
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-08 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20191102_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='setting_specfic',
            new_name='setting_specific',
        ),
    ]

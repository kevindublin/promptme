# Generated by Django 2.2.7 on 2019-11-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20191110_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='feedback_amount',
            field=models.IntegerField(default=0),
        ),
    ]
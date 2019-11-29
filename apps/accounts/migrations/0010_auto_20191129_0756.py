# Generated by Django 2.2.7 on 2019-11-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20191129_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='membership',
            field=models.IntegerField(choices=[(0, 'Member'), (1, 'Plus'), (2, 'Premium'), (3, 'Professional'), (4, 'Student'), (5, 'Instructor')], default='0'),
        ),
    ]

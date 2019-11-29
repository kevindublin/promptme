# Generated by Django 2.2.7 on 2019-11-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20191129_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='membership',
            field=models.CharField(choices=[('Member', 'Member'), ('Plus', 'Plus'), ('Premium', 'Premium'), ('Professional', 'Professional'), ('Student', 'Student'), ('Instructor', 'Instructor')], default='Member', max_length=12),
        ),
    ]

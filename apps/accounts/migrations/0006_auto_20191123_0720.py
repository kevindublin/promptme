# Generated by Django 2.2.7 on 2019-11-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191123_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='membership',
            field=models.CharField(choices=[('Member', 'Member'), ('Plus', 'Plus'), ('Premium', 'Premium'), ('Professional', 'Professional'), ('Instructor', 'Instructor'), ('Student', 'Student')], default='Member'),
        ),
    ]

# Generated by Django 2.2.10 on 2020-03-20 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200318_0628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='pov_clear',
            new_name='clear_pov',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='worldview',
            new_name='clear_worldview',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='style_distinct',
            new_name='distinct_style',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='adjective_specific',
            new_name='specific_adjectives',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='noun_specific',
            new_name='specific_nouns',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='setting_specific',
            new_name='specific_setting',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='verb_specific',
            new_name='specific_verbs',
        ),
    ]

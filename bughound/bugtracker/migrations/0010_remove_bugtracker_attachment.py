# Generated by Django 4.0.6 on 2022-07-26 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0009_alter_bugtracker_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugtracker',
            name='attachment',
        ),
    ]

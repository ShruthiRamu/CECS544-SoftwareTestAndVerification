# Generated by Django 4.0.6 on 2022-07-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0007_bugtracker_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugtracker',
            name='attachment',
            field=models.FileField(upload_to='pdfs/'),
        ),
    ]

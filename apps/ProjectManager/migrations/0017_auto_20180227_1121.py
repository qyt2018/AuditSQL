# Generated by Django 2.0.2 on 2018-02-27 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0016_auto_20180227_1117'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inceptionhostconfig',
            unique_together={('host',)},
        ),
    ]

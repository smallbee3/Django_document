# Generated by Django 2.0.2 on 2018-02-11 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0006_auto_20180211_1218'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]

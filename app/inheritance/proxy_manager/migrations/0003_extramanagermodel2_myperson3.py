# Generated by Django 2.0.2 on 2018-10-12 10:05

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_manager', '0002_auto_20180209_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraManagerModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            managers=[
                ('secondary', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MyPerson3',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy_manager.extramanagermodel2',),
            managers=[
                ('secondary', django.db.models.manager.Manager()),
            ],
        ),
    ]
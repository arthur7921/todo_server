# Generated by Django 3.0.4 on 2020-03-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='userTag',
            field=models.IntegerField(),
        ),
    ]

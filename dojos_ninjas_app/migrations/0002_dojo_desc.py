# Generated by Django 2.2.4 on 2022-09-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojos_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.8 on 2021-10-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate_angle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate_angle',
            name='nome',
            field=models.CharField(default='exit', max_length=20),
            preserve_default=False,
        ),
    ]

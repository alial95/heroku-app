# Generated by Django 3.1.3 on 2020-11-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Please add a profile.', max_length=200),
        ),
    ]

# Generated by Django 3.1 on 2021-02-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_auto_20210207_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

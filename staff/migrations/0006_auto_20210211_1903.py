# Generated by Django 3.1 on 2021-02-11 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20210208_1921'),
        ('staff', '0005_auto_20210211_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='subjects',
            field=models.ManyToManyField(blank=True, default=[], to='subject.Subject'),
        ),
    ]

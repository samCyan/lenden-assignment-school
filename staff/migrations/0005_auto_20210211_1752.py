# Generated by Django 3.1 on 2021-02-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20210208_1921'),
        ('staff', '0004_staff_takes_web_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='subjects',
            field=models.ManyToManyField(default=[], to='subject.Subject'),
        ),
    ]
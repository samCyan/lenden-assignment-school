# Generated by Django 3.1 on 2021-02-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20210208_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='shape',
            field=models.CharField(choices=[('oval', 'Oval'), ('rectangular', 'Rectangular'), ('canopy', 'Canopy'), ('elevated', 'Elevated')], default='Oval', max_length=20),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='web_lecture',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Active', max_length=20),
        ),
    ]
# Generated by Django 3.1 on 2021-02-07 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_auto_20210207_1124'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='subjects',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subject.subject'),
        ),
    ]
# Generated by Django 2.1.1 on 2020-03-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200318_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='pwd',
            field=models.CharField(max_length=32, null=True),
        ),
    ]

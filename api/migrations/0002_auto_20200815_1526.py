# Generated by Django 3.0.5 on 2020-08-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userac',
            name='token',
            field=models.CharField(max_length=24, null=True),
        ),
    ]

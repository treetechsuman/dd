# Generated by Django 4.0.3 on 2022-03-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_rename_number_ward_ward_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='coordinate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='municipality',
            name='coordinate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='province',
            name='coordinate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ward',
            name='coordinate',
            field=models.TextField(blank=True),
        ),
    ]

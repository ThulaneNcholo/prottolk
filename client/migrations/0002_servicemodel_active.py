# Generated by Django 4.2.2 on 2023-07-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='active',
            field=models.CharField(blank=True, default='No', max_length=200, null=True),
        ),
    ]

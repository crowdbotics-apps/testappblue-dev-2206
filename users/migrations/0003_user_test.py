# Generated by Django 2.2.11 on 2020-03-31 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200331_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]

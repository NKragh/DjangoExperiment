# Generated by Django 2.2.6 on 2019-10-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='title',
            field=models.TextField(default='Default Artist'),
        ),
    ]

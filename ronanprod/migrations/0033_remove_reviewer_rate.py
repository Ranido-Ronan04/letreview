# Generated by Django 3.1.6 on 2021-06-24 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ronanprod', '0032_auto_20210624_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewer',
            name='rate',
        ),
    ]

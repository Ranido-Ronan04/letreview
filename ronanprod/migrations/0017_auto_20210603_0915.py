# Generated by Django 3.1.6 on 2021-06-03 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ronanprod', '0016_auto_20210603_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='contact',
            new_name='cname',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='name',
            new_name='num',
        ),
    ]

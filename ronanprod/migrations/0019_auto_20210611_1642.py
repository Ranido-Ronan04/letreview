# Generated by Django 3.1.6 on 2021-06-11 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ronanprod', '0018_auto_20210611_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='Lecturer',
            new_name='lecturer',
        ),
    ]

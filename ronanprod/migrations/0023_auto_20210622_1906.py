# Generated by Django 3.1.6 on 2021-06-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ronanprod', '0022_auto_20210612_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=1000, null=True)),
                ('test', models.DateField(null=True)),
                ('payment', models.IntegerField(null=True)),
                ('ses', models.CharField(max_length=50, null=True)),
                ('discount', models.IntegerField(null=True)),
                ('user', models.ManyToManyField(to='ronanprod.Participant')),
            ],
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]

# Generated by Django 2.0rc1 on 2017-11-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171127_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('d_o_b', models.DateField(verbose_name='Date of Birth')),
                ('nationality', models.CharField(max_length=100)),
                ('employment', models.DateField(verbose_name='Date of Employment')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, verbose_name='Mobile Phone')),
                ('status', models.CharField(choices=[('m', 'Married'), ('s', 'Single'), ('n', 'None')], max_length=1)),
                ('emp_status', models.CharField(choices=[('p', 'Permanent'), ('c', 'Contractual')], max_length=1, verbose_name='Employment')),
            ],
        ),
    ]

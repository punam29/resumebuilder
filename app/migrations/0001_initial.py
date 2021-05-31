# Generated by Django 3.1 on 2021-05-16 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('phoneno', models.IntegerField()),
                ('emailid', models.CharField(max_length=100)),
                ('profilepic', models.CharField(max_length=200)),
                ('skills', models.TextField()),
                ('designation', models.CharField(max_length=100)),
                ('jobdescription', models.TextField()),
                ('yearsofexperience', models.IntegerField()),
                ('schoolname', models.CharField(max_length=100)),
                ('schoolduration', models.CharField(max_length=100)),
                ('collegename', models.CharField(max_length=100)),
                ('collegeduration', models.CharField(max_length=100)),
            ],
        ),
    ]

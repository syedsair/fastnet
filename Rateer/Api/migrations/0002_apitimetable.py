# Generated by Django 4.0.2 on 2022-04-18 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept', models.CharField(max_length=30)),
                ('CourseCode', models.CharField(max_length=10)),
                ('CourseName', models.CharField(max_length=50)),
                ('Day', models.CharField(max_length=8)),
                ('Venue', models.CharField(max_length=15)),
                ('StartsAt', models.CharField(max_length=5)),
                ('EndsAt', models.CharField(max_length=5)),
            ],
        ),
    ]

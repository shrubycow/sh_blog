# Generated by Django 3.0.3 on 2020-03-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh_blog', '0006_auto_20200316_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todayschedule',
            name='endLessonTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='todayschedule',
            name='startLessonTime',
            field=models.TimeField(),
        ),
    ]
# Generated by Django 3.0.3 on 2020-03-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh_blog', '0005_todayschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todayschedule',
            name='id',
        ),
        migrations.AddField(
            model_name='todayschedule',
            name='lesson_numb',
            field=models.SmallIntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
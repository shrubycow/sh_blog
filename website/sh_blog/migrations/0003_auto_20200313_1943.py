# Generated by Django 3.0.3 on 2020-03-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh_blog', '0002_auto_20200312_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]

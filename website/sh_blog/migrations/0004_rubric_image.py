# Generated by Django 3.0.3 on 2020-03-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh_blog', '0003_auto_20200313_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubric',
            name='image',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-12 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sh_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rubric',
            options={'ordering': ('name',), 'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
    ]
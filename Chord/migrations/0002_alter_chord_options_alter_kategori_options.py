# Generated by Django 4.1.3 on 2022-12-15 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chord', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chord',
            options={'ordering': ['songname'], 'verbose_name_plural': 'Kategori'},
        ),
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Kategori'},
        ),
    ]
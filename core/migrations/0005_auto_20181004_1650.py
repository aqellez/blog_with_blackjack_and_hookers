# Generated by Django 2.1.1 on 2018-10-04 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180923_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publication_date']},
        ),
    ]

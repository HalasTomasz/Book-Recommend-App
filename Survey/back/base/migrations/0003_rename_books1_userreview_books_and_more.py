# Generated by Django 4.1.2 on 2022-11-23 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_books_userreview_books1_userreview_books2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreview',
            old_name='Books1',
            new_name='Books',
        ),
        migrations.RemoveField(
            model_name='userreview',
            name='Books2',
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='Author_Name',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]

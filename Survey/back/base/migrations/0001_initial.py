# Generated by Django 4.1.2 on 2022-11-23 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('Order_ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Review1', models.IntegerField(blank=True, default=0, null=True)),
                ('Review2', models.IntegerField(blank=True, default=0, null=True)),
                ('Books', models.CharField(blank=True, max_length=255, null=True)),
                ('Date_Taken', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

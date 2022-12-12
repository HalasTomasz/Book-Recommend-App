# Generated by Django 4.1.2 on 2022-11-26 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_algorithmrecomendations'),
    ]

    operations = [
        migrations.CreateModel(
            name='OFFTOP_Recomendations',
            fields=[
                ('NrRecomendations', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('ROW_ID', models.IntegerField(blank=True, null=True)),
                ('Book_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.book')),
            ],
        ),
    ]
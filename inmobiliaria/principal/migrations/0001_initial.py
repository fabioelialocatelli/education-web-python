# Generated by Django 2.0.6 on 2018-06-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=50)),
                ('descrip', models.TextField()),
                ('precio', models.FloatField()),
                ('ref', models.IntegerField()),
            ],
        ),
    ]

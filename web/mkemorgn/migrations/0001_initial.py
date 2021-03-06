# Generated by Django 4.0.4 on 2022-05-31 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_photo_url', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'About Photo URL',
            },
        ),
        migrations.CreateModel(
            name='Denver2020Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Denver 2020 Photos',
            },
        ),
        migrations.CreateModel(
            name='Detroit2020Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Detroit 2020 Photos',
            },
        ),
        migrations.CreateModel(
            name='IndexPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Index Photos',
            },
        ),
        migrations.CreateModel(
            name='LA2021Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'LA 2021 Photos',
            },
        ),
        migrations.CreateModel(
            name='TripsPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trips_photo_url', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Trips Page Photo URLs',
            },
        ),
    ]

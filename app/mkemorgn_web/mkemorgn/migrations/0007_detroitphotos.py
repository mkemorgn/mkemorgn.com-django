# Generated by Django 4.0.2 on 2022-05-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkemorgn', '0006_tripsphotos_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetroitPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Detroit Photos',
            },
        ),
    ]
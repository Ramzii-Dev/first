# Generated by Django 4.0.5 on 2022-06-09 15:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_livre_date_update_alter_presentation_adresse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Galerie',
                'verbose_name_plural': 'Galeries',
            },
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 17, 25, 3, 86652)),
        ),
        migrations.CreateModel(
            name='GaleriesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.ImageField(upload_to='C:\\Users\\RAMZI\\projet_django\\Emma\\src\\webapp\\static/images/publication_images')),
                ('galeries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='webapp.galeries')),
            ],
        ),
    ]
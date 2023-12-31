# Generated by Django 4.2.2 on 2023-06-20 15:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_pic', models.ImageField(upload_to='categoris')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=200)),
                ('audio', models.FileField(upload_to='music/')),
                ('music_pic', models.ImageField(upload_to='music/pics/')),
                ('period', models.TimeField()),
                ('date_diffusion', models.DateField(default=django.utils.timezone.now)),
                ('views', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('keywords', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gqapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='PlayListe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playliste_name', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('music_included', models.ManyToManyField(to='gqapp.music')),
            ],
        ),
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mixname', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('music_included', models.ManyToManyField(to='gqapp.music')),
            ],
        ),
    ]

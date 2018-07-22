# Generated by Django 2.0.7 on 2018-07-22 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name (e.g. Christopher Nolan)', max_length=150)),
                ('birth_date', models.CharField(help_text='Use the following format: dd/mm/yyyy', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name (e.g. Warner Bros)', max_length=150)),
                ('city', models.CharField(help_text='Enter the city name (e.g. Los Angeles)', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(related_name='people', to='api.People'),
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='api.People'),
        ),
        migrations.AddField(
            model_name='film',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studio', to='api.Studio'),
        ),
    ]

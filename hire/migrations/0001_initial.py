# Generated by Django 3.1.2 on 2020-10-13 19:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tables', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
                ('cake', models.BooleanField(default=False)),
                ('event_size', models.CharField(choices=[('1', '0-50'), ('2', '50-100'), ('3', '100-200'), ('4', '200+')], max_length=10)),
                ('event_type', models.CharField(choices=[('1', 'Wedding'), ('2', 'Birthday'), ('3', 'Chama'), ('4', 'Any other')], max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_date', models.DateTimeField()),
                ('resources', models.CharField(help_text='Example, chairs, tents. Separate with a comma', max_length=1000)),
                ('AoB', models.CharField(help_text='Anything you should let us know, include it here?', max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
